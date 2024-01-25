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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
                                                                    str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """ Method that takes a key string argument
        and an optional Callable argument """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Method that takes a key string argument and returns a string """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Method that takes a key string argument and returns an int """
        return self.get(key, int)
