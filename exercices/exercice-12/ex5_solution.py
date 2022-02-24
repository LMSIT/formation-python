#!/usr/bin/env python

import json
import logging

logger = logging.getLogger("ex5")

def load_and_print(filename):
    try:
        with open(filename) as fp:
            data = json.load(fp)
            print(data)
    except FileNotFoundError as err:
        logger.error(err)

if __name__ == "__main__":
    load_and_print("file.json")

