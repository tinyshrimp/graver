'''
Created on Jun 4, 2010

@author: tinyshrimp
'''

import wx

from org.graver.application import Application

class MenuManager(object):
    def __init__(self, window):
        self._window = window
        self._menubar = None
        
    def initialize(self):
        menuInfos = Application.getSettings().getMenus()
        self.__createMenus(menuInfos)
        self._window.SetMenuBar(self.__getMenubar())
        
    def __getMenubar(self):
        if self._menubar is None:
            self._menubar = wx.MenuBar()
        return self._menubar
        
    def __createMenus(self, menuInfos):
        if menuInfos is None or 0 >= len(menuInfos.keys()):
            return
        
        helpMenuInfo = None
        for menuInfo in menuInfos.values():
            if 'help' != menuInfo.getName().lower():
                self.__createMenu(menuInfo, self.__getMenubar())
            else:
                helpMenuInfo = menuInfo
                
        if helpMenuInfo is not None:
            self.__createMenu(helpMenuInfo, self.__getMenubar())
    
    def __createMenu(self, menuInfo, parentMenu):
        menu = None
        if parentMenu == self.__getMenubar() or 0 < len(menuInfo.getChildren().keys()):
            menu = wx.Menu()
            self.__getMenubar().Append(menu, menuInfo.getName())
        else:
            if '-' == menuInfo.getName():
                parentMenu.AppendSeparator()
            else:
                menu = parentMenu.Append(-1, menuInfo.getName(), menuInfo.getTip())
            
        if menuInfo.getAction() is not None and '' != menuInfo.getAction():
            action = Application.getActionManager().getAction(menuInfo.getAction())
            if action is not None:
                self._window.Bind(wx.EVT_MENU, action.execute, menu)
            
        for sub in menuInfo.getChildren().values():
            self.__createMenu(sub, menu)
            