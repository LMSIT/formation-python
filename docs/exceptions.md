# Gestion des erreurs en Python

1. Dans le répertoire du générateur htaccess, renommez le fichier ip-addresses.csv en backup-ip-addresses.csv

2. Lancez le script generate-htaccess.py. Vous devriez avoir l'erreur suivante

```python
Traceback (most recent call last):
  File "generate-htaccess.py", line 9, in <module>
    with open('ip-addresses.csv') as fp:
FileNotFoundError: [Errno 2] No such file or directory: 'ip-addresses.csv'
```

L'erreur FileNotFoundError s'appelle une Exception en Python. Vous remarquerez que la partie du code qui a déclenchée cette erreur, se trouve en ligne 9.

Les **exceptions** standards de Python sont documentés ici: https://docs.python.org/fr/3.5/library/exceptions.html

On dit qu'une exception est **levée** et nous allons apprendre à la **capturer**

Encadrez votre code dans un bloc try/catch et ajoutez la fonction sys.exit():

```python
import sys

try:
    with open('ip-addresses.csv') as fp:
        reader = csv.DictReader(fp)
    ...
except Exception as err:
    print(f"htaccess error : {str(err)}")
    sys.exit(1)
```

Relancez le script et vous devriez maintenant avoir la sortie suivante:

```
htaccess error : [Errno 2] No such file or directory: 'ip-addresses.csv'
```

Affichez le code d'erreur renvoyé par le script:

```
echo $?
1
```

Vous pouvez mettre n'importe quelle valeur autre que zéro pour dire que votre programme s'est interrompu sur une erreur.

Dans le cas de notre script, il y avait une façon plus simple de gérer cette erreur particulière:

```python
import sys
import os

CSV_FILENAME = 'ip-addresses.csv'

if not os.path.exists(CSV_FILENAME):
    print(f"No such file {CSV_FILENAME}")
    sys.exit(1)  

with open(CSV_FILENAME) as fp:
    reader = csv.DictReader(fp)
    ...
```

> Au passage, vous noterez l'utilisation d'une constante pour stocker le nom de fichier.