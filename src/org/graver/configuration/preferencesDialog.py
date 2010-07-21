'''
Created on Jul 15, 2010

@author: tinyshrimp
'''

import wx

from org.graver.configuration.panes.fontAndColorPane import FontAndColorPane
from org.graver.configuration.panes.highlightPane import HighlightPane
from org.graver.configuration.panes.encodingPane import EncodingPane
from org.graver.configuration.panes.editorPane import EditorPane

class PreferencesDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Preferences', size=(800, 600), style=wx.DEFAULT_DIALOG_STYLE)
        self._treebook = None
        self.__initializeComponents()
        
    def __initializeComponents(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._treebook = wx.Treebook(self, -1)
        self.__initializeTreebook()
        sizer.Add(self._treebook, -1, wx.EXPAND | wx.ALL, 5)        
        
        self.SetSizer(sizer)
        
    def __initializeTreebook(self):
        ''' adds appearance setting group '''
        self._treebook.AddPage(wx.Panel(self._treebook), 'Appearance                      ')
        
        fontAndColorPane = FontAndColorPane(self._treebook)
        self._treebook.AddSubPage(fontAndColorPane, 'Font and Colors')
        
        highlightPane = HighlightPane(self._treebook)
        self._treebook.AddSubPage(highlightPane, 'Highlight')
        
        encodingPane = EncodingPane(self._treebook)
        self._treebook.AddSubPage(encodingPane, 'Encodings')
        
        ''' adds editors setting group '''
        editorPane = EditorPane(self._treebook)
        self._treebook.AddPage(editorPane, 'Editors')
        
        
        