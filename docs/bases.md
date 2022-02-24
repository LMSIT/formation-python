# Les bases du langage

## Python en ligne de commande

```shell
$ python3 -V
Python 3.8.2

$ python3 -c "print('Hello LBN')"
Hello LBN

$ python3 -m http.server -d .
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

## Le shell Python

```shell
$ python3
```

```python
"Hello LBN"
'Hello LBN'

exit()
```

## Shell avancé avec IPython

Il existe plusieurs shell Python permettant d'améliorer l'utilisation et le debug d'un code python.

Nous allons utiliser [IPython](https://ipython.org/) qui est l'un des plus connus.

```shell
pip install ipython

ipython
In [1]: 
```

A retenir sur IPython:
- **?** pour avoir de l'aide
- **hist** pour afficher l'historique des commandes écrites précédement
- L'affichage des variables est mise en forme pour plus de lisibilité
- IPython fournit de l'auto-complétion avec la touche **TAB**
- exit au lieu de exit() dans le shell standard

## Les types de base

```python
my_string = "mystring"
my_integer = 123
my_float = 1.2
my_bool = True
my_list = [1, -2, "a", "b"]
my_dict = {"key1": "value1", "key2": 2}
my_bytes = b"mybytes"
```

> Python, n'est pas un language *typé*, c'est à dire qu'il n'est pas nécessaire de déclarer le type de variable avant son utilisation.

## Variables & Constantes


```python
my_var = 10
my_var += 10
print(my_var)
20

MY_VAR = 10
# L'instruction suivante ne devrait pas fonctionner si c'était une vraie constante
MY_VAR += 10
print(MY_VAR)
20
```

En réalité, il n'existe pas de *constante* en Python mais par convention, elles sont déclarées en MAJUSCULE. Comme vous le voyez, le résultat est le même qu'avec une variable.

> Vous aurez remarqués que les noms de variables sont sensibles à la casse !

## Formatage des chaines

#### Les méthodes de concaténation

```python
last_name = "DURANT"
first_name = "Alain"

first_name + " " + last_name
'Alain DURANT'

"{} {}".format(first_name, last_name)
'Alain DURANT'

"%s %s" % (first_name, last_name)
'Alain DURANT'

"%(first_name)s %(last_name)s" % {"first_name": first_name, "last_name": last_name}
'Alain DURANT'
```

#### f-string

Les f-string sont la nouvelle méthode recommandée pour obtenir un code
plus lisible. [Documentation de f-string](https://docs.python.org/fr/3/tutorial/inputoutput.html#formatted-string-literals)

```python
f"{first_name} {last_name}"
'Alain DURANT'

full_name = f"{first_name} {last_name}"
full_name
'Alain DURANT'
```

#### Simple quote et Double quote

```python
f'{first_name} {last_name}'
'Alain DURANT'
```

#### Caractère d'échappement dans les chaînes

```python
f"\"{first_name} {last_name}\""
'"Alain DURANT"'
```

#### Triple quotes

```python
"""
Commentaires sur 
plusieurs 
ligne
"""

"""
# pour commenter du code
a = [1, 2, 3]
"""

first_name = "Alain"
last_name = "DURANT"
city = "Paris"

print(f"""First Name: {first_name}
Last Name: {last_name}
City: {city}
""")

```

## Manipulation de chaines

```python
# Transforme une chaine en tableau (séparateur espace par défaut)
"Un Deux Trois".split()
['Un', 'Deux', 'Trois']

# Même chose avec séparateur ","
"Un,Deux,Trois".split(",")
['Un', 'Deux', 'Trois']

# Supprime les caractères inutiles en début et fin de chaine
" Ma phrase ".strip()
'Ma phrase'
```

## Calcul avec les types numériques

```python
a = 1
a += 1
a
2

a -= 1
a
1

a = a + 1
a
2

multiplicator = 10
a * multiplicator
20

a
2
```

## Le type None

None est une valeur null. Vous pouvez l'utilisez par exemple, pour vérifier si un champs à bien été remplit dans un formulaire.

```python
a = None
a is None
True

a = "abcd"
a is None
False
```

## Le type Boolean

```python
a = True
a is True
True

