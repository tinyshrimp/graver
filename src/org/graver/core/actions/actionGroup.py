'''
Created on Jun 10, 2010

@author: tinyshrimp
'''

from org.graver.utils.instantiator import createClassInstance

class ActionGroup(object):
    def __init__(self, name, createToolbar=True):
        self._createToolbar = True
        self._visible = True
        self._actions = None
        self._name = name
        
    def getName(self):
        return self._name
        
    def getActions(self):
        if self._actions is None:
            self._actions = {}
        return self._actions
    
    def getActionClassPath(self, name):
        name = name.strip()
        if name is None or '' == name:
            return None
        
        if not self.getActions().has_key(name):
            return None
        
        return self.getActions()[name][0]
    
    def getActionInstance(self, name):
        name = name.strip()
        if name is None or '' == name:
            return None
        
        if not self.getActions().has_key(name):
            return None
        
        actionClassPath, actionInstance = self.getActions()[name]
        if actionInstance is None:
            actionInstance = self.__getActionInstance(actionClassPath)
            self.getActions()[name] = (actionClassPath, actionInstance)
        return actionInstance
    
    def isCreateToolbar(self):
        return self._createToolbar
    
    def setVisible(self, visible):
        self._visible = visible
        
    def getVisible(self):
        return self._visible
        
    def __getActionInstance(self, name):
        if name is None or '' == name:
            return None
        
        actionClassObj = createClassInstance(name)
        if actionClassObj is None:
            return None
        
        return actionClassObj()
        