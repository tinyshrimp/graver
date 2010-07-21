'''
Created on Jun 2, 2010

@author: tinyshrimp
'''

from org.graver.configuration.configurations import Configurations
from org.graver.core.documents.documentManager import DocumentManager
from org.graver.core.plugin.pluginManager import PluginManager
from org.graver.core.actions.actionManager import ActionManager

class Application(object):
    __mainFrame = None
    __settings = None
    __documentManager = None
    __pluginManager = None
    __actionManager = None
    
    @staticmethod
    def setMainFrame(mainFrame):
        Application.__mainFrame = mainFrame
    
    @staticmethod
    def getMainFrame():
        return Application.__mainFrame
    
    @staticmethod
    def getSettings():
        if Application.__settings is None:
            Application.__settings = Configurations(Application.getActionManager())
        return Application.__settings
    
    @staticmethod
    def getDocumentManager():
        if Application.__documentManager is None:
            Application.__documentManager = DocumentManager()
        return Application.__documentManager
    
    @staticmethod
    def getPluginManager():
        if Application.__pluginManager is None:
            Application.__pluginManager = PluginManager()
        return Application.__pluginManager
    
    @staticmethod
    def getActionManager():
        if Application.__actionManager is None:
            Application.__actionManager = ActionManager()
        return Application.__actionManager
    
        