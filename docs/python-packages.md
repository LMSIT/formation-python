# La notion de Package en Python

A chaque fois que vous utilisez l'instruction **import** dans du code Python, il a de grandes chances pour que le module que vous chargez, proviennent d'un package.

Par exemple, `import requests`, va charger les données à partir du package `.venv/lib/python3.8/site-packages/requests/`.

Un package python est définit par:
- Un répertoire
- Un fichier `__init__.py`
- D'autres fichiers .py facultatif

Donc, pour reprendre l'exemple de **requests**, quand vous faites un `import requests`, Python va charger le module `.venv/lib/python3.8/site-packages/requests/__init__.py` qui contient lui même, d'autres imports, internes et externes.

**Les deux imports suivants sont identiques:**

```python
from requests import Session
from requests.sessions import Session
```

**Le premier import, va charger le module __init__.py, qui contient un import du module sessions:**

```python
# https://github.com/psf/requests/blob/master/requests/__init__.py#L124
from .sessions import session, Session
```

**Le second import, va charger directement la classe Session dans son propre module sessions.py**

```python
# https://github.com/psf/requests/blob/master/requests/sessions.py#L337
class Session(SessionRedirectMixin):
    ...
```

> Vous aurez peut remarqué que le premier import, va charger le module sessions.py avec un chemin relatif et c'est encore une particularité des packages Python.

**Conclusions:**

Il faudrait quelques heures de plus pour approfondir le sujet et vous avez peu de chances d'avoir besoin de gérer des packages pour le moment.

> **A retenir:** Un package peut être utile, à partir du moment où votre projet contient au moins 2 modules Python.

**Quelques liens pour approfondir le sujet:**

- https://python-guide-fr.readthedocs.io/fr/latest/writing/structure.html#packages
- https://packaging.python.org/tutorials/packaging-projects/





