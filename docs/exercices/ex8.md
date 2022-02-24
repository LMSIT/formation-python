# Exercice n°8

## Scénario

Créez et utilisez un template Jinja pour formater le fichier .htaccess

## Opérations à réaliser

1. Modifiez la fonction parse_csv() pour qu'elle renvoi une liste de tuple (rule, ip)
2. Créez la fonction render_template(ip_rules, template_filepath="htaccess.j2") qui recevra la liste de tuple et utilisera le template htaccess.j2 et renverra le contenu définitif du .htaccess
3. Créez le template htaccess.j2
4. Modifiez la fonction write_file() qui va maintenant recevoir un texte
5. Modifiez la fonction main() pour prendre en compte tous ces changements
6. Exécutez et testez le fichier htaccess.txt sur http://www.htaccesscheck.com/
7. Quand le script fonctionne, effectuez un commit avec le libellé "exercice 08 done" et un push

## Acquis

- Utilisation de template Jinja2
