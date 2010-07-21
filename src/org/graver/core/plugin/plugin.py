'''
Created on Jun 2, 2010

@author: tinyshrimp
'''

class Plugin(object):
    def __init__(self):
        self._name = ''
        self._actions = None
        self._views = None
        
    def getName(self):
        return self._name
    
    def getActions(self):
        if self._actions is None:
            self._actions = {}
        return self._actions
    
    def getViews(self):
        if self._views is None:
            self._views = {}
        return self._views
        