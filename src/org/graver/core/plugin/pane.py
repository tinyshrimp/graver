'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx
from org.graver.core.plugin.view import View

class Pane(View):
    def __init__(self, parent, name, caption, pos=wx.DefaultPosition, showCaption=True):
        if self.__class__ is Pane:
            raise Exception('Cannot instantiate abstract class %s.' % self.__class__)
        View.__init__(self, parent)
        
        self._name = name
        self._caption = caption
        self._pos = pos
        self._showCaption = showCaption
        
    def getName(self):
        return self._name
    
    def getCaption(self):
        return self._caption
    
    def getPosition(self):
        return self._pos
    
    def isShowCaption(self):
        return self._showCaption