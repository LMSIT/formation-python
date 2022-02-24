# Initiation au langage Python

---

## Accueil

---

## Résumé du planning de la formation

---

## Objectifs pédagogiques

* Réaliser des scripts en Python
* Reconnaître et résoudre une erreur Python
* Suivre les bonnes pratiques de développement
* Documenter du code et un projet Python
* Versionner un projet avec Git
* Les bases du CI/CD

> Une mise en pratique après la formation est indispensable.

---

## Les moyens techniques de cette formation

* [Support de cours](EXERCICE_URL)
* [GitLab](https://git.lbn.fr/python-training/training-2020-10-19)
* [Slack](https://app.slack.com/client/T2L2LRYNN/G01CUK03LUR)

---

## Préparation de l'environnement

* Python
* Git
* GitLab
* VSCode
* Docker (optionnel)

---

## Introduction à Python

---

### Python VS les autres languages

* Installé par défaut sur la plupart des distributions Linux
* Pas de compilation, l'exécution du code est immédiate
* Courbe d'apprentissage rapide
* Langage structurant
* Beaucoup de documentation et d'exemples sur internet
* Librairies disponibles pour tous les Cloud Providers
* C'est aussi, une question d'appétence !

---

### Les Success Stories Python

- [Django](https://www.djangoproject.com/)
- [Ansible](https://github.com/ansible/ansible)
- [OpenStack](https://github.com/openstack)
- [docker-compose](https://github.com/docker/compose)
- Python scientifique (Scipy|Matplotlib|Numpy)
- Machine Learning (scikit-learn)
- Big Data (Pandas)

---

### Python et le Cloud

- Amazon AWS
    - [Lambda serverless](https://docs.aws.amazon.com/fr_fr/lambda/latest/dg/lambda-python.html)
    - [Boto3](https://aws.amazon.com/fr/sdk-for-python/)
- Microsoft Azure
    - [Azure Functions](https://docs.microsoft.com/fr-fr/azure/azure-functions/functions-reference-python)
    - [azure-cli](https://github.com/Azure/azure-cli)
- Google GCP
    - [Cloud Functions](https://cloud.google.com/functions/docs/quickstart-python?hl=fr)
    - [App Engine](https://cloud.google.com/appengine/docs/python?hl=fr)

---

### Python2 vs Python3

- **Python 3** est disponible depuis **fin 2008**
    - La version minimum encore maintenu est la 3.6 jusqu'au 23/12/2021
- **Python 2** n'est plus supporté par l'éditeur depuis le 1er Janvier 2020
- Encodage natif en UTF8
- Coroutines avec AsyncIO
- Les principales différences sont décrites [ici](https://python-future.org/compatible_idioms.html)
- Outil de conversion Python2 -> Python3 : [2to3](https://docs.python.org/fr/3.6/library/2to3.html)

---

### L'Ecosystème Python

- [Dépôt central des projets Python](https://pypi.org/)
- [Référentiel d'outils et projets Python](https://github.com/vinta/awesome-python)
- [Github](https://github.com/topics/python?l=python&o=desc&s=stars)
- [Peps](https://www.python.org/dev/peps/)

---

### IDE pour Python

- [VSCode](https://code.visualstudio.com/)
- [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/)
- [Eclipse Pydev](https://www.pydev.org/)
- [Atom](https://atom.io/packages/ide-python)

---

### Trouver de l'aide sur Python

- Fonction help dans le shell Python
- [Documentation Python](https://docs.python.org/fr/3.8/)
- [Modules standards](https://docs.python.org/fr/3/py-modindex.html)
- [stackoverflow](https://stackoverflow.com/questions/tagged/python)
- [developpez.com](https://python.developpez.com/)
- [Algorithmie](https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md)
- [Designs Patterns](https://github.com/faif/python-patterns)

---

## Les bases du langage Python

---

### Les bases du langage

* Python en ligne de commande
* Le shell Python
* Shell avancé avec iPython
* Les types de base
* Variables & Constantes
* Formatage des chaines
* Manipulation de chaines
* Calcul avec les types numériques
* Le type None
* Le type Boolean

---

### Les bases du langage (suite)

* Les tableaux indexés (list/tuple)
* Les tableaux associatifs (dict)
* Python et l’indentation
* La boucle for
* La boucle while
* Conditions if/elif/else
* Les dates avec le module datetime
* Lecture et écriture dans un fichier
* Passage du shell au script Python

---

## Exercice n°1

Un client vous demande de générer un fichier [htaccess](http://httpd.apache.org/docs/current/howto/htaccess.html) pour Apache à partir d'une liste d'adresse IP qu'il vous fournit dans un ticket. 

Dans un premier temps, nous allons uniquement afficher le résultat à l'écran, plus tard nous verrons comment l'écrire dans un fichier.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex1)

---

### Correction de l'exercice n°1

---

## Lecture d'un fichier CSV

* Lecture avec un tableau par ligne (csv.reader)
* Lecture avec un dictionnaire par ligne (csv.DictReader)

---

## Exercice n°2

La demande du client évolue, vous allez maintenant générer le fichier .htaccess à partir d’un fichier CSV qui contiendra également une colonne pour appliquer un Deny ou un Allow sur chaque adresse IP

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex2)

---

### Correction de l'exercice n°2

---

## Gestion des erreurs en Python

---

## Les logs Python avec le module logging

---

## Exercice n°3

À la suite d’erreurs dans le format d’adresse IP, vous allez ajouter une validation du format dans le générateur de fichier .htaccess à l’aide du module standard [ipaddress](https://docs.python.org/fr/3.7/library/ipaddress.html) 

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex3)

---

### Correction de l'exercice n°3

---

## Retour sur les acquis de la journée

- Les bases du langage
- Les exceptions
- Le logging
- Versionning avec Git
- Etat de l'application de génération de fichier .htaccess

---

## Les fonctions en Python

---

## Les modules python et la function import

---

## Exercice n°4

Transformez le code du générateur de fichier .htaccess en le réécrivant sous forme de fonction et appelez les fonctions à l’intérieur d’une fonction main.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex4)

---

### Correction de l'exercice n°4

---

## Documenter du code Python

---

## Documenter un projet Python avec Markdown

---

## Exercice n°5

Appliquez les bonnes pratiques de nommage. Documentez le code et le projet pour le générateur de fichier .htaccess

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex5)

---

### Correction de l'exercice n°5

---

## Le module argparse pour des options en ligne de commande

---

## Exercice n°6

Dans le générateur de fichier .htaccess, utilisez argparse pour choisir l’emplacement du fichier CSV et le niveau de logging.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex6)

---

### Correction de l'exercice n°6

---

## Configuration dynamique à l’aide des variables d’environnement

---

## Exercice n°7

Dans notre générateur, configurez l’emplacement du fichier .htaccess à l’aide d’une variable d’environnement.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex7)

---

### Correction de l'exercice n°7

---

## Utilisation de templates Jinja

---

## Exercice n°8

Créez et utilisez un template Jinja pour formater le fichier .htaccess

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex8)

---

### Correction de l'exercice n°8

---

## Introduction aux tests unitaires

---

## Exercice n°9

Créez un test unitaire pour la fonction qui renvoi le résultat du template Jinja.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex9)

---

### Correction de l'exercice n°9

---

## Retour sur les acquis

- Documenter du code
- Documenter un projet
- Le module argparse
- La configuration par variable d'environnement
- Template Jinja
- Les tests unitaires

---

## Introduction au CI/CD avec Gitlab-CI

---

## Exercice n°10

Automatisez l’exécution du test unitaire développé lors de l’exercice n°9 pour qu’il s’exécute à chaque commit du code sur Gitlab.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex10)

---

### Correction de l'exercice n°10

---

## Introduction aux tests qualités

---

## Exercice n°11

Corrigez le code et ajoutez l’automatisation du test qualité au fichier .gitlab-ci.yml

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex11)

---

### Correction de l'exercice n°11

---

## Exercice n°12

Dépannez et améliorez les scripts qui vous seront fournis

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex12)

---

### Correction de l'exercice n°12

---

## Lecture/Ecriture de fichier JSON

---

## Lecture/Ecriture de fichier YAML

---

## Survol des modules standards Python les plus utiles

---

## Consommation de service web avec la librairie requests

---

## Exercice n°13

Avec la librairie requests, téléchargez le contenu du service web  https://jsonplaceholder.typicode.com/todos et écrivez le dans un fichier todos.json

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex13)

---

### Correction de l’exercice n°13

---

## Production de service web avec le framework flask

---

## Exercice n°14

Fournissez une route avec Flask qui exposera le service web /todos et consommez ce service avec requests.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex14)

---

### Correction de l’exercice n°14

---

## Retour sur les acquis

- Le CI/CD avec Gitlab-CI
- Test qualité
- Dépanner du code Python
- Gestion de fichiers JSON/YAML
- Les modules standard les plus utiles
- Consommer et produire des services Web

---

## La notion de Package en Python

---

## L’outil pip et le fichier requirements.txt

---

## Le déploiement d’un projet Python avec setup.py

---

## Exercice n°15

Ajoutez un setup.py au générateur de fichier .htaccess et modifiez, le CI/CD pour l’utiliser lors de l’installation.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex15)

---

### Correction de l’exercice n°15

---

## Analyser et comprendre un projet Python existant

- La compatibilité avec Python3
- Les dépendances
- Les bonnes pratiques
- La conformité PEP8
- Les tests automatisés
- La documentation

---

## Exercice n°16

Chaque participant va créer une nouvelle branche de son projet et introduire des bugs qui seront corrigés par un autre participant.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex16)

---

## Exécution de commandes systèmes

- subprocess
- pyinvoke

---

## Exercice n°17

A l’aide de subprocess ou de pyinvoke, affichez la liste des fichiers du répertoire /tmp.

[Lien vers l'exercice](EXERCICE_URL/#/exercices/ex17)

---

### Correction de l’exercice n°17

---

## Les possibilités de traitements parallèles en Python

- https://www.programmersought.com/article/32442087347/

- Le multi threading
- Le multi processing
- Les coroutines
- Les workers
- Les micros-services

---

## Introduction au modèle objet en Python

- Les classes
- Les instances de classe
- L'héritage
- Les méthodes (fonctions)

---

## Introduction au ServerLess

---

## Introduction à Ansible

---

## Questions/Réponses et conclusion de la formation
