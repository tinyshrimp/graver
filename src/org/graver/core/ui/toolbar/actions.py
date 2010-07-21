'''
Created on Jun 13, 2010

@author: tinyshrimp
'''

from org.graver.core.actions.action import Action
from org.graver.core.ui.toolbar.configDialog import ConfigDialog

class ConfigAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        configDlg = ConfigDialog()
        configDlg.ShowModal()
    
    def getStatus(self, selectedView):
        return True