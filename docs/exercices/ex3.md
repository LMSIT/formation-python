# Exercice n°3

## Scénario

À la suite d’erreurs dans le format d’adresse IP, vous allez ajouter une validation du format dans le générateur de fichier .htaccess à l’aide du module standard [ipaddress](https://docs.python.org/fr/3.7/library/ipaddress.html) 

Vous en profiterez pour mettre à profit vos nouvelles connaissances sur les Exception et le Logging.

## Opérations à réaliser

1. Ajoutez une ligne dans le fichier CSV avec une adresse IP mal formatée
2. Pour chaque adresse ip trouvée dans le fichier CSV, validez le format avec le module https://docs.python.org/fr/3.7/library/ipaddress.html. Ex: `ipaddress.ip_address(row['IP Address'])`
3. Capturez l'exception et affichez l'erreur ainsi que l'adresse IP concernée
4. Quand le script fonctionne, effectuez un commit avec le libellé "exercice 03 done" et un push

## Acquis

* Utilisation du module ipaddress
* Utilisation de la capture d'Exception
* Utilisation du module logging
