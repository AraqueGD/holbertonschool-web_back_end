#!/usr/bin/python3
""" LFU Cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class LFUCache """

    def __init__(self):
        """ Cosntructor """
        super().__init__()
        self.list_cache = []
        self.count = {}

    def put(self, key, item):
        """ Method Put """
        if (key is None or item is None):
            return

        self.cache_data[key] = item

        item_count = self.count.get(key, None)

        if (item_count is not None):
            self.count[key] += 1
        else:
            self.count[key] = 1

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first = self.get_first(self.list_cache)
            if (first):
                self.list_cache.pop(0)
                del self.cache_data[first]
                del self.count[first]
                print("DISCARD: {}".format(first))

        if key not in self.list_cache:
            self.list_cache.insert(0, key)
        self.right_list(key)

    def get(self, key):
        """ Method Get """
        item = self.cache_data.get(key, None)
        if (item is not None):
            self.count[key] += 1
            self.right_list(key)
        return item

    @staticmethod
    def get_first(array):
        """ Get First Item """
        return array[0] if array else None

    def right_list(self, item):
        """ Right List """
        length = len(self.list_cache)

        idx = self.list_cache.index(item)
        item_count = self.count[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.list_cache[i + 1]
                nxt_count = self.count[nxt]

                if nxt_count > item_count:
                    break

        self.list_cache.insert(i + 1, item)
        self.list_cache.remove(item)
