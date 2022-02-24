# Git Aide Mémoire

## Installation

TODO...

## Configuration

Il y a deux paramètres obligatoires pour utiliser Git:
- Le username
- L'email

Ce sont ces paramètres qui seront utilisés pour identifier les personnes qui auront contribués à un projet.

**Pour configurez Git avec ces 2 paramètres:**

```bash
git config --global user.name "Stéphane RAULT"
git config --global user.email s.rault@linkbynet.com
```

**Vérifier la configuration globale de Git:**

```
git config --global -l
user.name=Stéphane RAULT
user.email=stephane.rault@radicalspam.org
```

**Vous pouvez également définir des alias qui vous seront très utiles:**

```
# git st
git config --global alias.st=status
# git br
git config --global alias.br=branch
# git co master
git config --global alias.co=checkout
# git ci -m "message"
git config --global alias.ci=commit
```

## Versionner un projet avec Git

En partant du principe que vous venez de créer un repository **python-training** dans votre espace utilisateur GitLab, voici les commandes à effectuer pour commencer à l'utiliser:

```shell
$ cd exercices
$ git init
$ git remote add origin https://YOUR_GIT_USERNAME:TOKEN@git.lbn.fr/YOUR_GIT_USERNAME/python-training.git
$ git add .
$ git commit -m "initial commit"
$ git push origin master
```

> Le token d'authentification à gitlab doit être généré [ici](https://git.lbn.fr/profile/personal_access_tokens)


- Si le dépôt existait déjà sur Gitlab et qu'il contenait déjà des fichiers, nous aurions seulement utilisé:
```shell
git clone https://YOUR_GIT_USERNAME:TOKEN@git.lbn.fr/YOUR_GIT_USERNAME/python-training.git
```

## Les commandes essentielles de GIT

- `git init`: Active git pour le répertoire en cours (créé un sous-répertoire .git)
- `git status` / `git st` : Affiche le status des fichiers dans le dépôt local
- `git add -A` . : Active ou met à jour le suivi de version des fichiers
- `git commit -m "message"` / `git ci -m "message"` : Publie localement les dernières modifications
- `git remote add origin http://xxx`: Définit l'adresse du dépôt distant (.git/config)
- `git push origin master`: Publie les modifications de la branche master sur le dépôt distant
- `git log`: Affiche les dernières modifications
- `git clone <REPO>`: Clone un projet existant
- `git config`: Gère la configuration de Git
- `git diff`: Affiche les modifications depuis le dernier commit
