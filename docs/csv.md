# Lecture d'un fichier CSV

## Introduction au format CSV

**La base commune à tous les fichiers CSV:**
- La 1ère ligne contient les titres (optionnel)
- 1 ligne par enregistrement (équivalent à 1 ligne d'un tableur)
- 1 séparateur de colonne

**Ce qui peut varier d'un fichier CSV à l'autre**
- Le séparateur entre chaque champs: virgule, point virgule, tabulation, autres...
- Les caractères pour encadrer chaque champs: rien, simple quote, double quote
- Le(s) caractère(s) de fin de ligne: LF ou CRLF

Exemple de fichier simple avec séparateur virgule et des champs sans encadrement:

```csv
firstname,lastname,city
Alain,Durant,Paris
Jean,DUPONT,Nantes
```

Ce qui va justifier d'un autre séparateur que la virgule est que si l'une des colonnes (champs) contient également une virgule, on ne pourra pas faire la différence entre le séparateur et le texte.

**Un exemple plus prudent** avec encadrement par des double quote et un séparateur point virgule:

```csv
"firstname";"lastname";"city"
"Alain";"Durant";"Paris"
"Jean";"DUPONT";"Nantes"
```

## Le module CSV de Python

Python fournit en standard un module pour lire et écrire le format CSV. [Documentation](https://docs.python.org/fr/3/library/csv.html)

Chaque ligne d'un fichier CSV peut être renvoyé sous forme de tableau (csv.reader) ou de dictionnaire (csv.DictReader).

## Lecture avec un tableau par ligne

```python
import csv

with open('fichier.csv') as fp:
    reader = csv.reader(fp, delimiter=';', quotechar='"')
    for row in reader:
        print(row[0], row[1], row[2])
```

## Lecture avec un dictionnaire par ligne

```python
import csv
with open('fichier.csv') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        print(row['firstname'], row['lastname'], row['city'])
```
