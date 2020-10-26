#!/usr/bin/python3
""" Lifo Cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache """

    def __init__(self):
        """ Cosntructor """
        super().__init__()
        self.list_cache = []

    def put(self, key, item):
        """ Method Put """
        if (key is None or item is None):
            return

        self.cache_data[key] = item

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            if (self.list_cache):
                l = self.list_cache.pop()
                del self.cache_data[l]
                print("DISCARD: {}".format(l))

        if (key not in self.list_cache):
            self.list_cache.append(key)
        else:
            self.l_list(key)

    def get(self, key):
        """ Method Get """
        return self.cache_data.get(key, None)

    def l_list(self, item):
        """ Method Lasted List Item """
        length = len(self.list_cache)
        if self.list_cache[length - 1] != item:
            self.list_cache.remove(item)
            self.list_cache.append(item)
