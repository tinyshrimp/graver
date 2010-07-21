'''
Created on Jun 14, 2010

@author: tinyshrimp
'''

import wx.stc as stc

class EditorStyle(object):    
    MARKER_STYLES = {'arrowPoint':{stc.STC_MARKNUM_FOLDEROPEN:stc.STC_MARK_ARROWDOWN,
                                   stc.STC_MARKNUM_FOLDER:stc.STC_MARK_ARROW,
                                   stc.STC_MARKNUM_FOLDERSUB:stc.STC_MARK_EMPTY,
                                   stc.STC_MARKNUM_FOLDERTAIL:stc.STC_MARK_EMPTY,
                                   stc.STC_MARKNUM_FOLDEREND:stc.STC_MARK_EMPTY,
                                   stc.STC_MARKNUM_FOLDEROPENMID:stc.STC_MARK_EMPTY,
                                   stc.STC_MARKNUM_FOLDERMIDTAIL:stc.STC_MARK_EMPTY},
                     'plus':{stc.STC_MARKNUM_FOLDEROPEN:stc.STC_MARK_MINUS,
                             stc.STC_MARKNUM_FOLDER:stc.STC_MARK_PLUS,
                             stc.STC_MARKNUM_FOLDERSUB:stc.STC_MARK_EMPTY,
                             stc.STC_MARKNUM_FOLDERTAIL:stc.STC_MARK_EMPTY,
                             stc.STC_MARKNUM_FOLDEREND:stc.STC_MARK_EMPTY,
                             stc.STC_MARKNUM_FOLDEROPENMID:stc.STC_MARK_EMPTY,
                             stc.STC_MARKNUM_FOLDERMIDTAIL:stc.STC_MARK_EMPTY},
                     'circular':{stc.STC_MARKNUM_FOLDEROPEN:stc.STC_MARK_CIRCLEMINUS,
                                 stc.STC_MARKNUM_FOLDER:stc.STC_MARK_CIRCLEMINUS,
                                 stc.STC_MARKNUM_FOLDERSUB:stc.STC_MARK_VLINE,
                                 stc.STC_MARKNUM_FOLDERTAIL:stc.STC_MARK_LCORNERCURVE,
                                 stc.STC_MARKNUM_FOLDEREND:stc.STC_MARK_CIRCLEPLUSCONNECTED,
                                 stc.STC_MARKNUM_FOLDEROPENMID:stc.STC_MARK_CIRCLEMINUSCONNECTED,
                                 stc.STC_MARKNUM_FOLDERMIDTAIL:stc.STC_MARK_TCORNERCURVE},
                     'square':{stc.STC_MARKNUM_FOLDEROPEN:stc.STC_MARK_BOXMINUS,
                               stc.STC_MARKNUM_FOLDER:stc.STC_MARK_BOXPLUS,
                               stc.STC_MARKNUM_FOLDERSUB:stc.STC_MARK_VLINE,
                               stc.STC_MARKNUM_FOLDERTAIL:stc.STC_MARK_LCORNER,
                               stc.STC_MARKNUM_FOLDEREND:stc.STC_MARK_BOXPLUSCONNECTED,
                               stc.STC_MARKNUM_FOLDEROPENMID:stc.STC_MARK_BOXMINUSCONNECTED,
                               stc.STC_MARKNUM_FOLDERMIDTAIL:stc.STC_MARK_TCORNER}}
    
    def __init__(self):
        self._font = None
        self._indent = None
        self._marker = None
        self._eol = None
        self._edge = None
        self._caret = None
        self._highlight = None
        
    def getFont(self):
        if self._font is None:
            return Font()
        return self._font
    
    def setFont(self, font):
        self._font = font
    
    def getIndent(self):
        if self._indent is None:
            return Indent()
        return self._indent
    
    def setIndent(self, indent):
        self._indent = indent
    
    def getMarker(self):
        if self._marker is None:
            return Marker()
        return self._marker
    
    def setMarker(self, marker):
        self._marker = marker
    
    def getEOL(self):
        if self._eol is None:
            return EOL()
        return self._eol
    
    def setEOL(self, eol):
        self._eol = eol
    
    def getEdge(self):
        if self._edge is None:
            return Edge()
        return self._edge
    
    def setEdge(self, edge):
        self._edge = edge
    
    def getCaret(self):
        if self._caret is None:
            return Caret()
        return self._caret
    
    def setCaret(self, caret):
        self._caret = caret
    
    def getHighlightStyles(self):
        if self._highlight is None:
            self._highlight = {}
        return self._highlight
    
