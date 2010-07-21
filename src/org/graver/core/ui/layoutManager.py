'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx
from wx import aui

class LayoutManager(object):
    def __init__(self, window):
        self._panes = None
        self._toolbars = None
        
        self._auiMgr = aui.AuiManager(window)
        self._auiMgr.Update()
        
    def getPanes(self):
        if self._panes is None:
            self._panes = {}
        return self._panes
    
    def getToolbars(self):
        if self._toolbars is None:
            self._toolbars = {}
        return self._toolbars
    
    def clear(self):
        for pane in self.getPanes().values():
            if pane is None:
                continue
            self._auiMgr.DetachPane(pane)
            
        for toolbar in self.getToolbars().values():
            if toolbar is None:
                continue
            self._auiMgr.DetachPane(toolbar)
        
    def addPane(self, pane):
        if pane is None or pane.getName() is None or '' == pane.getName():
            return False
        
        if not self.getPanes().has_key(pane.getName()):
            self.getPanes()[pane.getName()] = pane
            
        paneInfo = self.__createAuiPaneInfo(pane.getName(), pane.getCaption(), pane.getPosition(), pane.isShowCaption())
        self._auiMgr.AddPane(pane, paneInfo)
        self._auiMgr.Update()
        
        return True
        
    def removePane(self, name):
        if not self.getPanes().has_key(name):
            return
        
        pane = self.getPanes()[name]
        self._auiMgr.DetachPane(pane)
        
    def addToolbar(self, name, toolbar):
        if toolbar is None or name is None or '' == name:
            return False
        
        if not self.getToolbars().has_key(name):
            self.getToolbars()[name] = toolbar
            
        auiInfo = self.__createAuiToolbarInfo(name)
        self._auiMgr.InsertPane(toolbar, auiInfo)
        self._auiMgr.Update()
        
        return True
        
    def removeToolbar(self, name):
        if not self.getToolbars().has_key(name):
            return
        
        toolbar = self.getToolbars().pop(name)
        toolbar.Hide()
        self._auiMgr.DetachPane(toolbar)
        self._auiMgr.Update()
    
    def __createAuiToolbarInfo(self, name):
        return aui.AuiPaneInfo().Name(name).CaptionVisible(False).MaximizeButton(False).CloseButton(False).ToolbarPane().Top().Row(1).LeftDockable(False).RightDockable(False).BottomDockable(True)
        
    def __createAuiPaneInfo(self, name, caption, pos, showCaption):        
        auiPaneInfo = aui.AuiPaneInfo()
    
        ''' set pane name '''
        auiPaneInfo = auiPaneInfo.Name(name)
    
        ''' set pane caption '''
        if showCaption:
            auiPaneInfo = auiPaneInfo.Caption(caption)
        else:
            auiPaneInfo = auiPaneInfo.CaptionVisible(showCaption)
    
        ''' set show maximize button '''
        auiPaneInfo = auiPaneInfo.MaximizeButton(True)
    
        ''' set show close button '''
        auiPaneInfo = auiPaneInfo.CloseButton(True)
    
        ''' set pane location '''
        if pos == wx.LEFT:
            auiPaneInfo = auiPaneInfo.Left()
        elif pos == wx.RIGHT:
            auiPaneInfo = auiPaneInfo.Right()
        elif pos == wx.TOP:
            auiPaneInfo = auiPaneInfo.Top()
        elif pos == wx.BOTTOM:
            auiPaneInfo = auiPaneInfo.Bottom()
        else:
            auiPaneInfo = auiPaneInfo.Center()
    
        # set pan size
        auiPaneInfo = auiPaneInfo.BestSize(wx.Size(200,200))
    
        return auiPaneInfo