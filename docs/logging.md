# Les logs Python avec le module logging

https://docs.python.org/3.5/library/logging.html

Les logs font parties d'une application et sont très important pour retrouver une erreur ou une action.

Le module logging Python est puissant mais très simple à utiliser.

L'utilisation la plus courante:

```
import logging

logger = logging.getLogger(__name__)

logger.info("normal message")
logger.error("error message")
logger.critical("critical message")
```

TODO: configuration