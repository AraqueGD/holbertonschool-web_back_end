#!/usr/bin/python3
""" LRY Cache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class LRUCache """

    def __init__(self):
        """ Cosntructor """
        super().__init__()
        self.list_cache = []

    def put(self, key, item):
        """ Method Put """
        if (key is None or item is None):
            return

        if (key not in self.list_cache):
            self.list_cache.append(key)
        else:
            self.l_list(key)

        self.cache_data[key] = item

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first = self.get_first(self.list_cache)
            if (first):
                self.list_cache.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Method Get """
        item = self.cache_data.get(key, None)
        if (item is not None):
            self.l_list(key)
        return item

    def l_list(self, item):
        """ Method Lasted List Item """
        length = len(self.list_cache)
        if self.list_cache[length - 1] != item:
            self.list_cache.remove(item)
            self.list_cache.append(item)

    @staticmethod
    def get_first(array):
        """ Get First Item """
        return array[0] if array else None
