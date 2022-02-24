# Survol des modules standards Python les plus utiles

- [Liste des modules pour Python3.8](https://docs.python.org/3.8/py-modindex.html)

## argparse

- https://docs.python.org/3.8/library/argparse.html#module-argparse

Vous avez déjà utilisé ce module dans l'exercice n°5.

## atexit

- https://docs.python.org/3.8/library/atexit.html#module-atexit

Ce module est très utile quand vous lancez un script en tâche de fond ou en mode serveur pour exécuter des tâches avant l'arrêt complet du programme.

Par exemple:
- Fermer une connection à une BDD
- Vérifier que tous les utilisateurs sont bien déconnectés
- Enregistrer des données de récupération pour le prochain démarrages

## base64

- https://docs.python.org/3.8/library/base64.html#module-base64

Permet de transformer des chaines en Base64 et inversement.

Il est très utile pour convertir un binaire (image, video, ...) en texte avant de le stocker dans une BDD.

## collections

- https://docs.python.org/3.8/library/collections.html#collections.OrderedDict

Ce module contient quelques fonctions avancés pour les structures Python.

Vous pouvez avoir besoin en particulier d'un OrderedDict pour conserver l'ordre d'insertion et d'affichage des clés dans un dict.

## concurrent.futures

- https://docs.python.org/3.8/library/concurrent.futures.html#module-concurrent.futures

Il s'agit de l'une des méthodes pour exécuter du code parallèle en Python3.

Son utilisation est assez simple mais un peu verbeuse.

## csv

- https://docs.python.org/3.8/library/csv.html#module-csv

Module que vous avez utilisé dans l'exercice n°2

## datetime

- https://docs.python.org/3.8/library/datetime.html#module-datetime

Manipulation de dates et heures.

## email

- https://docs.python.org/3.8/library/email.html#module-email

Manipulation d'emails pour l'envoi et la réception.

## hashlib

- https://docs.python.org/3.8/library/hashlib.html#module-hashlib

Module pour générer des Hash sur des chaines de caractère. Exemple: pour masquer un mot de passe ou définir une somme de contrôle.

## http.server

- https://docs.python.org/3.8/library/http.server.html#module-http.server

> Si vous exécutez cette exemple à partir de n'importe quel répertoire, vous disposerez d'un serveur http très basique non sécurisé.

```shell
python -m http.server 8000
```

## io

- https://docs.python.org/3.8/library/io.html#module-io

Module très utile pour manipuler des fichiers binaires ou textuels de grandes tailles.

## ipaddress

- https://docs.python.org/3.8/library/ipaddress.html#module-ipaddress

Module de manipulation de validation d'adresse IP

## json

- https://docs.python.org/3.8/library/json.html#module-json

Manipulation de données au format JSON

## logging

- https://docs.python.org/3.8/library/logging.html#module-logging

Module très complet pour la gestion des logs des applications Python.

## multiprocessing

- https://docs.python.org/3.8/library/multiprocessing.html#module-multiprocessing

Module pour l'exécution parallèle sur plusieurs processeurs.

## os

- https://docs.python.org/3.8/library/os.html#module-os

Beaucoup d'utilitaires comme `os.mkdir() ou os.makedirs()` pour créer un répertoire.

## os.path

- https://docs.python.org/3.8/library/os.path.html#module-os.path

## pathlib

- https://docs.python.org/3.8/library/pathlib.html#module-pathlib

## platform

- https://docs.python.org/3.8/library/platform.html#module-platform

Fournit des informations sur Python et la plateforme d'exécution où est il est exécuté

## pprint

- https://docs.python.org/3.8/library/pprint.html#module-pprint

Fonction pretty print pour obtenir un affichage plus lisible.

## random

- https://docs.python.org/3.8/library/random.html#module-random

Module de génération de données aléatoires.

## re

- https://docs.python.org/3.8/library/re.html#module-re

Module de gestion d'expressions régulières (Regex)

## shutil

- https://docs.python.org/3.8/library/shutil.html#module-shutil

Manipulation de fichiers et répertoires.

## smtplib

- https://docs.python.org/3.8/library/smtplib.html#module-smtplib

Client SMTP

## sqlite3

- https://docs.python.org/3.8/library/sqlite3.html#module-sqlite3

Base de données SQL light stocké localement dans un fichier.

## subprocess

- https://docs.python.org/3.8/library/subprocess.html#module-subprocess

Exécution de commandes système.

## sys

- https://docs.python.org/3.8/library/sys.html#module-sys

Plusieurs utilitaires dont la fonction `sys.exit()`.

## tarfile

- https://docs.python.org/3.8/library/tarfile.html#module-tarfile

Manipulation d'archives .tar

## tempfile

- https://docs.python.org/3.8/library/tempfile.html#module-tempfile

Gestion de répertoires et fichiers temporaires

## time

- https://docs.python.org/3.8/library/time.html#module-time

Module relatif au temps. A ne pas confondre avec le module datetime.

Parmis les utilisations:
- Faire une pause avec `time.sleep(10)`
- Obtenir un timestamp avec `time.time()`

## unittest

- https://docs.python.org/3.8/library/unittest.html#module-unittest

Module dédié à la conception de tests unitaires.

## uuid

- https://docs.python.org/3.8/library/uuid.html#module-uuid

Génération d'identifiant unique.

Exemple: 

```python
from uuid import uuid4
print(str(uuid4()))
"604d9b87-d01b-4c03-981d-d607a4d492ca"
```

## xml

- https://docs.python.org/3.8/library/xml.html#module-xml

Manipulation de flux XML.

Je vous conseille d'utiliser plutôt: https://lxml.de/

