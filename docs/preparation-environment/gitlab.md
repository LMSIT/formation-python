# Préparation de l'environnement Gitlab

## Votre espace personnel sur Gitlab

Vous avez tous un espace personnel sur le Gitlab LBN.

L'adresse pour y accéder est https://gitlab.com/PARTIE_GAUCHE_DE_L_EMAIL.

**Exemple:**

- Mon email est rodolphemazamda@gmail.com
- La partie gauche (ou local) est s.rault
- Mon espace personnel est donc: https://gitlab.com/rodolphemazamda

Dans cet espace, il est possible de suivre et mesurer l'activité d'un utilisateur.

> Vous pouvez également accéder à votre espace en utilisant le menu utilisateur en haut à droite, menu **Profile**

## Création d'un token d'authentification

Pour gérer des dépôts sur le GitLab LBN, il est obligatoire d'utiliser un token d'authentification.

Vous pouvez le générer dans votre profil GitLab, à l'adresse https://gitlab.com/profile/personal_access_tokens

Ce token à une durée de vie limité et vous devrez le renouveler périodiquement.

> **Notez** bien la valeur de ce token car il n'est affiché qu'une fois.

Pour un accès en lecture/écriture à un projet, vous pouvez cocher **read_repository** et **write_repository**.

Ce token s'utilise dans l'url, par exemple pour cloner un projet:

```
git clone https://USER:TOKEN@gitlab.com/YOUR_PROJECT
```

## Configurez ~/.netrc pour GitLab

Pour éviter d'avoir à utiliser le token dans les URL, vous pouvez créer une entrée dans un fichier ~/.netrc:

```
vi ~/.netrc

machine gitlab.com
    login YOUR_LBN_EMAIL
    password YOUR_TOKEN

chmod 600 ~/.netrc
```


