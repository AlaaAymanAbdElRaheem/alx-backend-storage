#!/usr/bin/env python3
""" Module for testing exercise code. """


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ Class for implementing a Cache """

    def __init__(self):
        """ Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
