'''
Created on Jul 15, 2010

@author: tinyshrimp
'''

import wx
from org.graver.core.plugin.pane import Pane

class EditorPane(Pane):
    def __init__(self, parent):
        Pane.__init__(self, parent, 'editorPane', 'Editor', showCaption=False)
        