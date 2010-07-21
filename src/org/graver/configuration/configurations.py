'''
Created on Jun 2, 2010

@author: tinyshrimp
'''
import os

from org.graver.utils.xmlLoader import XmlLoader
from org.graver.core.ui.menu.menuInfo import MenuInfo
from org.graver.core.ui.toolbar.toolbarItemInfo import ToolbarItemInfo
from org.graver.utils.orderedSet import OrderedSet
from org.graver.core.actions.actionGroup import ActionGroup
from org.graver.core.ui.editor.editorStyle import EditorStyle, Font, Indent, Marker, EOL, Edge, Caret, Highlight
from org.graver.core.ui.editor import languages

class Configurations(object):
    def __init__(self, actionManager):
        self._actionManager = actionManager
        
        self._workPath = ''
        self._defaultEditor = ''
        self._editorStyle = None
        self._editors = None
        self._encodings = None
        self._menus = None
        self._toolbars = None
        self._fileAssociations = None
        
    def setWorkPath(self, path):
        self._workPath = path
        
    def getWorkPath(self):
        return self._workPath
    
    def getDefaultEditor(self):
        return self._defaultEditor
    
    def getEditorStyle(self):
        if self._editorStyle is None:
            self._editorStyle = EditorStyle()
        return self._editorStyle
    
    def getEditors(self):
        if self._editors is None:
            self._editors = {}
        return self._editors
    
    def getEncodings(self):
        return self._encodings
    
    def getMenus(self):
        if self._menus is None:
            self._menus = OrderedSet()
        return self._menus
    
    def getToolbars(self):
        if self._toolbars is None:
            self._toolbars = OrderedSet()
        return self._toolbars
        
    def getFileAssociations(self):
        if self._fileAssociations is None:
            self._fileAssociations = {}
        return self._fileAssociations
        
    def load(self):
        configFile = '%s%sconfig%sconfig.xml' % (self.getWorkPath(), os.path.sep, os.path.sep)
        xmlLoader = XmlLoader()
        xmlroot = xmlLoader.load(configFile)
        
        if xmlroot is None:
            raise Exception('Failed to load config file.\n%s' % configFile)
        
        for config in xmlroot.getChildren():
            for setting in config.getChildren():
                if 'editors' == setting.getName().lower():
                    self.__parseEditorsSettings(setting)
                elif 'encodings' == setting.getName().lower():
                    self.__parseEncodingSettings(setting)
                elif 'actions' == setting.getName().lower():
                    self.__parseActionsSettings(setting)
                elif 'appearance' == setting.getName().lower():
                    self.__parseAppearanceSettings(setting)
            
    def __parseEditorsSettings(self, editors):
        for editor in editors.getChildren():
            if 'default' == editor.getName().lower():                
                self._defaultEditor = '%s.%s:%s' % (editor.getAttrs()['package'], editor.getAttrs()['module'], editor.getAttrs()['class'])
            else:
                editorName = editor.getAttrs()['name']
                classPath = '%s.%s:%s' % (editor.getAttrs()['package'], editor.getAttrs()['module'], editor.getAttrs()['class'])
                pattern = editor.getAttrs()['pattern']
                if self.getEditors().has_key(editorName):
                    pass # write log here. the editor name is  duplicated.
                self.getEditors()[editorName] = (classPath, pattern) 
                
    def __parseEncodingSettings(self, encodings):
        if encodings is None:
            return
        
        encodinglist = encodings.getAttrs()['value']
        self._encodings = encodinglist.split(',')
                
    def __parseActionsSettings(self, actions):
        if actions is None:
            return
        
        menuInfo = None
        toolbar = None        
        
        actionGroupName = actions.getAttrs()['name']  
            
        shouldCreateToolbar = True
        try:
            createToolbar = actions.getAttrs()['createtoolbar']
            if createToolbar is not None and createToolbar.lower() == 'false':
                shouldCreateToolbar = False
        except KeyError:
            pass
        
        '''gets or creates toolbar'''
        if shouldCreateToolbar:
            if self.getToolbars().has_key(actionGroupName):
                toolbar = self.getToolbars().get(actionGroupName)
            else:
                toolbar = OrderedSet()
                self.getToolbars().put(actionGroupName, toolbar)
            
        ''' creates action group '''
        actionGroup = ActionGroup(actionGroupName, shouldCreateToolbar)
        
        separatorCnt = 0
        for setting in actions.getChildren():
            if 'menu' == setting.getName():
                menuPath = setting.getAttrs()['path']
                menuInfo = self.__createMenuInfoTree(menuPath)
                if 0 < menuInfo.getChildren().length():
                    separatorMenuItem = MenuInfo('-', '', '', '')
                    menuInfo.getChildren().put(actionGroupName, separatorMenuItem)
            elif 'action' == setting.getName():
                actionName = setting.getAttrs()['name']
                package = setting.getAttrs()['package']
                module = setting.getAttrs()['module']
                cls = setting.getAttrs()['class']
                imagePath = setting.getAttrs()['image']
                tip = setting.getAttrs()['tip']
                
                ''' adds action '''
                clsPath = '%s.%s:%s' % (package, module, cls)
                actionGroup.getActions()[actionName] = (clsPath, None)                
                
                name = '%s.%s' % (actionGroupName, actionName)
                
                '''create menu item'''
                actionMenuItem = MenuInfo(actionName, imagePath, tip, name)
                menuInfo.getChildren().put(actionName, actionMenuItem)
                
                '''create toolbar item'''
                if shouldCreateToolbar:
                    actionToolbarItem = ToolbarItemInfo(actionName, name, imagePath, tip)
                    toolbar.put(actionName, actionToolbarItem)
            elif 'separator' == setting.getName():
                actionMenuItem = MenuInfo('-', '', '', '')
                menuInfo.getChildren().put('%s_separator_%d' % (actionGroupName, separatorCnt), actionMenuItem)
                separatorCnt += 1
        
        self._actionManager.getActionGroups()[actionGroupName] = actionGroup
        
        if shouldCreateToolbar:
            self.getToolbars().put(actionGroupName, toolbar)
                
    def __createMenuInfoTree(self, path):
        if path is None or '' == path:
            return None
        
        menuNames = path.split(':')
        
        curMenu = None
        for menuName in menuNames:
            if curMenu is None:
                if self.getMenus().has_key(menuName):
                    curMenu = self.getMenus().get(menuName)
                else:
                    curMenu = MenuInfo(menuName)
                    self.getMenus().put(menuName, curMenu)
            else:
                if curMenu.getChildren().has_key(menuName):
                    curMenu = curMenu.get(menuName)
                else:
                    menuInfo = MenuInfo(menuName)
                    curMenu.getChildren().pug(menuName, menuInfo)
                    curMenu = menuInfo
                    
        return curMenu
            
    def __parseAppearanceSettings(self, appearance):
        if appearance is None:
            return
        
        for setting in appearance.getChildren():
            if setting is None or setting.getName() is None or '' == setting.getName():
                continue
            
            if 'font' == setting.getName().lower():
                font = self.__createFontBySetting(setting)
                if font is None:
                    continue
                self.getEditorStyle().setFont(font)
            elif 'indent' == setting.getName().lower():
                indent = self.__createIndentBySetting(setting)
                if indent is None:
                    continue
                self.getEditorStyle().setIndent(indent)
            elif 'marker' == setting.getName().lower():
                marker = self.__createMarkerBySetting(setting)
                if marker is None:
                    continue
                self.getEditorStyle().setMarker(marker)
            elif 'eol' == setting.getName().lower():
                eol = self.__createEOLBySetting(setting)
                if eol is None:
                    continue
                self.getEditorStyle().setEOL(eol)
            elif 'edge' == setting.getName().lower():
                edge = self.__createEdgeBySetting(setting)
                if edge is None:
                    continue
                self.getEditorStyle().setEdge(edge)
            elif 'caret' == setting.getName().lower():
                caret = self.__createCaretBySetting(setting)
                if caret is None:
                    continue
                self.getEditorStyle().setCaret(caret)
            elif 'highlight' == setting.getName().lower():
                self.__createHighlightBySetting(setting)
    
    def __createFontBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        fontName = ''
        if attrs.has_key('name'):
            fontName = attrs['name']
            
        fontSize = ''
        if attrs.has_key('size'):
            fontSize = attrs['size']
            
        fgColor = ''
        if attrs.has_key('fgcolor'):
            fgColor = attrs['fgcolor']
            
        bgColor = ''
        if attrs.has_key('bgcolor'):
            bgColor = attrs['bgcolor']
            
        bold = ''
        if attrs.has_key('bold'):
            bold = attrs['bold']
            
        underline = ''
        if attrs.has_key('underline'):
            underline = attrs['underline']
            
        return Font(fontName, fontSize, fgColor, bgColor, bold, underline)
    
    def __createIndentBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        size = ''
        if attrs.has_key('size'):
            size = attrs['size']
            
        showIndentGuide = ''
        if attrs.has_key('showindetguide'):
            showIndentGuide = attrs['showindentguide']
            
        backspaceUnindents = ''
        if attrs.has_key('backspaceunindents'):
            backspaceUnindents = attrs['backspaceunindents']
            
        tabIndents = ''
        if attrs.has_key('tabindents'):
            tabIndents = attrs['tabindents']
            
        tabWidth = ''
        if attrs.has_key('tabwidth'):
            tabWidth = attrs['tabwidth']
            
        useTabs = ''
        if attrs.has_key('usetabs'):
            useTabs = attrs['usetabs']
            
        viewWhitespace = ''
        if attrs.has_key('viewwhitespace'):
            viewWhitespace = attrs['viewwhitespace']
            
        return Indent(size, tabWidth, showIndentGuide, backspaceUnindents, tabIndents, useTabs, viewWhitespace)
    
    def __createMarkerBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        style = ''
        if attrs.has_key('style'):
            style = attrs['style']
            
        fgColor = ''
        if attrs.has_key('fgcolor'):
            fgColor = attrs['fgcolor']
            
        bgColor = ''
        if attrs.has_key('bgcolor'):
            bgColor = attrs['bgcolor']
            
        return Marker(style, fgColor, bgColor)
    
    def __createEOLBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        showEOL = ''
        if attrs.has_key('showeol'):
            showEOL = attrs['showeol']
            
        return EOL(showEOL)
        
    def __createEdgeBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        maxColumns = ''
        if attrs.has_key('maxcolumns'):
            maxColumns = attrs['maxcolumns']
            
        return Edge(maxColumns)
    
    def __createCaretBySetting(self, setting):
        if setting is None:
            return None
        
        attrs = setting.getAttrs()
        
        color = ''
        if attrs.has_key('color'):
            color = attrs['color']
            
        return Caret(color)
    
    def __createHighlightBySetting(self, setting):
        if setting is None:
            return
        
        for language in setting.getChildren():
            if language is None or language.getName() is None or '' == language.getName():
                continue
            
            languageName = language.getName().lower().strip()
            if not languages.LANGUAGE_MAP.has_key(languageName):
                continue
            lexer = languages.LANGUAGE_MAP[languageName]
            
            ''' gets path of style file '''
            if language.getAttrs().has_key('style'):
                styleFilePath = language.getAttrs()['style'].strip()
                if '' == styleFilePath:
                    continue
                styleFilePath = "%s%s..%s..%s..%s%s" % (os.path.dirname(__file__), os.path.sep, os.path.sep, os.path.sep, os.path.sep, styleFilePath)
                if not os.path.exists(styleFilePath):
                    continue
                
                styleSettings = XmlLoader().load(styleFilePath)
                if styleSettings is None:
                    continue
                
                highlightStyle = Highlight()
                for setting in styleSettings.getChildren():
                    if setting is None or '' == setting.getName():
                        continue
                    if 'keywords' == setting.getName():
                        keywords = setting.getCharData().strip()
                        if '' != keywords:
                            highlightStyle.setKeywords(keywords)
                    elif 'styles' == setting.getName():
                        for mode in setting.getChildren():
                            if mode is None or mode.getName() is None or '' == mode.getName():
                                continue
                            font = self.__createFontBySetting(mode)
                            highlightStyle.getHighlightStyles()[mode.getName().lower().strip()] = font
            
                self.getEditorStyle().getHighlightStyles()[lexer] = highlightStyle
            
            
                