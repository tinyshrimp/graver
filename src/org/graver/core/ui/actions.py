'''
Created on Jun 8, 2010

@author: tinyshrimp
'''

import wx
from wx.lib.wordwrap import wordwrap

from org.graver.core.actions.action import Action
from org.graver.application import Application

class MainFrameCloseAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        mainFrm = Application.getMainFrame()
        if mainFrm is None:
            return
        mainFrm.Close()
        
    def getStatus(self, selectedView):
        return True
    
class AboutAction(Action):
    def __init__(self):
        Action.__init__(self)
        
    def execute(self, evt):
        info = wx.AboutDialogInfo()
        info.Name = "Graver"
        info.Version = "0.0.1"
#        info.Copyright = "(C) 2006 Programmers and Coders Everywhere"
        info.Description = wordwrap(
            "Graver is a light text editor which created by Python and wxPython.\n"            
            "This text editor implemented plugin interface for developers.\n"
            "Developers could create their own panels, editors, menus and toolbars to extend the function of this editor.\n"
            "In the future, this text editor will be implemented to a lightly IDE.\n",
            350, wx.ClientDC(Application.getMainFrame()))
        info.WebSite = ("http://graver.sourceforge.net", "Graver Home Page")
        info.Developers = [ "Tiny Strimp" ]

#        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
        
    def getStatus(self, selectedView):
        return True