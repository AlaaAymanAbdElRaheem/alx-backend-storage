#!/usr/bin/env python3
"""uses the requests module to obtain the HTML content
of a particular URL and returns it."""


import requests
import redis
from typing import Callable
from functools import wraps



def count(method: Callable) -> Callable:
    """ counts how many times methods of the Cache class are called"""
    @wraps(method)
    def wrapper(url):
        """ Wrapper function """
        connection = redis.Redis()
        connection.incr(f"count:{url}")
        result = method(url)
        connection.setex(f"result:{url}", 10, result)
        return result
    return wrapper


def get_page(url: str) -> str:
    """ returns the HTML content of the URL """
    return requests.get(url).text
