'''
Created on Jun 9, 2010

@author: tinyshrimp
'''

from org.graver.application import Application
from org.graver.core.actions.action import Action

class UndoAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.undo()
    
    def getStatus(self, selectedView):
        return True
    
class RedoAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.redo()
    
    def getStatus(self, selectedView):
        return True
    
class CopyAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.copy()
    
    def getStatus(self, selectedView):
        return True
    
class PasteAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.paste()
    
    def getStatus(self, selectedView):
        return True
    
class CutAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.cut()
    
    def getStatus(self, selectedView):
        return True
    
class DeleteAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        editor.delete()
    
    def getStatus(self, selectedView):
        return True