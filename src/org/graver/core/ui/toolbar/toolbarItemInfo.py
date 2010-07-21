'''
Created on Jun 5, 2010

@author: tinyshrimp
'''

class ToolbarItemInfo(object):
    def __init__(self, name, action, image='', tip=''):
        self._name = name
        self._image = image
        self._tip = tip
        self._action = action
        
    def getName(self):
        return self._name
    
    def getImage(self):
        return self._image
    
    def getTip(self):
        return self._tip
    
    def getAction(self):
        return self._action
    