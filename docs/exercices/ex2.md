# Exercice n°2

## Scénario

La demande du client évolue, vous allez maintenant générer le fichier htaccess.txt à partir d’un fichier [CSV](https://docs.python.org/fr/3.7/library/csv.html#csv.reader) qui contiendra également une colonne pour appliquer un Deny ou un Allow sur chaque adresse IP.

> Le fichier à générer se nomme habituellement .htaccess mais pour simplifier son utilisation, nous allons le nommer htaccess.txt

## Fichier CSV

```
IP Address,Rule
192.168.1.10,Allow
172.100.2.11,Allow
1.1.1.1,Deny
```

## Opérations à réaliser

1. Remplissez manuellement le fichier ip-addresses.csv
2. Remplacez le tableau d'adresse IP par le chargement du fichier CSV
3. Testez le fichier htaccess.txt sur http://www.htaccesscheck.com/
4. Quand le script fonctionne, effectuez un commit avec le libellé "exercice 02 done" et un push

## Résultat attendu

Le fichier htaccess.txt doit contenir:

```
Order Allow,Deny
Allow from 192.168.1.10
Allow from 172.100.2.11
Deny from 1.1.1.1
Deny from all
```

## Acquis

* Lecture d'un fichier CSV
* Utilisation des conditions if/elif/else