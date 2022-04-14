# Analyser et comprendre un projet Python existant

Vous aurez peut être un jour, la charge de reprendre le développement total ou partiel d'un projet Python ou vous souhaiterez en savoir plus sur une librairie Python avant de l'intégrer dans votre script.

## Analyse d'un projet open-source sur Github

- https://github.com/psf/requests

**Regardez toujours:**

- Les stars: 43700 stars c'est assez exceptionnel pour un projet. Cela signifie qu'au minimum 43700 personnes soutiennent, utilise le projet et remontent éventuellement des bugs.
- La date du dernier commit: Vous devez éviter d'intégrer une librairie qui n'est plus maintenue ou il faut chercher un fork actif
- La documentation: D'abord dans le README et toutes documentation extérieur qui doivent vous permettre de prendre rapidement en main la librairie
- La liste des contributeurs: https://github.com/psf/requests/graphs/contributors
- La liste des pull requests ouvertes: https://github.com/psf/requests/pulls . Ce sont les propositions de corrections ou d'ajout de fonctionnalités. Si il y en a trop en attente ou de très anciennes qui n'ont pas été closes, il y a peut être un problème avec le propriétaire du projet.
- Le taux de couverture des tests: Sur Github, en haut du README, vous trouvez souvent des mini-graphiques avec des couleurs dont l'un d'eux pointent vers un CI/CD (github-actions, travis, circle-ci, autres...)
- Le type de licence est important. Il faut vérifier qu'il sera compatible avec votre usage future
- Les dépendances à d'autres projets. Soit dans setup.py, soit dans requirements.txt
- La fréquence des releases

**A vérifier si vous avez le temps:**

- La présence d'une démonstration en ligne quand ce serait pertinent
- Regardez le code de la librairie, vous y verrez peut être une mauvaise organisation, un manque d'optimisation mais vous y verrez souvent de quoi vous faire progresser

## Analyse d'un projet internet sur Gitlab

- https://gitlab.com/engieit/fastmep-projects/fastmep-next/lms-sdk/lms-lrc

**Ce sont à peu près les mêmes critères que pour un projet open-source:**

- Documentation
- Tests et taux de couverture des test
    - Graphique pipeline en haut du readme
    - Graphique coverage en haut du readme
    - https://gitlab.com/engieit/fastmep-projects/fastmep-next/lms-sdk/lms-lrc/-/pipelines
    - https://gitlab.com/engieit/fastmep-projects/fastmep-next/lms-sdk/lms-lrc/-/jobs/233059
- Qualité du code
- Date du dernier commit

**Particularités internes:**

- Contributeurs (souvent, un seul chez lms)
    - Attention à vérifier dans l'annuaire si le collaborateur est toujours chez lms
- Dépendances à d'autres projets interne
- Codes d'accès spécifiques ou documentation pour les trouver sur Idefix, le wiki ou ailleurs
