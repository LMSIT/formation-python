# Utilisation de templates Jinja

Jinja est un framework de template très utilisé dans le monde Python mais également dans [Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html) et d'autres outils.

Sa syntaxe est inspiré des templates du framework Django et d'autres languages ont repris et adaptés cette syntaxe dans leur language.

Un language de template permet d'aller plus loin que la simple concaténation de chaine de caractères. Il fournit des fonctions, des conditions (if/else/endif), des boucles et un système d'héritage pour relier plusieurs templates.

La documentation se trouve ici: https://jinja.palletsprojects.com/

**Utilisation simple:**

> N'oubliez pas d'installer la librairie Jinja2 pour tester ces exemples: `pip install jinja2`

```python
from jinja2 import Template
template = Template('Hello {{ first_name }} {{ last_name }}')
template.render(first_name='Alain', last_name='DURANT')
```

**Définition de fichiers de templates:**

```jinja
# base.j2 ou base.html
<html>
    <head>
        <title>{% block title %}LBN Site{% endblock %}</title>          
    </head>
    <body>
        <h1>{% block page_title %}{% endblock %}</h1>
        {% block page %}
        <div class="page">
            {% block content %}{% endblock %}
        </div>
        {% endblock %}
    </body>
</html>
```

```jinja
# home.j2
{% extends "base.j2" %}

{% block title %}LBN Site - Home Page{% endblock %}

{% block content %}
My text......
{% endblock %}
```


