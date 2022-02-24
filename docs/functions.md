# Les fonctions en Python

**Rappel:**
- Un module python est un fichier unique contenant du code python. Ce n'est pas obligatoire mais par convention, les fichiers Python on l'extension .py.
- Le code dans un module Python est interprété de la 1ère ligne à la dernière ligne
- L'importation d'un module dans un autre, suit les mêmes règles d'interprétation du code
- Les fonctions présentes dans un module ne sont exécutés que si elles sont appellés explicitement.

**Les fonctions permettent:**
- De mieux découper le code
- Une meilleure réutilisation
- Une plus grande lisibilité

**Exemple de code sans fonction:**

```python
first_name = "Alain"
last_name = "Durant"
print(f"{first_name} {last_name}")
```

**Avec fonction:**

```python
def merge_name(first_name, last_name):
    return f"{first_name} {last_name}"

full_name = merge_name("Alain", "Durant")
print(full_name)
```

> Le résultat est le même dans les 2 cas, mais celui avec fonction est **lisible** et **réutilisable**. 

## Les paramètres d'une fonction

Une fonction peut recevoir 2 types de paramètres:
- Un paramètre obligatoire
- Un paramètre facultatif avec une valeur par défaut

```python
# first_name et last_name sont obligatoire et doivent être fournis dans l'ordre
def merge_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(merge_name("Alain", "Durant"))

# Inverser les paramètres fonctionnera mais le résultat sera faux
print(merge_name("Durant", "Alain"))

def merge_name(first_name=None, last_name=None):
    return f"{first_name} {last_name}"

print(merge_name(first_name="Alain", last_name="Durant"))

# Cette fois, quelque soit l'ordre, la fonction saura distinguer chaque paramètre
print(merge_name(last_name="Durant", first_name="Alain"))

# Cette forme continuera de fonctionner et les variables sont affectés dans l'ordre
print(merge_name("Alain", "Durant"))
```

## Les paramètres spéciaux *args et **kwargs

```python
# la fonction recevra une nombre illimité de paramètres sous forme de tableau
def merge_name(*args):
    first_name = args[0]
    last_name = args[1]
    return f"{first_name} {last_name}"

print(merge_name("Alain", "Durant"))

# Le 3ème argument sera ignoré par la fonction
print(merge_name("Alain", "Durant", "Paris"))

# la foncion recevra un dictionnaire
def merge_name(**kwargs):
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{first_name} {last_name}"

print(merge_name(last_name="Durant", first_name="Alain"))

# Ceci renverra une erreur
print(merge_name("Alain", "Durant"))

# Le champs city sera ignoré
print(merge_name(last_name="Durant", first_name="Alain", city="Paris"))
```

## La valeur de retour d'une fonction

Par défaut, sans instruction spécifique, une fonction renvoi toujours **None**

```python
# Renvoi None
def my_function():
    print("test...")

# Renvoi un str avec la valeur "end"
def my_function():
    print("test...")
    return "end"

def my_function():
    print("test...")
    return 0, "test", {"key": "value"}

var1, var2, var3 = my_function()    

def my_function():
    print("test...")
    return {"key": "value", "": ""}

var_dict = my_function()
print(var_dict)
```

## Les annotations

Depuis la version 3.5 de Python (à vérifier), vous disposez d'une nouvelle façon de déclarer les paramètres d'une fonction et son type de retour.

```python
# Les paramètres sont requis, leur type déclaré et le type de retour est précisé
def merge_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"

print(merge_name("Alain", "Durant"))

# Paramètres facultatifs:
def merge_name(first_name: str=None, last_name: str=None) -> str:
    return f"{first_name} {last_name}"

print(merge_name(first_name="Alain", last_name="Durant"))
```

Les annotations ne sont pas contraignantes pour le moment car si vous passez un **int** à la place d'un **str**, vous n'aurez pas d'erreur à l'exécution.

Les éditeurs modernes de code comme VSCode utilisent les annotations pour signaler des erreurs et d'autres outils peuvent également valider si les types de valeurs fournis à vos fonctions corresponde à ce qui est attendu.


## La pseudo fonction main

**Placez ce code dans un module function1.py**

```python
print(__file__)
print(__name__)

if __name__ == "__main__":
    print("Main function")
```

**Exécutez le module:**

```shell
$ python3 function1.py
archives/tmp1.py
__main__
```

La variable `__file__`, renvoi toujours un String avec le chemin relatif du module

La variable `__name__`, renvoi une valeur qui peut changer selon la méthode d'exécution et de packaging (que nous verrons plus tard). Pour l'instant gardez à l'esprit que pour un script exécutable, il faudra toujours utiliser les 2 dernières lignes pour exécuter du code.

