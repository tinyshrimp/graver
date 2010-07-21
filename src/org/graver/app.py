'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx

from org.graver.application import Application
from org.graver.core.ui.mainframe import MainFrame

class App(wx.App):
    def __init__(self, workPath):
        wx.App.__init__(self)
        Application.getSettings().setWorkPath(workPath)
        
    def initApp(self, argv):
        self.initData(argv)
        self.initUI(argv)
        
        Application.getMainFrame().Show(True)
        
    def initData(self, argv):
        '''init configurations'''
        Application.getSettings().load()
        
        '''init document manager'''
        
        '''init plugin manager'''
        
    def initUI(self, argv):
        mainfrm = MainFrame('Graver', displaySize=(800,600))
        self.SetTopWindow(mainfrm)
        Application.setMainFrame(mainfrm)
    
    def start(self):
        self.MainLoop()
        