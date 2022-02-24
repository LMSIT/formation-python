# Lecture/Ecriture de fichier JSON

JSON (JavaScript Object Notation) est un format très utilisé dans l'informatique.

Même si ce format a été créé initialement pour Javascript, tous les langages de développement disposent d'au moins une librairie pour lire et écrire du JSON.

Dans Python, le [module JSON](https://docs.python.org/fr/3/library/json.html) est intégré à la distribution standard.

**Exemple de fichier json:**

```json
{
    "first_name": "Alain",
    "last_name": "DURANT",
    "age": 20,
    "actif": true,
    "birthday": "10/10/2000",
    "tags": ["manager", "rh"],
    "address": {
        "city": "Paris",
        "zipcode": 75010
    }
}
```

**Même chose mais dans un tableau:**

```json
[
    {"username": "User1", "id": 1},
    {"username": "User2", "id": 2},
    {"username": "User3", "id": 3},
]
```

Comme vous pouvez le voir, à part le type boolean qui s'écrit **true** en minuscule au lieu de **True** en majuscule, le JSON est très proche d'un dictionnaire Python.

**Transformer un texte JSON en dict:**

```python
import json

TXT = """
{
    "first_name": "Alain",
    "last_name": "DURANT",
    "age": 20,
    "actif": true,
    "birthday": "10/10/2000",
    "tags": ["manager", "rh"],
    "address": {
        "city": "Paris",
        "zipcode": 75010
    }
}
"""

print(json.loads(TXT))
```

*Vous devriez avoir le résultat suivant (sauf l'ordre des champs):*

```python
{'first_name': 'Alain', 'last_name': 'DURANT', 'age': 20, 'actif': True, 'birthday': '10/10/2000', 'tags': ['manager', 'rh'], 'address': {'city': 'Paris', 'zipcode': 75010}}
```

**Ecrire un fichier JSON:**

```python
import json

MY_DICT = {
    'actif': True,
    'address': {
        'city': 'Paris', 
        'zipcode': 75010
    },
    'age': 20,
    'birthday': '10/10/2000',
    'first_name': 'Alain',
    'last_name': 'DURANT',
    'tags': ['manager', 'rh']
}


with open("file.json", "w") as fp:
    json.dump(MY_DICT, fp, indent=4)

pprint(txt)
```

> Pour une meilleure lisibilité, vous pouvez utiliser le module [pprint](https://docs.python.org/fr/3/library/pprint.html)


**Lire un fichier JSON:**

```python
import json
from pprint import pprint

with open("file.json") as fp:
    txt = json.load(fp)

pprint(txt)
```

*Vous devriez avoir le résultat suivant (sauf l'ordre des champs):*

```python
{'actif': True,
 'address': {'city': 'Paris', 'zipcode': 75010},
 'age': 20,
 'birthday': '10/10/2000',
 'first_name': 'Alain',
 'last_name': 'DURANT',
 'tags': ['manager', 'rh']}
```

**Remarques:**
- La différence entre json.load() et json.loads() est que load() attend un objet de type File et loads() attend un objet de type str (même chose pour dump/dumps)
- Les types complexes comme le **datetime** doivent faire l'objet de déclarations supplémentaires comme nous le verrons ci-après.

## Sérialiser / Désérialiser un type datetime

Si vous essayez de convertir un datetime en JSON (sérialisation) vous aurez l'erreur `TypeError: Object of type datetime is not JSON serializable` comme dans l'exemple suivant:

```python
from datetime import datetime
import json

print(json.dumps(datetime.now()))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type datetime is not JSON serializable
```

**Plusieurs solutions possibles:**

```python
from datetime import datetime
import json

# datetime.now() renvoi un type datetime qui est un objet complexe
print(datetime.now())
datetime.datetime(2020, 10, 14, 9, 59, 42, 285907)

# Avec la méthode isoformat(), la date est renvoyé en str et donc sérialisable
print(datetime.now().isoformat())
'2020-10-14T09:59:50.372442'

# Avec une librairie externe:
# pip install arrow

import arrow
now = datetime.now()
print(arrow.get(now).for_json())
'2020-10-14T10:06:52.681582+00:00'
```

Le problème des méthodes précédentes est qu'il faut savoir à l'avance, où se trouve un champs datetime pour le transformer manuellement avant de le sérialiser.

La bonne méthode consiste à fournir une fonction à json.dumps() pour qu'il s'en charge automatiquement.

```python
import json
import datetime

employee = {
    "id": 456,
    "name": "William Smith",
    "saley": 8000,
    "joindate": datetime.datetime.now()
}

def my_serialize_function(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

# Nous passons la fonction my_serialize_function() à json.dumps() 
print(json.dumps(employee, default=my_serialize_function))
```

Nous venons de voir la sérialisation avec json.dumps(), c'est à dire transformer un type Python en JSON. Nous allons maintenant voir la désérialisation avec json.loads() qui transforme du JSON en Python.

> Pour faire le chemin inverse, c'est à dire, transformer le texte en datetime, c'est un peu plus compliqué et long à documenter.

Vous avez [ici](http://sametmax.com/faire-manger-du-datetime-a-json-en-python/) un très bon exemple à mettre dans vos bookmarks.


