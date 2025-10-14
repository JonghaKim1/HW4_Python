# log.py
import time
from functools import wraps

def timestamp(func):
    @wraps(func)
    def wrapper():
        print(time.ctime())
        func()
    return wrapper
