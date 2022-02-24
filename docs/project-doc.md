# Documenter un projet Python avec Markdown

[Markdown](https://fr.wikipedia.org/wiki/Markdown) est l'un des formats les plus simples et les plus courants pour créer de la documentation.

Ce support de cours est lui même écrit en Markdown et des librairies Javascript comme [revealjs](https://revealjs.com/) et [docsify](https://docsify.js.org/#/) permettent de le transformer dynamiquement en slides ou en pages HTML.

Que ce soit sur GitLab ou Github, la page d'accueil d'un projet, provient toujours d'un fichier README.md.

**Quelques exemples les plus courants:**

```markdown
# Titre 1
## Titre 1.1
### Titre 1.1.1

**Texte en gras:**

*Texte en italique:*

- Liste el1
- Liste el2
- Liste el3

\```python
print("ma fonction python")
\```

[Un lien externe](http://localhost)
```

**Structure d'un fichier README.md:**

```markdown
# Titre du projet

Texte explicatif (en anglais si possible)

## Requires

- Python version : 3.5+
- Linux Ubuntu 18.04+

## Installation

\```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
\```

## Usage

\```shell
python my_module.py --help
\```

## TODO

- Feature 1.1
```
