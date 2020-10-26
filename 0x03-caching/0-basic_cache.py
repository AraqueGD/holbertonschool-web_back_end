#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache """

    def put(self, key, item):
        """ Method Put """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ Method Get """
        return self.cache_data.get(key, None)
