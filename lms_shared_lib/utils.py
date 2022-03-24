import time
import logging

from urllib3.connection import HTTPSConnection

logger = logging.getLogger(__name__)

def retry(tries=3, sleep_time=2):
    """Retry calling the decorated function
    :param tries: number of times to try
    :type tries: int
    
    >>> @retry(tries=3, sleep_time=2)
    >>> def download_page(url):
    >>> ...return requests.get(url)
    
    """

    def try_it(func):
        def f(*args, **kwargs):
            attempts = 0
            while True:
                try: 
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if isinstance(e, HTTPSConnection):
                        print("!!! ERROR !!! : host [%s]" % e.host)

                    logger.error(
                        "retry %s - error[%s] - attempts[%s/%s]"
                        % (func, str(e), attempts, tries)
                    )
                    if attempts >= tries:
                        raise e
                    time.sleep(sleep_time)
        
        return f
    
    return try_it