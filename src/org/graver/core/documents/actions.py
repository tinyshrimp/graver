'''
Created on Jun 4, 2010

@author: tinyshrimp
'''

import os
import wx

from org.graver.application import Application
from org.graver.core.actions.action import Action

class NewFileAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        Application.getDocumentManager().openDocument('')
    
    def getStatus(self, selectedView):
        return True
    
class OpenFileAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        wildcard = "All files (*.*)|*"
        dlg = wx.FileDialog(None, message='Open File', defaultDir='', defaultFile='',
                            wildcard=wildcard, style=wx.OPEN | wx.CHANGE_DIR | wx.MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            files = dlg.GetPaths()
            for file in files:
                Application.getDocumentManager().openDocument(file)
    
    def getStatus(self, selectedView):
        return True
    
class SaveFileAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        if document.getFullPath() is None or '' == document.getFullPath():
            wildcard = "All files (*.*)|*"
            dlg = wx.FileDialog(None, message='Save file as ...',
                                 defaultDir = os.getcwd(),
                                 defaultFile='',
                                 wildcard=wildcard,
                                 style=wx.SAVE | wx.CHANGE_DIR)
            if dlg.ShowModal() == wx.ID_OK:
                document.rename(dlg.GetPath())        
        document.save()
    
    def getStatus(self, selectedView):
        return True
    
class SaveFileAsAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        wildcard = "All files (*.*)|*"
        dlg = wx.FileDialog(None, message='Save file as ...',
                             defaultDir = os.getcwd(),
                             defaultFile='',
                             wildcard=wildcard,
                             style=wx.SAVE | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            document.rename(dlg.GetPath())
            document.save()
    
    def getStatus(self, selectedView):
        return True
    
class CloseFileAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        document = Application.getDocumentManager().getCurrentDocument()
        if document is None:
            return
        
        if document.isContentChanged():
            if wx.MessageDialog(None, 'Do you want to save file: %s?' % document.getName(), 
                                'Warning', wx.YES | wx.NO | wx.ICON_WARNING).ShowModal() == wx.ID_YES:
                saveAction = Application.getActionManager().getAction('DocumentActions.Save')
                if saveAction is not None:
                    saveAction.execute(None)
        document.close()
        
    def getStatus(self, selectedView):
        return True
    
class CloseAllFileAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        while 0 < len(Application.getDocumentManager().getDocuments()):
            document = Application.getDocumentManager().getCurrentDocument()
            if document is None:
                continue
            
            if document.isContentChanged():
                if wx.MessageDialog(None, 'Do you want to save file: %s?' % document.getName(), 
                                    'Warning', wx.YES | wx.NO | wx.ICON_WARNING).ShowModal() == wx.ID_YES:
                    saveAction = Application.getActionManager().getAction('DocumentActions.Save')
                    if saveAction is not None:
                        saveAction.execute(None)
            document.close()