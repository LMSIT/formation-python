# Le déploiement d’un projet Python avec setup.py

Ces dernières années, ont émergés de nombreux framework pour déployer une application Python et gérer ses dépendances:

- [setuptools](https://packaging.python.org/tutorials/packaging-projects/)
    - La plus ancienne et la plus utilisé
    - Installe votre application avec `pip install .`
- [pipenv](https://pipenv.pypa.io/)
    - Même auteur que la librairie **requests**
    - Utilise un fichier **Pipfile** (un peu comme le packages.json de Node.JS)
- [poetry](https://github.com/python-poetry/poetry)
    - Très populaire ces dernières années
    - Utilise un fichier au format [toml](https://toml.io/en/)

Nous allons parler ici de setuptools et de la fabrication d'un fichier setup.py car c'est une méthode qui est encore d'actualité et qui fonctionne très bien.

**setuptools** est également la seule manière de publier des applications sur le dépôts mondial des applications Python : [pypi](https://pypi.org/).

**Votre script à installer:**

```python
#!/usr/bin/env python

# hello-world.py
print("hello world !")
```

**Le fichier setup.py:**

```python
from setuptools import setup

setup(
    name='mypackage-name',
    version="0.1.0",
    description="Hello world de formation",
    scripts=[
        "hello-world.py"
    ],
    install_requires=[
        "flask",
        "requests==2.24.0"
    ],
    author='Stephane RAULT',
    author_email="s.rault@linkbynet.com",
    python_requires='>=3.7',
)
```

```shell
# Installez l'application
pip install .

# Exécutez le script avec la syntaxe suivante
hello-world.py

# Vérifiez où se trouve le script qui vient d'être exécuté
type hello-world.py
hello-world.py is hashed (~/code/lbn/supports/python-initiation/.venv/bin/hello-world.py)

# Vérifiez dans la liste des packages installés
pip freeze | grep mypackage

# Désinstallez l'application
pip uninstall mypackage-name

# Installez à l'ancienne (sans pip)
python setup.py install
```

**Plusieurs remarques:**
- Vous n'avez pas eu besoin de rendre le fichier exécutable avec chmod
- Vous pourriez supprimer le fichier hello-world.py et setup.py mais la commande hello-world.py fonctionnerait encore car elle est installé dans les packages python locaux
- Si vous utilisez `pip freeze`, vous constaterez que les dépendances (requests et flask) ont bien été installés (ainsi que beaucoup d'autres packages dont ils dépendent eux mêmes)
