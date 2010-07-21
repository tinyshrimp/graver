'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

class EventHandler(object):
    def __init__(self):
        self._handlers = []

    def add(self, handler):
        if self._handlers.__contains__(handler):
            return
        self._handlers.append(handler)

    def remove(self, handler):
        if self._handlers.__contains__(handler):
            self._handlers.remove(handler)

    def invoke(self, sender, args):
        for handler in self._handlers:
            handler(sender, args)
            