#!/usr/bin/python3
"""Module for class FIFOCache that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """caching system"""
    def __init__(self):
        """innitializes"""
        super().__init__()

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_Items \
                    and key not in self.cache_data.keys():
                        first_key = next(iter(self.cache_data.keys()))
                        del self.cache_data[first_key]
                        print("DISCARD: {}".format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            None
        return self.cache_data.get(key)
