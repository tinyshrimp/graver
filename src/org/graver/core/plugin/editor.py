'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

from org.graver.core.plugin.view import View
from org.graver.utils.eventHandler import EventHandler

class Editor(View):
    def __init__(self, parent):
        if self.__class__ is Editor:
            raise Exception('Cannot instantiate abstract class %s.' % self.__class__)
        View.__init__(self, parent)
        
        self._contentChangedEventHandler = None
        self._contentSavedEventHandler = None
        
    def saveFile(self, filename):
        pass
    
    def openFile(self, filename):
        pass
    
    def copy(self):
        pass
    
    def paste(self):
        pass
    
    def cut(self):
        pass
    
    def delete(self):
        pass
    
    def undo(self):
        pass
    
    def redo(self):
        pass
        
    def getContentChangedEventHandler(self):
        if self._contentChangedEventHandler is None:
            self._contentChangedEventHandler = EventHandler()
        return self._contentChangedEventHandler
    
    def getContentSavedEventHandler(self):
        if self._contentSavedEventHandler is None:
            self._contentSavedEventHandler = EventHandler()
        return self._contentSavedEventHandler
    