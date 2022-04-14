# Formation d'initiation à Python

Le support est découpé en 3 parties:
- Les slides à projeter pendant le cours
- Le support
- Les solutions aux exercices


## Support

Publié temporairement à l'adresse https://lmsit.github.io/formation-python/

La documentation est rédigé en Markdown et affiché dynamiquement à l'aide de l'outil https://docsify.js.org/

Il n'y a pas comme pour les slides de phases de compilation/transformation.

Il suffit d'ouvrir le fichier index.html dans un navigateur ou avec:

```bash
python3 -m http.server -d docs
```

## Solutions des Exercices

Les solutions sont dans le répertoire exercices/

Pour exécuter les solutions, il faut installer les dépendances:

```bash
pip install -r requirements.txt
```

## TODO

- [ ] Publier les slides et la doc sur un support interne (OKD ?)
- [ ] Automatisation de la publication avec Gitlab-CI