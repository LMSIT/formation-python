# Consommation de service Web avec la librairie requests

La librairie requests est devenu une référence dans le monde Python.

Elle est utilisé par exemple dans des outils comme:
- az cli (le client Azure en ligne de commande)
- boto3 (le client AWS)
- La librairie [docker-py](https://github.com/docker/docker-py)

Pour vous entraînez à consommer des services web, nous utiliserons le service [jsonplaceholder](https://jsonplaceholder.typicode.com) qui a été créé à cet usage.

**Installez la librairie requests:**

```shell
pip install requests
```

**Essayez le script suivant:**

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

# Code HTTP https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
# 2XX, 3XX : normal
# 4XX, 5XX : erreur. Exemple avec les erreurs 404 ou 500.
print(response.status_code)

# Réponse au format Brut
print(response.text)

# Réponse au format Json
print(response.json())

for user in response.json():
    print(user["address"]["city"], user["id"], user["username"])
```

Si vous ouvrez l'adresse https://jsonplaceholder.typicode.com/users dans votre navigateur, vous constaterez que ce que vous avez récupéré, est une liste d'objets au format JSON.

**Pour rappel:** le protocole [HTTP](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol#M%C3%A9thodes) utilise des méthodes dont la plus connue est **GET**. C'est celui que vous utilisez par défaut, à chaque fois que vous ouvrez un site ou une page sur internet

**Les autres méthodes (verbes) sont:**
- POST (pour créer un objet, en général dans un formulaire)
- PUT (pour modifier un objet existant par remplacement complet)
- PATCH (pour modifier un objet existant par remplacement partiel)
- HEAD (ne fait rien mais est souvent utilisé pour vérifier l'accès à une page ou sa date de dernière modification)
- DELETE (pour supprimer un objet)

**Création d'un objet avec POST:**

```
import requests

new_post = {
    "title": "Formation Python",
    "body": "Création d'un objet avec POST...",
    "userId": 1,
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

print(response.status_code)
201

print(response.json())
{'title': 'Formation Python', 'body': "Création d'un objet avec POST...", 'userId': 1, 'id': 101}
```

Tous les exemples se trouvent [ici](https://jsonplaceholder.typicode.com/guide/). Ils sont écrit en Javascript mais vous devriez pouvoir les transformer en Python.

