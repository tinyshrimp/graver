'''
Created on Jun 5, 2010

@author: tinyshrimp
'''

class ActionManager(object):
    def __init__(self):
        self._actions = None
        
    def getActionGroups(self):
        if self._actions is None:
            self._actions = {}
        return self._actions
    
    def getAction(self, name):
        name = name.strip()
        if name is None or '' == name:
            return None
        
        actionGroupName = None
        actionName = None
        try:
            actionGroupName, actionName = name.split('.')
            actionGroupName = actionGroupName.strip()
            actionName = actionName.strip()
        except ValueError:
            return None
        
        if actionGroupName is None or '' == actionGroupName or actionName is None or '' == actionName:
            return None 
        
        if not self.getActionGroups().has_key(actionGroupName):
            return None
        
        actionGroup = self.getActionGroups()[actionGroupName]
        if actionGroup is None:
            return None
        
        if not actionGroup.getActions().has_key(actionName):
            return None
        
        return actionGroup.getActionInstance(actionName)
        