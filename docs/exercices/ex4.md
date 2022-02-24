# Exercice n°4

## Scénario

Transformez le code du générateur de fichier .htaccess en le réécrivant sous forme de fonction et appelez les fonctions à l’intérieur d’une fonction main.

## Opérations à réaliser

1. Placez le code de parsing du CSV dans une fonction parse_csv() et renvoyer un tableau contenant pour chaque ligne, la chaine Allow ou Deny avec l'adresse IP
2. Placez le code d'écriture du fichier htaccess dans une fonction write_file() à qui vous passerez le tableau récupérer de la fonction parse_csv()
3. Appellez les 2 fonctions à partir d'une fonction main() et n'oubliez pas d'insérer la première ligne et dernière ligne avant de générer le fichier htaccess.
4. Exécutez le script et vérifiez le résultat
4. Quand le script fonctionne, effectuez un commit avec le libellé "exercice 04 done" et un push

## Acquis

- Organisation du code en fonctions
- Utilisation de la pseudo fonction main