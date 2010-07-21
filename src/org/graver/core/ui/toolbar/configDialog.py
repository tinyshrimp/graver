'''
Created on Jun 13, 2010

@author: tinyshrimp
'''

import wx

from org.graver.application import Application

class ConfigDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Toolbar Settings', size=(500, 300), style=wx.DEFAULT_DIALOG_STYLE)
        self.__initializeComponents()
        
    def __initializeComponents(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        toolbars = Application.getMainFrame().getToolbarManager().getToolbars()
        shownToolbars = Application.getMainFrame().getLayoutManager().getToolbars()
        
        self._toolbarListBox = wx.CheckListBox(self, -1, choices=toolbars.keys())
        
        index = 0
        indexes = []
        for toolbarName in toolbars.keys():
            if shownToolbars.has_key(toolbarName):
                indexes.append(index)
            index += 1
        self._toolbarListBox.SetChecked(indexes)            
        
        sizer.Add(self._toolbarListBox, 0, wx.EXPAND | wx.ALL, 5)
        
        self.Bind(wx.EVT_CHECKLISTBOX, self.__checkChanged, self._toolbarListBox)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
    def __checkChanged(self, evt):
        index = evt.GetSelection()
        label = self._toolbarListBox.GetString(index)
        
        isChecked = False
        if self._toolbarListBox.IsChecked(index):
            isChecked = True
            
        shownToolbars = Application.getMainFrame().getLayoutManager().getToolbars()
            
        toolbars = Application.getMainFrame().getToolbarManager().getToolbars()
        if not toolbars.has_key(label):
            return
        
        toolbar = toolbars[label]
        if toolbar is None:
            return
        
        if isChecked:
            if shownToolbars.has_key(label):
                return
            Application.getMainFrame().getLayoutManager().addToolbar(label, toolbar)
        else:
            if not shownToolbars.has_key(label):
                return
            Application.getMainFrame().getLayoutManager().removeToolbar(label)
        
            
        
        
    