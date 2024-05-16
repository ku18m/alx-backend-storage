#!/usr/bin/env python3
"""Using redis with python"""
import redis
from typing import Union, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ A counter decorator that counts the calls and store it in redis """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ The counter callable """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Class Cache that handles redis connection and methods """
    def __init__(self) -> None:
        """ Class constructor which starts the connection """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores the given data and return it's uuid generated key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> str:
        """
        Retrieves the data of the given key
        and convert it with the given conversion function
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Retrieves the data of the given key and decode it """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Retrieves the data of the given key and convert it to int """
        data = self._redis.get(key)
        try:
            data = int(data)
        except Exception:
            data = 0
        return data
