'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx

from org.graver.application import Application
from org.graver.core.ui.layoutManager import LayoutManager
from org.graver.core.ui.menu.menuManager import MenuManager
from org.graver.core.ui.toolbar.toolbarManager import ToolbarManager
from org.graver.core.ui.editor.editorContainer import EditorContainer

class MainFrame(wx.Frame):
    def __init__(self, caption, displaySize=wx.DefaultSize, position=wx.DefaultPosition):
        wx.Frame.__init__(self, None, -1, title=caption, pos=position, size= displaySize)
        
        self._layoutManager = None
        self._menuManager = None
        self._toolbarManager = None
        self._layoutManager = None
        
        self.initializes()
        
        self.Bind(wx.EVT_CLOSE, self.__onClose)
        
    def initializes(self):
        ''' init menus '''
        self.getMenuManager().initialize()
        
        ''' init toolbars '''
        self.getToolbarManager().initializes()
        for toolbarName in self.getToolbarManager().getToolbars().keys():
            toolbar = self.getToolbarManager().getToolbars()[toolbarName]
            self.getLayoutManager().addToolbar(toolbarName, toolbar)
        
        ''' adds editor container to frame '''
        editorContainer = EditorContainer(self)
        self._layoutManager.addPane(editorContainer)
        
    def getLayoutManager(self):
        if self._layoutManager is None:
            self._layoutManager = LayoutManager(self)
        return self._layoutManager
    
    def getMenuManager(self):
        if self._menuManager is None:
            self._menuManager = MenuManager(self)
        return self._menuManager
    
    def getToolbarManager(self):
        if self._toolbarManager is None:
            self._toolbarManager = ToolbarManager(self)
        return self._toolbarManager
    
    def __onClose(self, evt):
        ''' close all documents '''
        closeAllFileAction = Application.getActionManager().getAction('DocumentActions.Close All')
        if closeAllFileAction is not None:
            closeAllFileAction.execute(None)
            
        ''' close all panes '''
        self.getLayoutManager().clear()
        
        ''' destroy frame '''
        self.Destroy()
        