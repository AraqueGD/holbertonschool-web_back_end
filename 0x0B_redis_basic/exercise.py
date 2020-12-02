#!/usr/bin/env python3
""" Modules Import """
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache():
    """ Class Cache """

    def __init__(self):
        """ Constructor Init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union(str, bytes, int, float)) -> str:
        """ Store Method """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
