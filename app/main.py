from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper_cache(*args) -> dict:
        cache_key = func.__name__ + str(args)

        if cache_key not in results_cache:
            print("Calculating new result")
            results_cache[cache_key] = func(*args)
        else:
            print("Getting from cache")

        return results_cache[cache_key]

    return wrapper_cache
