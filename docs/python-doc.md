# Documenter du code Python

Dans tous les languages, documenter du code a pour objectif:
- De fournir des informations sur la façon dont une fonction ou un module doit être utilisé
- De permettre à d'autres développeurs ou à vous même de le faire évoluer

Et dans Python en particulier:
- De produire un résultat utilisable avec la fonction help(nom_de_votre_fonction)
- De générer de la documentation automatique

En Python, la syntaxe pour documenter du code se nomme [docstring](http://sametmax.com/les-docstrings/) et s'écrit au format [RST](https://fr.wikipedia.org/wiki/ReStructuredText)

Exemple de documentation généré partiellement à partir des docstrings:
- https://arrow.readthedocs.io/en/stable/#module-arrow.arrow
- https://raw.githubusercontent.com/arrow-py/arrow/master/docs/index.rst
- https://github.com/arrow-py/arrow/blob/master/arrow/arrow.py#L32

> Au minimum, essayez de documentez ce que fait une fonction et dans la mesure du possible, documentez également les paramètres. Quelques commentaires dans les passages complexes seront également les bienvenues.

**Les docstring standards:**

- La documentation se place dès la première ligne de la fonction
- Elle est encadré par des triples quotes
- Chaque paramètre est décrit sur 2 lignes: son utilisation et son type
- return et rtype décrivent ce que renvoi la fonction et quel type Python est renvoyé

```python
def my_function(param1):
    """Small function for Python learning.
    
    :param param1: CSV File Name
    :type param1: str
    :return: A Array of param for example
    :rtype: list
    """

    return [param1]
```

**Le Google style:**

- https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
- https://google.github.io/styleguide/pyguide.html

> Comme vous le voyez avec l'exemple suivant, ce style demande moins de travail et il est plus lisible.

```python
def my_function(param1):
    """Small function for Python learning.
    
    Args:
        param1 (str): CSV File Name
    
    Returns:
        list: A Array of param for example
    """

    return [param1]
```



