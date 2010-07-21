'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

from org.graver.core.documents.document import Document
from org.graver.utils.eventHandler import EventHandler

class DocumentManager(object):
    def __init__(self):
        self._documents = None # key: full path of document; value: a Document object
        self._currentDoc = None
        
        self._documentOpenedEventHandler = None
        self._documentClosedEventHandler = None
        self._documentChangedEventHandler = None
        self._documentSavedEventHandler = None
        self._documentRenamedEventHandler = None
        self._selectedDocumentChangedEventHandler = None
        
    def getDocuments(self):
        if self._documents is None:
            self._documents = {}
        return self._documents
    
    def getCurrentDocument(self):
        return self._currentDoc
        
    def openDocument(self, fullPath):
        if self.getDocuments().has_key(fullPath):
            self.selectDocument(fullPath)
        else:
            document = Document(fullPath)
            self.getDocuments()[fullPath] = document
            
            document.getDocumentChangedEventHandler().add(self.__onDocumentChanged)
            document.getDocumentNameChangedEventHandler().add(self.__onDocumentNameChanged)
            document.getDocumentSavedEventHander().add(self.__onDocumentSaved)
            document.getDocumentClosedEventHandler().add(self.__onDocumentClosed)
            
            self.getDocumentOpenedEventHandler().invoke(self, document)
            
    def closeDocument(self, fullPath):
        if not self.getDocuments().has_key(fullPath):
            return
        document = self.getDocuments()[fullPath]
        if self.getCurrentDocument() == document:
            self._currentDoc = None
        document.close()
            
    def selectDocument(self, fullPath):
        if fullPath is None:
            return
        
        if self.getCurrentDocument() is not None and fullPath == self.getCurrentDocument().getName():
            return
        
        if not self.getDocuments().has_key(fullPath):
            return
        self._currentDoc = self.getDocuments()[fullPath]
        self.getSelectedDocumentChangedEventHandler().invoke(self, self.getCurrentDocument())
        
    def getDocumentChangedEventHandler(self):
        if self._documentChangedEventHandler is None:
            self._documentChangedEventHandler = EventHandler()
        return self._documentChangedEventHandler
    
    def getDocumentSavedEventHandler(self):
        if self._documentSavedEventHandler is None:
            self._documentSavedEventHandler = EventHandler()
        return self._documentSavedEventHandler
    
    def getDocumentOpenedEventHandler(self):
        if self._documentOpenedEventHandler is None:
            self._documentOpenedEventHandler = EventHandler()
        return self._documentOpenedEventHandler
    
    def getDocumentClosedEventHandler(self):
        if self._documentClosedEventHandler is None:
            self._documentClosedEventHandler = EventHandler()
        return self._documentClosedEventHandler
    
    def getSelectedDocumentChangedEventHandler(self):
        if self._selectedDocumentChangedEventHandler is None:
            self._selectedDocumentChangedEventHandler = EventHandler()
        return self._selectedDocumentChangedEventHandler
    
    def getDocumentRenamedEventHandler(self):
        if self._documentRenamedEventHandler is None:
            self._documentRenamedEventHandler = EventHandler()
        return self._documentRenamedEventHandler        
    
    def __onDocumentChanged(self, sender, evt):
        self.getDocumentChangedEventHandler().invoke(sender, evt)
        
    def __onDocumentNameChanged(self, sender, evt):
        oldName, newName = evt
        document = self.getDocuments().pop(oldName)
        self.getDocuments()[newName] = document
        self.getDocumentRenamedEventHandler().invoke(sender, evt)
        
    def __onDocumentSaved(self, sender, evt):
        self.getDocumentSavedEventHandler().invoke(sender, evt)
        
    def __onDocumentClosed(self, sender, evt):      
        document = evt
        if document is None:
            return
          
        fullPath = document.getFullPath()
        if self.getDocuments().has_key(fullPath):
            document = self.getDocuments().pop(fullPath)
            if self.getCurrentDocument() == document:
                self._currentDoc = None
        self.getDocumentClosedEventHandler().invoke(sender, evt)
        
        