b = False
b == a
False
```

## Les tableaux indexés (list/tuple)

Les tableaux sont très utilisés en Python et les exemples suivants sont les usages les plus fréquents.

### Le type list

```python
a = [1, 2, 3]
a.append(4)
a
[1, 2, 3, 4]

# Renvoi la position de la valeur 2
a.index(2)
1

# Elément à la position 1
a[1]
2

# Dernier éléments
a[-1]

len(a)
4

a.reverse()
a
[4, 3, 2, 1]

a.sort()
a
[1, 2, 3, 4]

a.pop()
4
a.pop()
3
a
[1, 2]

a.insert(0, 10)
a
[10, 1, 2, 3]

a = [1, 2, 3]
type(a)
<class 'list'>

# Transforme un tableau de chaines en une chaine
a = ["A", "l", "a", "i", "n"]
a
['A', 'l', 'a', 'i', 'n']
"".join(a)
'Alain'

# Transforme un mot ou une chaine en tableau
list("Alain")
['A', 'l', 'a', 'i', 'n']
```

### Le type tuple

Un tuple est identique à un type **list** à la différence qu'il se déclare avec () au lieu de [] et n'est pas modifiable

```python
a = (1, 2, 3)

# La méthode d'ajout d'un élément au tableau n'existe pas dans un tuple
a.append(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'

# Transformation d'un type list en tuple
a = [1, 2, 3]
tuple(a)
```

> Les tuples sont plus rapides et moins couteux en mémoire que les **list** mais ils ne répondent pas toujours à vos besoins.


## Le tableau associatif (dict)

```python
# Ces 2 méthodes sont identiques
a = {"key1": "value1", "key2": 2}
b = dict(key1="value1", key2=2)

a == b
True

a["key1"]
'value1'

# Génère une exception car la clé n'existe pas
a["key3"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key3'

# Renvoi None car la clé n'existe pas
a.get("key3")

# Renvoi une valeur par défaut quand la clé n'existe pas
a.get("key3", "default value key3")
'default value key3'

# Ajout de la clé key3
a["key3"] = "value3"

a["key3"]
'value3'

# Affiche la liste des clés disponible
list(a.keys())
['key1', 'key2', 'key3']

# Affiche la liste des clés/valeurs sous forme de tuple (key, value)
list(a.items() )
[('key1', 'value1'), ('key2', 2), ('key3', 'value3')]

# Enlève la key3 du dictionnaire et renvoi sa valeur
a.pop('key3')
'value3'
list(a.keys())
['key1', 'key2']

# Supprime la clé/valeur key2
del a["key2"]
list(a.keys())
['key1']
```

## Python et l’indentation

Jusqu'à maintenant, l'indentation du code n'était pas nécessaire car nous n'avons pas utilisé d'instruction sur plusieurs ligne comme les boucles, les conditions ou les fonctions.

Python est particulièrement dépendant de l'indentation pour exécuter son code.

L'indentation se définit par lot de 4 espaces.

**Exemple:**

```python
a = 1
b = 2
if a >= 1:
    print("OK")
    if b < 10:
        print("OK2")
```

## La boucle for

La boucle **for** parcours les éléments d'une liste et continue jusqu'à la fin de la liste.

```python
my_list = [3, 1, 10]

for i in my_list:
    print(i)
3
1
10

my_list = [1, 2, "a", "b"]

# Vous pouvez aussi le faire sur une ligne
for l in my_list: print(l)

# L'instruction break, permet de sortir d'une boucle avant la fin
for i in my_list:
...     if i == "a":
...         break
...     print(i)
```

## La boucle while

While permet de boucler tant que la condition est vrai.

```python
loop_condition = True
while loop_condition:
...    print("toujours là...")
...    loop_condition = False

while loop_condition:
...    print("toujours là...")
...    break # pour éviter une boucle sans fin

i = 1
while i < 5:
...    i += 1
...    print("toujours là...")
```


## Conditions if/elif/else

```python
age = 10

if age < 18:
    print("Vous êtes mineur !")


if age < 18:
    print('Vous avez %s ans et vous êtes mineur' % age)
elif age >= 18 and age < 65:
    print("Vous avez %s ans et vous payez beaucoup d'impôts" % age)
else:
    print('Vous avez %s ans et vous êtes à la retraite' % age)
```

## Les dates avec le module datetime

Les instructions et fonctions que nous avons utilisés jusqu'à maintenant étaient intégrés à Python [Built-in Functions](https://docs.python.org/3/library/functions.html)

Pour la manipulation de Date et d'Heure, il faut charger l'un des nombreux modules standards: [datetime](https://docs.python.org/fr/3/library/datetime.html)

Le chargement de module se fait toujours à l'aide de l'instruction **import**

```python
import datetime

datetime.date.today()
datetime.date(2020, 9, 23)

# Date/Heure actuelle avec la timezone courante du système
datetime.datetime.now()
datetime.datetime(2020, 9, 23, 11, 7, 43, 61958)

# Date/Heure actuelle en UTC
datetime.datetime.utcnow()
datetime.datetime(2020, 9, 23, 9, 7, 45, 655149)

now = datetime.datetime.now()

now.strftime("%Y/%m/%d")
'2020/09/23'

now.strftime("%Y/%m/%d %H:%M:%S")
'2020/09/23 11:08:28'
```

> Pour l'UTC, vous trouverez de nombreuses explications sur internet. ex: [Wikipedia](https://fr.wikipedia.org/wiki/Temps_universel_coordonn%C3%A9)


## Lecture et écriture dans un fichier

> Nous allons commencer par l'écriture dans un fichier afin d'avoir un exemple de fichier à lire...

```python
# Ouverture d'un fichier en écriture. Il sera créé si il n'existe pas
fp = open("my_file.txt", "w")
fp.write("abcdef")
fp.close()

# Syntaxe recommandée pour ne jamais oublier de fermer le fichier
with open("my_file.txt", "w") as fp:
    fp.write("abcdef")

# Lecture du fichier (ouverture en lecture seule "r")
with open("my_file.txt", "r") as fp:
    data = fp.read()
    print(data)
```

> Pour l'instant, nous n'avons écrit qu'un fichier **text** avec une seule ligne. Nous allons passer au multiligne.

```python
lines = ["un", "deux", "trois"]
with open("my_file.txt", "w") as fp:
    for line in lines:
        fp.write(line)

with open("my_file.txt", "r") as fp:
    data = fp.read()
    print(data)
```

Comme vous le voyez à l'écran ou en ouvrant le fichier, il y a un problème, car vous ne trouvez qu'une ligne: "undeuxtrois"

La fonction write(), écrit le texte, tel qu'il est fournis. Il faut donc ajouter un retour à la ligne (line feed) avec le caractère "\n"

```python
lines = ["un", "deux", "trois"]
with open("my_file.txt", "w") as fp:
    for line in lines:
        fp.write(f"{line}\n")
```

Maintenant, dans le fichier, vous devriez trouver le résultat suivant:

```
un
deux
trois
```

## Passage du shell au script Python

Un script Python s'écrit par convention dans un fichier avec l'extension .py même si ce n'est pas obligatoire.

Créez un fichier **my-first-script.py** avec le contenu suivant:

```python
import datetime

now = datetime.datetime.now()
print(f"heure courante : {now}")

with open("my_file.txt", "r") as fp:
    lines = fp.readlines()
    for i, line in enumerate(lines):
        print(f"{i} : {line}")
```

Exécutez le script:

```shell
python my-first-script.py
```

Vous pouvez constater que tout ce que nous avons fait dans le shell Python jusqu'à maintenant, peut être fait de la même façon dans un script.

**Quelques remarques:**

- L'affichage à l'écran se fait toujours avec la fonction print()
- Le code Python s'exécute en partant de la première ligne à la dernière ligne
- Les instructions **import** sont toujours en haut du fichier (sauf cas particuliers)

Essayez d'exécuter directement le script:

```shell
./my-first-script.py

# Selon votre environnement, vous aurez une erreur:
-bash: ./my-first-script.py: Permission denied
```
Il y a deux choses à faire pour rendre exécutable le script:

**La première:**

```shell
chmod +x /my-first-script.py
```

**La seconde:** est d'ajouter `#!/usr/bin/env python` en première ligne du script
