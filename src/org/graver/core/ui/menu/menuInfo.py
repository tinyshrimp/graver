'''
Created on Jun 5, 2010

@author: tinyshrimp
'''

from org.graver.utils.orderedSet import OrderedSet

class MenuInfo(object):
    def __init__(self, name, image='', tip='', action=''):
        self._name = name
        self._action = action
        self._image = image
        self._tip = tip
        self._children = None
        self._actionInstance = None
        
    def getChildren(self):
        if self._children is None:
            self._children = OrderedSet()
        return self._children
    
    def getName(self):
        return self._name
    
    def getImage(self):
        return self._image
    
    def setImage(self, image):
        self._image = image
        
    def getTip(self):
        return self._tip
    
    def setTip(self, tip):
        self._tip = tip
    
    def getAction(self):
        return self._action
    
    def setAction(self, action):
        self._action = action
    
    