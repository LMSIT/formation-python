# Production de service web avec le framework flask

## Les services WEB

**Il existe plusieurs façon d'exposer des services:**

- [HTTP Rest](https://fr.wikipedia.org/wiki/Representational_state_transfer)
    - Le plus courant
    - Utilise les mêmes verbes HTTP que votre navigateur
    - Le plus facile à utiliser
    - Moins performant pour des requêtes multiples
- [GraphQL](https://fr.wikipedia.org/wiki/GraphQL)
    - Alternative à REST créé par Facebook en 2012
    - Permet d'interroger plusieurs source en une seule requêtes
    - Fournit un Meta Langage pour les requêtes
- [GRPC](https://www.grpc.io/)
    - Alternative à REST créés par Google en 2015
    - Peut s'utiliser dans beaucoup de langage
    - Très performant

Les points communs de ces technologies est qu'elles s'appuient toutes sur le protocole HTTP et sont donc plus simple à sécuriser, à mettre en cache, à scaler.

## Les Frameworks Python WEB pour HTTP

Il existe de nombreux framework en Python pour développer une application Web ou produire des API.

J'a choisi [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) car il est très simple et rapide à mettre en oeuvre.

Parmis les autres solutions:
- [Django](https://www.djangoproject.com/):
    - Le plus populaire et le plus complet
    - A utiliser, en particulier si vos données sont dans une BDD SQL
- [Bottle](https://bottlepy.org/) : Tout le framework tiens dans un fichier que vous pouvez embarquer dans votre code
- [Starlette](https://www.starlette.io/)
- [FastApi](https://fastapi.tiangolo.com/)

Il existe 2 spécifications pour les framework Web Python:
- [WSGI](https://wsgi.readthedocs.io/)
    - Frameworks: Django, Flask, Bootle
    - Implémentation de référence: https://docs.python.org/3.8/library/wsgiref.html
- [ASGI](https://asgi.readthedocs.io/)
    - Frameworks: Starlette, FastAPI, Django Channels
    - Performances proche du GoLang

## Exemple basique de service Web avec Flask

```shell
pip install flask
```

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/v1/ip', methods=('GET'))
def ip_list():
    return jsonify([
        "1.1.1.1",
        "192.168.1.2"
    ])
```

```shell
FLASK_APP=myapp.py flask run -p 8181
```

**Lancez un shell Python dans une autre fenêtre:**

```python
import requests

response = requests.get('http://127.0.0.1:8181/api/v1/ip')

print(response.status_code)
200

print(response.json())
['1.1.1.1', '192.168.1.2']
```

## Ce qu'il reste à apprendre pour produire des services Web

- Exposer des services avec les méthodes/verbes POST, PUT, PATCH, DELETE
- Utiliser les arguments dans l'url: `?field=value&other_field=value`
- Utiliser les paramètres dans la route: `/api/v1/ip/<int:id>`
- Gérer l'authentification et sécuriser les routes
- Générer un [swagger](https://petstore.swagger.io/) automatiquement. Par exemple pour flask:
    - https://github.com/flasgger/flasgger
    - https://github.com/noirbizarre/flask-restplus
- Versionner l'api
- Structurer le code quand il devient volumineux
- Créer des tests unitaires
- Automatiser le déploiement
- Ajouter du cache

