'''
Created on Jun 10, 2010

@author: tinyshrimp
'''

class ActionInfo(object):
    def __init__(self, name, clsPath, imagePath, tip='', showInToolbar=True):
        self._name = name
        self._clsPath = clsPath
        self._imagePath = imagePath
        self._tip = tip
        self._showInToolbar = showInToolbar
        