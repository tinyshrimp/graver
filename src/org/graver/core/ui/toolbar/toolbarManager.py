'''
Created on Jun 5, 2010

@author: tinyshrimp
'''

import os
import wx

from org.graver.application import Application

class ToolbarManager(object):
    ICON_SIZE=wx.Size(16, 16)
    
    def __init__(self, window):
        self._window = window
        
        self._toolbars = None
        
    def initializes(self):
        toolbarInfos = Application.getSettings().getToolbars()
        self.__createToolbars(toolbarInfos);
        
    def getToolbars(self):
        if self._toolbars is None:
            self._toolbars = {}
        return self._toolbars
    
    def __createToolbars(self, toolbarInfos):
        if toolbarInfos is None:
            return
        
        id = 0
        for toolbarName in toolbarInfos.keys():
            if not self.getToolbars().has_key(toolbarName):
                toolbarInfo = toolbarInfos.get(toolbarName)
                toolbar = self.__createToolbar(toolbarInfo, 0)
                if toolbar is not None:
                    self.getToolbars()[toolbarName] = toolbar
            
            
    def __createToolbar(self, toolbarInfo, id):
        if toolbarInfo is None:
            return
        
        toolbar = wx.ToolBar(self._window, id, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        
        index = 0
        for itemInfo in toolbarInfo.values():
            itemId = id * 100 + index
            
            if itemInfo.getImage() is None or '' == itemInfo.getImage().strip():
                continue
            
            imagePath = Application.getSettings().getWorkPath() + os.path.sep + itemInfo.getImage()
            bmp = wx.Bitmap(imagePath, wx.BITMAP_TYPE_PNG)
            toolbar.AddLabelTool(itemId, itemInfo.getName(), bmp, longHelp=itemInfo.getTip())
            
            action = Application.getActionManager().getAction(itemInfo.getAction())
            if action is not None:
                toolbar.Bind(wx.EVT_TOOL, action.execute, id=itemId)
            index += 1
            
        if 0 == index:
            return None
        
        toolbar.Realize()
        return toolbar
            
