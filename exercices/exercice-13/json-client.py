#!/usr/bin/env python3

import logging
import json

import requests

logger = logging.getLogger(__name__)

def download_todos(filepath="todos.json"):
    logger.info(f"START download todos to file : {filepath}")

    res = requests.get("https://jsonplaceholder.typicode.com/todos")
    res.raise_for_status()
    
    with open(filepath, 'w') as fp:
        json.dump(res.json(), fp, indent=4)
    
    logger.info("END download todos")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    download_todos()
    