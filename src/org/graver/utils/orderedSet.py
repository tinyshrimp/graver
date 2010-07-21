#!/usr/bin/env python
#coding=UTF-8

__author__="tiny.strimp"
__date__ ="Sep 21, 2009"

class OrderedSet(object):
    def __init__(self):
        self._set = {}
        self._keys = []
        self._values = []

    def clear(self):
        self._set.clear()
        self._keys.clear()
        self._values.clear()

    def get(self, key):
        return self._set[key]

    def put(self, key, value):
        if key is None:
            return
        
        if self._set.has_key(key):
            self._set[key] = value
            key_index = self._keys.index(key)
            self._values[key_index] = value
        else:
            self._set[key] = value
            self._keys.append(key)
            self._values.append(value)
            
    def insert(self, key, value, pos):
        if key is None:
            return False
        
        if pos >= len(self._keys):
            self.put(key, value)
            return False
        
        if self._set.has_key(key):
            return False
        
        self._set[key] = value        
        self._keys.insert(pos, key)
        self._values.insert(pos, value)
        
        return True

    def remove(self, key):
        if not self._set.has_key(key):
            return

        try:
            key_index = self._keys.index(key)
            self._values.pop(key_index)
        except ValueError:
            pass

        try:
            self._keys.remove(key)
        except ValueError:
            pass        
        
        self._set.pop(key)

    def has_key(self, key):
        return self._set.has_key(key)

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def length(self):
        return len(self._set)
