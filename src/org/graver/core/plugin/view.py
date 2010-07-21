'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx

class View(wx.Panel):
    def __init__(self, parent):
        if self.__class__ is View:
            raise Exception('Cannot instantiate abstract class %s.' % self.__class__)
        wx.Panel.__init__(self, parent)