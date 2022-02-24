# Lecture/Ecriture de fichier YAML (Yet Another Markup Language)

Le YAML se retrouve un peu partout depuis quelques années. Je l'ai vu arriver avec le framework [php Symfony](https://symfony.com/) et je le retrouve maintenant dans les définitions [Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) ainsi que dans la configuration de plusieurs solutions de CI/CD comme GitLab-CI.

Son avantage, par rapport à JSON est qu'il est :
- Beaucoup plus lisible
- Moins contraignant (problèmes de virgule dans JSON)
- Il évite les problèmes de sérialisation/désérialisation rencontrés avec JSON
- Il peut être dynamique car il est possible de faire des références entre plusieurs entrées

L'inconvénient est qu'il faut installer une librairie spécifique pour le lire et l'écrire, contrairement à JSON qui est inclus avec la plupart des langages.

La documentation de la librairie PyYAML se trouve [ici](https://pyyaml.org/wiki/PyYAMLDocumentation)

## Exemple de sérialisation

```python
from datetime import datetime

import yaml

MY_DICT = {
    'actif': True,
    'address': {
        'city': 'Paris', 
        'zipcode': 75010
    },
    'age': 20,
    'birthday': datetime.now(),
    'first_name': 'Alain',
    'last_name': 'DURANT',
    'tags': ['manager', 'rh']
}

print(yaml.dump(MY_DICT))
```

> Comme vous pouvez le constater, il n'y a pas eu besoin d'ajouter une fonction spéciale pour la conversion du datetime.

**Résultat:**

```yaml
actif: true
address:
  city: Paris
  zipcode: 75010
age: 20
birthday: 2020-10-14 10:53:50.123215
first_name: Alain
last_name: DURANT
tags:
- manager
- rh
```

## Exemple de désérialisation

```python
from io import StringIO
from pprint import pprint

import yaml

YAML_STR = """
actif: true
address:
  city: Paris
  zipcode: 75010
age: 20
birthday: 2020-10-14 10:53:50.123215
first_name: Alain
last_name: DURANT
tags:
- manager
- rh
"""

fp = io.StringIO(YAML_STR)
YAML_DICT = yaml.load(fp)
pprint(YAML_DICT)
```

**Résultat:**

> Encore une fois, comme pour la sérialisation, vous constaterez qu'il n'y a rien à faire de particulier pour transformer un str en datetime.

```python
{'actif': True,
 'address': {'city': 'Paris', 'zipcode': 75010},
 'age': 20,
 'birthday': datetime.datetime(2020, 10, 14, 10, 53, 50, 123215),
 'first_name': 'Alain',
 'last_name': 'DURANT',
 'tags': ['manager', 'rh']}
```

