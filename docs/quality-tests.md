# Introduction aux tests qualités

Les tests de qualité, permettent de vérifier:
- Le respect des bonnes pratiques (nommage, taille des ligne, espaces entre les fonctions, ...)
- Le taux de couverture des tests

Il existe un grand nombre d'outils en ligne de commande ou sous forme de service SAAS.

**Quelques outils en ligne de commande:**

- [pycodestyle](https://pycodestyle.pycqa.org/)
- [flake8](https://gitlab.com/pycqa/flake8)
- [pylint](https://www.pylint.org/)
- [black](https://black.readthedocs.io/)

Cette [documentation](https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html) en décrit quelques uns et fournit des exemples.

**Quelques services SAAS:**

- [coverall](https://coveralls.io/)
    - Se concentre surtout sur la couverture des tests
- [sonarcloud](https://sonarcloud.io/)
    - Fournit également des tests de vulnérabilités

**Essai de pycodestyle sur notre générateur de fichier .htaccess:**

```shell
pip install pycodestyle

pycodestyle generate_htaccess.py

generate_htaccess.py:22:1: W293 blank line contains whitespace
generate_htaccess.py:34:1: W293 blank line contains whitespace
generate_htaccess.py:40:1: W293 blank line contains whitespace
generate_htaccess.py:48:1: W293 blank line contains whitespace
generate_htaccess.py:57:1: W293 blank line contains whitespace
generate_htaccess.py:62:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:64:1: W293 blank line contains whitespace
generate_htaccess.py:77:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:79:1: W293 blank line contains whitespace
generate_htaccess.py:89:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:90:1: W293 blank line contains whitespace
generate_htaccess.py:115:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:125:80: E501 line too long (98 > 79 characters)
generate_htaccess.py:127:80: E501 line too long (97 > 79 characters)
generate_htaccess.py:132:1: W293 blank line contains whitespace
generate_htaccess.py:138:1: W293 blank line contains whitespace
generate_htaccess.py:143:1: E305 expected 2 blank lines after class or function definition, found 1

# En ignorant les erreurs W293 et E501
pycodestyle --ignore=W293,E501 generate_htaccess.py

generate_htaccess.py:62:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:77:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:89:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:115:1: E302 expected 2 blank lines, found 1
generate_htaccess.py:143:1: E305 expected 2 blank lines after class or function definition, found 1
```

Ces erreurs ne sont pas trop grave et vous pouvez soit les corriger manuellement, soit faire appel à **black** pour qu'il s'en charge:

```shell
pip install black

# Pour afficher les modifications sans modifier le script:
black --diff generate_htaccess.py

# Pour appliquer les modifications:
black generate_htaccess.py
```