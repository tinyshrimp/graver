'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import os

from org.graver.utils.eventHandler import EventHandler
from org.graver.core.plugin.editor import Editor

class Document(object):
    def __init__(self, fullPath):
        self._fullPath = fullPath
        self._editor = None
        self._contentChanged = False
        
        self._documentChangedEventHandler = None
        self._documentSavedEventHander = None
        self._documentNameChangedEventHandler = None
        self._documentClosedEventHandler = None
                
    def getName(self):
        return os.path.basename(self._fullPath)
    
    def getPath(self):
        return os.path.dirname(self._fullPath)
    
    def getFullPath(self):
        return self._fullPath
    
    def getEditor(self):
        return self._editor
    
    def setEditor(self, editor):
        if editor is None:
            raise Exception('None object could not be set as editor.')
        
        if isinstance(type(editor), Editor):
            raise Exception('The value of parameter is not Editor type.')
        
        self._editor = editor
        
        self._editor.getContentChangedEventHandler().add(self.__onEditorContentChanged)
        self._editor.getContentSavedEventHandler().add(self.__onEditorContentSaved)
        
    def isContentChanged(self):
        return self._contentChanged
    
    def rename(self, fullPath):
        oldFullPath = self._fullPath
        self._fullPath = fullPath
        self.getDocumentNameChangedEventHandler().invoke(self, (oldFullPath, self.getFullPath()))
        
    def save(self):
        if self.getEditor() is None:
            return    
        self.getEditor().saveFile(self.getFullPath())
        
    def close(self):
        if self._editor is not None:
            self._editor.getContentChangedEventHandler().remove(self.__onEditorContentChanged)
            self._editor.getContentSavedEventHandler().remove(self.__onEditorContentSaved)
            
            self.getDocumentClosedEventHandler().invoke(self, self)  
            
            self._editor.Hide()
            self._editor.Close()
            self._editor = None
    
    def getDocumentChangedEventHandler(self):
        if self._documentChangedEventHandler is None:
            self._documentChangedEventHandler = EventHandler()
        return self._documentChangedEventHandler
    
    def getDocumentSavedEventHander(self):
        if self._documentSavedEventHander is None:
            self._documentSavedEventHander = EventHandler()
        return self._documentSavedEventHander
    
    def getDocumentNameChangedEventHandler(self):
        if self._documentNameChangedEventHandler is None:
            self._documentNameChangedEventHandler = EventHandler()
        return self._documentNameChangedEventHandler
    
    def getDocumentClosedEventHandler(self):
        if self._documentClosedEventHandler is None:
            self._documentClosedEventHandler = EventHandler()
        return self._documentClosedEventHandler
    
    def __onEditorContentChanged(self, sender, evt):
        self._contentChanged = True
        self.getDocumentChangedEventHandler().invoke(self, self)
    
    def __onEditorContentSaved(self, sender, evt):
        self._contentChanged = False
        self.getDocumentSavedEventHander().invoke(self, self)