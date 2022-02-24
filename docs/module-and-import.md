# Les modules python et la function import

Un module est un simple fichier avec l'extension .py, contenant du code réutilisable.

Exemple avec le module [ipaddress](https://docs.python.org/fr/3.7/library/ipaddress.html#convenience-factory-functions) que nous avons utilisé récement:

```python
# https://github.com/python/cpython/blob/3.7/Lib/ipaddress.py#L27
def ip_address(address):
    ...
```

Quand vous utilisez l'**import** suivant dans votre script: `from ipaddress import ip_address`, celà revient à copier tout le contenu de la fonction **ip_address()** dans votre script.

**Essayez vous même avec l'exemple suivant:**

```python
# my_functions.py

def get_fullname(first_name, last_name):
    return f"{first_name} {last_name}"

# script.py

from my_functions import get_fullname
fullname = get_fullname("Alain", "Durant")
print(fullname)
```

**Quelques règles dans l'écriture de fonctions:**
- Le nom du fichier contenant des fonctions à importer ne doit pas contenir de "-" ni d'accent ou de caractères spéciaux.
- La totalité du code de ce module sera chargé, même si vous n'importer qu'une seule fonction alors éviter de mettre des actions à l'extérieur de fonctions.
- Le module à importer doit être dans le chemin de recherche Python. Voir ci-après:

Visualisez le chemin de recherche avec la ligne de commande suivante:

```shell
python -c "import sys; print(sys.path)"
```

Vous pouvez modifier le chemin de recherche avec la variable PYTHONPATH:

```shell
PYTHONPATH=/tmp python -c "import sys; print(sys.path)"
```

> **Remarque:** Par défaut, Python recherche d'abord dans le répertoire courant pour charger un module. 