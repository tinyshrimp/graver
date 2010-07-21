'''
Created on Jul 15, 2010

@author: tinyshrimp
'''

from org.graver.core.actions.action import Action
from org.graver.configuration.preferencesDialog import PreferencesDialog

class PreferencesAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        configDlg = PreferencesDialog()
        configDlg.ShowModal()
    
    def getStatus(self, selectedView):
        return True
        