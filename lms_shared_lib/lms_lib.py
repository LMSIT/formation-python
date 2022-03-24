import logging
import json
import time


from decouple import config
import requests
from .utils import retry

logger = logging.getLogger(__name__)

class CI:

    def create_resource_group():
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)