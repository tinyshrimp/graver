'''
Created on Jun 2, 2010

@author: tinyshrimp
'''

class PluginManager(object):
    def __init__(self):
        self._plugins = None
        self._editors = None
        
    def getPlugins(self):
        if self._plugins is None:
            self._plugins = {}
        return self._plugins
    
    def getPlugin(self, name):
        if not self.getPlugins().has_key(name):
            return None
        return self.getPlugins()[name]
    
    def getEditors(self):
        if self._editors is None:
            self._editors = {}
        return self._editors
    
    def addPlugin(self, plugin):
        pass
    
        