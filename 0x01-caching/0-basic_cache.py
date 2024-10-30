#!/usr/bin/python3
"""Module for class BasicCache that inherits from BaseCaching:
    Is a caching system
    Uses self.cache_data - dictionary from Parent class(BaseCaching)
    Is system has no limit
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """inherits from BaseCaching"""

    def __init__(self):
        """innitiliazes"""
        super().__init__()

    def put(self, key, item):
        """method to add an item to cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    def get(self, key):
        """retrieves values cfrom the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
