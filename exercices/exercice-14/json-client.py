#!/usr/bin/env python3

import logging
import json
import os

import requests

logger = logging.getLogger(__name__)

TODOS_URLS = os.environ.get("TODOS_URLS", "https://jsonplaceholder.typicode.com/todos")

def download_todos(filepath="todos.json"):
    logger.info(f"START download todos to file : {filepath} from url : {TODOS_URLS}")
    res = requests.get(TODOS_URLS)
    res.raise_for_status()
    return res.json()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    todos = download_todos()
    for todo in todos:
        print(f"{todo['id']} : {todo['title']}")
    