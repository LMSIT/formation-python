# Les possibilités de traitements parallèles en Python

Quand vous exécutez un script Python, il est relié à un [Processus](https://fr.wikipedia.org/wiki/Processus_(informatique)) unique et [Thread](https://fr.wikipedia.org/wiki/Thread_(informatique)) unique.

Le code s'exécute séquentiellement et si une tâche est bloqué comme par exemple, un appel de Web Service, le reste du code doit attendre pour s'exécuter.

Dans l'exemple du générateur de fichier .htaccess, imaginez que vous ayez besoin de traiter 1000 fichiers CSV qui vont générer 1000 fichiers htaccess différents.

**Analysons les parties principales de notre htaccess-generator:**

1. La fonction parse_csv() ouvre et lit un fichier qui peut contenir plusieurs milliers de ligne
    1.1 A l'intérieur de cette fonction, nous faisons appel au module ipaddress pour valider chaque adresse IP
2. La fonction render_template() va ouvrir un fichier de template et renvoyer un texte avec le contenu du fichier .htaccess
3. La fonction write_file() va écrire le fichier sur disque

**Les enjeux du parallèlisme:**

- Durée d'exécution qui doit prendre en compte la gestion d'un à plusieurs milliers de fichiers htaccess à générer
- Consommation CPU et RAM qui peuvent être exponentiels
- Accès en lecture/écriture au disque ou un flux réseaux (BDD, Web Service, ...)
- Le partage en lecture/écriture dans le même espace mémoire. Ex: un compte global sous forme de variable qui serait incrémenté par chaque thread.

## Solution avec le multi threading

Nous pourrions commencer par réunir l'appel aux 3 fonctions principales à l'intérieur d'une function comme c'est le cas de la méthode main().

Pour chaque fichier CSV à traiter en parallèle, nous pouvons créer un Thread et exécuter la totalité des threads.

Pour éviter une surconsommation mémoire, nous avons la possibilité de limiter le nombre de thread qui s'exécuterons simultanément.

**Pseudo code pour la réalisation:**

```python
from threading import Thread, current_thread

HTACCESS_DATAS = [
    {"csv_filepath": "ip1.csv", "output_filepath": "client1/htaccess"},
    {"csv_filepath": "ip2.csv", "output_filepath": "client2/htaccess"},
    {"csv_filepath": "ip3.csv", "output_filepath": "client3/htaccess"},
]

def main(csv_filepath, output_filepath):
    # Affichera le numéro de thread en cours
    print("current thread : %s" % current_thread())
    datas = parse_csv(csv_filepath)
    result = render_template(datas)
    write_file(result, output_filename=output_filepath)

def main_multi_thread():
    threads = []
    for data in HTACCESS_DATAS:
        t = Thread(target=main, args=(data['csv_filepath'], data['output_filepath']))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main_multi_thread()
```

*Dans cet exemple, nous n'avons pas traité le nombre maximum de thread simultanés, ce qui posera un problème de surcharge CPU/RAM si vous devez traiter plusieurs centaines de fichier CSV.*

Une version de multi thread plus simple existe depuis la version 3.2 de Python dans le module concurrent.futures:

Elle à aussi l'avantage de gérer très simplement le nombre de Thread simultanés avec le paramètre `max_workers`

```python
from concurrent.futures import ThreadPoolExecutor

def main_multi_thread():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for data in HTACCESS_DATAS:
            executor.submit(main, data['csv_filepath'], data['output_filepath'])
        # voir aussi executor.map(main, HTACCESS_DATAS) en modifiant main()
```

**Conclusions:**
- La solution est relativement simple à mettre en oeuvre avec peu de refactoring du code existant
- Il sera difficile de gérer la consommation CPU/RAM qui peuvent être rapidement saturé, même en limitant le nombre de threads simultanés.
- Nous n'avons pas gérés d'accès bloquant (web service, BDD, ...) mais le multi-threading ne serait pas indiqué pour ce besoin.

## Solution avec le multi processing

A la solution multi-thread, nous étions toujours dans le même processus, lui même relié à un seul processeur (ou coeur).

Avec le multi-processing, nous pouvons exécuté plusieurs processus, chaque étant exécuté sur un processeur différent.

Nous allons utiliser la même base de pseudo code que pour les theads et remplacer uniquement la fonction main_multi_thread() par une fonction main_multi_processing()

```python
from concurrent.futures import ProcessPoolExecutor

def main_multi_processing():
    # Si max_workers n'est pas renseigné, 
    # ProcessPoolExecutor utilisera tous les processeurs disponibles
    with ProcessPoolExecutor() as executor:
        for data in HTACCESS_DATAS:
            executor.submit(main, data['csv_filepath'], data['output_filepath'])

if __name__ == "__main__":
    main_multi_thread()
```

**Conclusions:**
- Comme pour le multi-threading, la solution est relativement simple à mettre en oeuvre avec peu de refactoring du code existant
- Le parallélisme sera limité au nombre de processeur !

## Solution avec les coroutines

Une coroutine est un concept un peu difficile à expliquer mais vous trouvez plusieurs documentations sur internet dont celle de [wikipédia](https://fr.wikipedia.org/wiki/Coroutine#:~:text=Dans%20un%20programme%2C%20une%20coroutine,signal%C3%A9%20de%20reprendre%20son%20cours)

Son arrivé dans plusieurs langages à permis de d'améliorer considérablement le parallélisme en réduisant la consommation exponentiels de RAM/CPU et en gérant plus particulièrement, le problème des accès bloquants.

En python, c'est le module [asyncio](https://docs.python.org/fr/3.7/library/asyncio-task.html) qui fournit ce mécanisme.

Attention car il faut vraiment s'habituer aux spécificités de la syntaxe qui est un peu trop verbeuse à mon goût.

Par exemple, une fonction `def my_function` se déclare `async def my_function()` pour être asynchrone et à l'intérieur de cette fonction, il faut également utiliser d'autre mot clés comme "await".

Vous pouvez regarder la librairie [aiohttp](https://docs.aiohttp.org/en/stable/) qui est un remplaçant Asynchrone (coroutines avec asyncio) de la librairie [requests](https://requests.readthedocs.io/)

J'ai pris l'habitude, bien avant l'arrivé de Python AsyncIO d'utiliser une autre librairie pour les coroutines. Il s'agit de [gevent](http://www.gevent.org/) qui est beaucoup moins invasive que **asyncio** et produit de très bons résultats.

Gevent fournit un module de patching qui permet de remplacer des modules standard Python par une version asynchrone sans autre intervention de votre pars.

**Exemple:**

```
from gevent import monkey; monkey.patch_socket()
```

Ce simple ajout au début de votre script, permettra de patcher le module [socket](https://docs.python.org/3/library/socket.html) qui est utilisé pour toutes les connections réseaux (BDD, WebService, ...)

Vous pouvez également patché beaucoup d'autres modules avec `monkey.patch_all()`.

## Solution avec les workers

TODO: celery

## Solution avec le ServerLess et les micros-services

TODO: Azure

## Quelques liens

- https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/2235545-faites-de-la-programmation-parallele-avec-threading
