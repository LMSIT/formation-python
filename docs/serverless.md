# Introduction au ServerLess

## Introduction

Le concept du [ServerLess](https://en.wikipedia.org/wiki/Serverless_computing) est le plus souvent, associé à celui des [micro-services](https://en.wikipedia.org/wiki/Microservices).

Le ServerLess ne veut pas vraiment dire, **sans serveur** car il y a bien sûr, des serveurs mais ça ne nous concerne plus car ils sont transparents pour le développeur ou le consommateur de fonctions.

**Ce qui distingue le ServerLess d'une application standard:**

- Exécution à la demande (le serveur qui est plutôt un conteneur de type Docker) est allumé seulement quand il y a une demande.
- Gestion d'Evènements: Les fonctions s'exécute seulement quand survienne un évènement. Le plus courant est un evènement de type HTTP Get mais aussi, à l'arrivé d'un fichier dans un stockage réseau, au moment de la suppression d'une ressource dans votre souscription cloud, ...
- Facturation à l'exécution: Comme il n'y a plus de notions de serveur, il fallait bien trouver un modèle économique viable. Les fonctions sont donc facturés à l'exécution selon différents critères (nombre d'exécution, durée, consommation RAM/CPU, ..)
- Exécution parallèles et indépendantes d'instances d'une même fonction

**Rapprochons notre expérience** de développement du générateur de fichier .htaccess avec le ServerLess et les micro-services:
- Un fichier .csv contenant les adresses IP est fournit par le client dans un stockage de type Storage Account chez Azure
- L'exécution d'une fonction **parse_ip** que nous avons déployé chez Azure, est activé automatiquement et après avoir remplie son rôle, elle envoi le résultat dans un fichier .htaccess, sur un Storage Account.
- Une autre fonction qui réagit à l'arrivé d'un fichier .htaccess, est chargé de se connecter à toutes les machines contenant un Apache pour remplacer le fichier .htaccess puis relancer le service Apache.

Avec du ServerLess, nous aurions peut-être ajouté des **étapes supplémentaires** comme:
- Enregistrement des IP dans une BDD
- Alimentation de statistiques
- Génération d'un rapport
- ...

## Azure Functions

- https://azure.microsoft.com/fr-fr/services/functions/

> Les procédures d'installation suivantes ont été réalisés sur Ubuntu 20.04 (WSL2). Vous trouverez [ici](https://docs.microsoft.com/fr-fr/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash) des instructions concernant les autres distributions.

**Installation de azure cli:**

```shell
sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Installation du azure-functions-core-tools:**

```shell
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-get update
sudo apt-get install azure-functions-core-tools-3
```

**Création d'un projet Azure Function avec un runtime python:**

```shell
func init htaccess-generator-func --worker-runtime python --source-control
```

```shell
# Exécutez cette commande pour visualiser la structure du projet:
find htaccess-generator-func
htaccess-generator-func/.gitignore
htaccess-generator-func/host.json
htaccess-generator-func/.vscode
htaccess-generator-func/.vscode/extensions.json
htaccess-generator-func/local.settings.json
htaccess-generator-func/requirements.txt
```

```shell
cd htaccess-generator-func
git init

# Création d'un environnement virtuel python
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel

# Installation des dépendances pour Azure Function Python
pip install -r requirements.txt
```

**Liste des templates de création de functions:**

```shell
# Templates pour tous les languages pris en charges
func templates list

# Templates pour python
func templates list -l python
```

**Création d'une fonction de type HTTP Trigger:**

Le but de la fonction ValidateIpAddress serait dans notre cas, de recevoir une ou plusieurs adresse IP, de les valider et de générer une erreur 4xx si il y a une ip en erreur.

Si toutes les IP sont valides, la fonction pourrait envoyer ces Ips dans une queue et s'arrêter ici.

Ce serait une autre fonction, à l'écoute d'evènement dans une queue, qui prendrait la suite pour, par exemple, générer le fichier final puis l'écrire dans un blob d'un Storage Account Azure afin qu'une autre fonction l'envoi sur les serveurs Apache.

```
func new --name ValidateIpAddress --template "HTTP trigger"
```

**Fichiers créés par la commande `func new`:**

**ValidateIpAddress/__init__.py:**

```python
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
```

**ValidateIpAddress/function.json:**

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get",
        "post"
      ]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

**Démarrage local de la fonction:**

```shell
func start
```

**Test de la fonction:**

TODO: A terminer !

**Publication des fonctions sur Azure:**

> A faire une seule fois, avec azure-cli, Terraform, le portail Azure ou tout autres moyens

```shell
AZURE_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
AZURE_REGION=westeurope
AZURE_RESOURCE_GROUP=RG_TRAINING
STORAGE_ACCOUNT_NAME=trainingstorage
FUNCTION_APP_NAME=lbn-htaccess-generator-uat

# Compte azure ou service principal
az login -u VOTRE_COMPTE_AZURE
az account set -s $AZURE_SUBSCRIPTION_ID

# Création du Storage Account
az storage account create --name $STORAGE_ACCOUNT_NAME --location $AZURE_REGION \
--resource-group $AZURE_RESOURCE_GROUP --sku Standard_LRS

# Création de l'application de fonctions
az functionapp create --name $FUNCTION_APP_NAME --resource-group $AZURE_RESOURCE_GROUP \
-c $AZURE_REGION --runtime python --runtime-version 3.8 --os-type Linux \
--functions-version 3 --storage-account $STORAGE_ACCOUNT_NAME
```

**Publication de l'application:**

> A faire à chaque fois que vous voulez publiez une mise à jour de vos fonctions

```shell
func azure functionapp publish $FUNCTION_APP_NAME
```

## AWS Lambda

- https://aws.amazon.com/fr/lambda/

TODO: exemple

## Google Functions

- https://cloud.google.com/functions/

TODO: exemple