class Font(object):
    def __init__(self, name='Monospace', size='8', fgColor='#000000', bgColor='#ffffff', bold='False', underline='False'):
        self._name = name
        self._size = size
        self._fgColor = fgColor
        self._bgColor = bgColor
        self._bold = bold
        self._underline = underline
        
    def getName(self):
        if self._name is None or '' == self._name:
            return 'Monospace'
        return self._name
    
    def getSize(self):
        if self._size is None or '' == self._size.strip():
            return '8'
        return self._size
    
    def getFgColor(self):
        if self._fgColor is None or '' == self._fgColor.strip():
            return '#000000'
        return self._fgColor
    
    def getBgColor(self):
        if self._bgColor is None or '' == self._bgColor.strip():
            return '#ffffff'
        return self._bgColor
    
    def getBold(self):
        if self._bold is None:
            return ''
        if 'true' == self._bold.lower():
            return 'bold'
        return ''
    
    def getUnderline(self):
        if self._underline is None:
            return ''
        if 'true' == self._underline.lower():
            return 'underline'
        return ''
    
    def getSettings(self):
        return 'face:%s,size:%s,fore:%s,back:%s,%s,%s' % (self.getName(), self.getSize(), self.getFgColor(), self.getBgColor(), self.getBold(), self.getUnderline())
        
class Indent(object):
    def __init__(self, size='4', tabWidth='4', showIndentGuide='True', backspaceUnindents='True', tabIndents='True', useTabs='False', viewWhitespace='False'):
        self._size = size
        self._tabWidth = tabWidth
        self._showIndentGuide = showIndentGuide
        self._backspaceUnindents = backspaceUnindents
        self._tabIndents = tabIndents
        self._useTabs = useTabs
        self._viewWhitespace = viewWhitespace
        
    def getSize(self):
        if self._size is None or '' == self._size:
            return 4
        try:
            return int(self._size)
        except ValueError:
            return 4
    
    def getTabWidth(self):
        if self._size is None or '' == self._tabWidth:
            return 4
        try:
            return int(self._tabWidth)
        except ValueError:
            return 4
    
    def getShowIndentGuide(self):
        if self._showIndentGuide is None:
            return False
        if 'true' == self._showIndentGuide.lower():
            return True 
        return False
    
    def getBackspaceUnindents(self):
        if self._backspaceUnindents is None or '' == self._backspaceUnindents:
            return 4
        try:
            return int(self._backspaceUnindents)
        except ValueError:
            return 4
    
    def getTabIndes(self):
        if self._tabIndents is None or '' == self._tabIndents:
            return 4
        try:
            return int(self._tabIndents)
        except ValueError:
            return 4
    
    def getUseTabs(self):
        if self._useTabs is None:
            return False
        if 'true' == self._useTabs.lower():
            return True 
        return False
    
    def getViewWhitespace(self):
        if self._viewWhitespace is None:
            return False
        if 'true' == self._viewWhitespace.lower():
            return True 
        return False
        
class Marker(object):
    def __init__(self, style='square', fgColor='#000000', bgColor='#ffffff'):
        self._style = style
        self._fgColor = fgColor
        self._bgColor = bgColor
        
    def getStyle(self):
        if self._style is None or '' == self._style:
            return 'square'
        if EditorStyle.MARKER_STYLES.has_key(self._style):
            return self._style
        else:
            return 'square'
    
    def getFgColor(self):
        if self._fgColor is None or '' == self._fgColor:
            return '#000000'
        return self._fgColor
    
    def getBgColor(self):
        if self._bgColor is None or '' == self._bgColor:
            return '#ffffff'
        return self._bgColor
        
class EOL(object):
    def __init__(self, showEOL='False'):
        self._showEOL = showEOL
        
    def getShowEOL(self):
        if self._showEOL is None:
            return False
        if 'true' == self._showEOL.lower():
            return True 
        return False
        
class Edge(object):
    def __init__(self, maxColumns='80', visible='False'):
        self._maxColumns = maxColumns
        self._visible = visible
        
    def getMaxColumns(self):
        if self._maxColumns is None or '' == self._maxColumns:
            return 80
        try:
            return int(self._maxColumns)
        except ValueError:
            return 80
        
    def getVisible(self):
        if self._visible is None:
            return False
        if 'true' == self._visible.strip().lower():
            return True
        return False
        
class Caret(object):
    def __init__(self, color='#000000'):
        self._color = color
        
    def getColor(self):
        if self._color is None or '' == self._color:
            return '#000000'
        return self._color
        
class Highlight(object):    
    def __init__(self):
        self._styles = None
        self._keywords = None
        
    def getKeywords(self):
        if self._keywords is None:
            return (" ")
        return (self._keywords)
    
    def setKeywords(self, keywords):
        self._keywords = keywords
        
    def getHighlightStyles(self):
        if self._styles is None:
            self._styles = {}
        return self._styles
    
    def getHighlightStyle(self, type):
        if not self.getHighlightStyles().has_key(type):
            return Font()
        
        style = self.getHighlightStyles()[type]
        if style is None:
            return Font()
        return style