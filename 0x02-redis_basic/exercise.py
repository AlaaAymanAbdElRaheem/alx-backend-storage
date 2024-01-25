#!/usr/bin/env python3
""" Module for testing exercise code. """


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Method that takes a single method Callable argument and
    returns a Callable """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Method that takes a single method Callable argument and
        returns a Callable """

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function """
        output = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output
    return wrapper


def replay(method: Callable)-> None:
    """ Method that displays the history of calls of a particular function """
    counts = method.__self__._redis.get(method.__qualname__).decode("utf-8")
    print("{} was called {} times:".format(method.__qualname__,
                                           counts))
    inputs = method.__self__._redis.lrange(method.__qualname__ + ":inputs",
                                           0, -1)
    outputs = method.__self__._redis.lrange(method.__qualname__ + ":outputs",
                                            0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """ Class for implementing a Cache """

    def __init__(self):
        """ Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
