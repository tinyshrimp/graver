'''
Created on Jul 15, 2010

@author: tinyshrimp
'''

import wx
from org.graver.core.plugin.pane import Pane

class HighlightPane(Pane):
    def __init__(self, parent):
        Pane.__init__(self, parent, 'highlightPane', 'Highlight', showCaption=False)
        