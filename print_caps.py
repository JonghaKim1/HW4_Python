# print_caps.py
from functools import wraps

def allcaps(func):
    @wraps(func)
    def wrapper():
        result = func()
        return result.upper() if isinstance(result, str) else result
    return wrapper
