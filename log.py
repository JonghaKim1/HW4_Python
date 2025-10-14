# log.py
import time
from functools import wraps

def timestamp(func):
    """Decorator that prints the current time before running the function."""
    @wraps(func)
    def wrapper():
        print(time.ctime())
        func()
    return wrapper
