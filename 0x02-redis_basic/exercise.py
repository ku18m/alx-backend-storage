#!/usr/bin/env python3
"""Using redis with python"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ Class Cache that handles redis connection and methods """
    def __init__(self) -> None:
        """ Class constructor which starts the connection """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores the given data and return it's uuid generated key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
