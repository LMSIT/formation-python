# Introduction au CI/CD avec Gitlab-CI

Le CI/CD (Continuous Integration / Continuous Delivery) fait partis des pratiques essentiels du DevOps.

Il s'agit de mettre en oeuvre un workflow d'automatisation pour:
- Le provisionning d'infrastructure (ex: avec Terraform)
- L'exécution de tests unitaires et qualités
- La fabrication et la livraison de binaires
- La mise à jour d'application dans des environnement de type Staging et Production

Parmis les outils open-source les plus utilisés en CI/CD, vous entendrez sûrement parler de [Jenkins](https://fr.wikipedia.org/wiki/Jenkins_(logiciel)) qui existe depuis 2008.

Ne vous attachez pas trop à un produit en particulier car le concept du CI/CD est le même dans tous les produits concurrents.

Les concepts communs:
- Un pipeline d'exécution
- Des tâches individuels (Job) à l'intérieur du Pipeline
- Un lien étroit avec les repositories pour que l'envoi de commit puisse déclencher l'exécution d'un pipeline

Pour démystifier le CI/CD, sachez que toutes les tâches qui s'exécuterons dans un pipeline, peuvent également êtres exécutés sur votre poste de travail.

**Par exemple:**

- Lancer des tests unitaires
- Vérifier la qualité du code
- Produire un binaire ou une image Docker
- Publier le package sur un dépôt comme Pypi.

**Ce qu'apportent le CI/CD:**

- Dans un développement en équipe, il est important que la totalité des tâches du pipeline, soit exécutés, le soit dans l'ordre et le soit pour chaque commit envoyé sur le dépôt de source du projet.
- Certaines tâches nécessitent des comptes de services et des paramètres privés qui ne doivent pas êtres diffusés, même à l'intérieur d'une équipe. Le CI/CD centralisera et gèrera ces données dans un stockage sécurisé.
- Le pipeline peut être exécuté périodiquement sans attendre un commit pour produire quotidiennement une release "Nightly Builds"

**Gitlab et Gitlab-CI:**

L'une des particularités de Gitlab-CI est qu'il est couplé et parfaitement intégré à Gitlab. Ce qui peut également être un inconvénient quand vous gérez vos sources sur un autre produit que Gitlab.

La seconde particularité est que les pipeline ou plutôt, les jobs, sont exécutés à l'intérieur d'image Docker. Donc, tous ce qui ne fonctionnent pas dans Docker, ne fonctionnera pas non plus avec Gitlab-CI, ex: la création d'une VirtualBox.

Pour activer l'exécution d'un pipeline sur votre projet, vous devez seulement définir un fichier [.gitlab-ci.yml](https://docs.gitlab.com/ee/ci/yaml/README.html) à la racine de votre projet et d'y décrire votre pipeline.

TODO: runners