'''
Created on Jun 2, 2010

@author: tinyshrimp
'''

import os
import wx
import wx.stc as stc 

from org.graver.core.plugin.editor import Editor
from org.graver.core.ui.editor.editorStyle import EditorStyle
from org.graver.application import Application
from org.graver.core.ui.editor import highlightSymbols
from org.graver.core.ui.editor import languages

class DefaultEditor(Editor):
    def __init__(self, parent):
        Editor.__init__(self, parent)
        self._filename = ''
        self._encoding = 'utf-8'
        self.__initializeComponents()
        
    def __initializeComponents(self):
        sizer = wx.BoxSizer(wx.VERTICAL)        
        self.SetSizer(sizer)
        
        self._editView = stc.StyledTextCtrl(self)
        
        self.Bind(stc.EVT_STC_SAVEPOINTLEFT, self.__onSavePointLeft)
        self.Bind(stc.EVT_STC_SAVEPOINTREACHED, self.__onSavePointReached)
        
        sizer.Add(self._editView, True, wx.EXPAND)
        
        wx.CallAfter(self.Layout)
        
    def openFile(self, filename):
        if filename is None:
            return False
        
        self.__setEditorStyle(filename)
        
        if os.path.exists(filename):
            context = self.__loadFileWithEncoding(filename)
            if context is None:
                return False
            self.Unbind(stc.EVT_STC_SAVEPOINTLEFT, handler=self.__onSavePointLeft)
            self.Unbind(stc.EVT_STC_SAVEPOINTREACHED, handler=self.__onSavePointReached)
            self._editView.SetText(context)
            self._editView.SetSavePoint()
            self.Bind(stc.EVT_STC_SAVEPOINTLEFT, self.__onSavePointLeft)   
            self.Bind(stc.EVT_STC_SAVEPOINTREACHED, self.__onSavePointReached)            
        self._filename = filename
        return True
        
    def saveFile(self, filename):
        if filename is None:
            return 
        import io
        context = self._editView.GetText()
        file = io.open(filename, 'w', encoding=self._encoding, newline='\n') 
        file.write(context)
        self._editView.SetSavePoint()
        if filename != self._filename:
            self._filename = filename
            self.__setEditorStyle(filename)
    
    def copy(self):
        self._editView.Copy()
    
    def paste(self):
        self._editView.Paste()
    
    def cut(self):
        self._editView.Cut()
    
    def delete(self):
        self._editView.DeleteBack()
    
    def undo(self):
        self.undo()
    
    def redo(self):
        self.redo()
        
    def __loadFileWithEncoding(self, filename):
        import codecs
        encodings=Application.getSettings().getEncodings()
        if encodings is None:
            encodings = ['utf-8']
        for encoding in encodings:
            try:
                file = codecs.open(filename, 'r', encoding=encoding)
                context = file.read()
                self._encoding = encoding
                file.close()
                return context
            except UnicodeDecodeError:
                file.close()
            except LookupError:
                pass # invalid encoding
        return None
        
    def __setEditorStyle(self, filename):
        if filename is None:
            return
        
        lexer = stc.STC_LEX_NULL
        if '' != filename:
            basename = os.path.basename(filename)
            try:
                name, ext = basename.split('.')
                if languages.LANGUAGES.has_key(ext):
                    lexer = languages.LANGUAGES[ext]
                else:
                    lexer = stc.STC_LEX_NULL
                    
                self._editView.SetLexer(lexer)
            except ValueError:
                pass
            
        self._editView.SetProperty('fold', '1')
        self._editView.SetProperty('tab.timmy.whinge.level', '1')
        self._editView.SetMargins(0, 0)
        
        self.__setIndentStyle()
        self.__setEOLStyle()
        self.__setEdgeStyle()
        self.__setMarginStyle()
        self.__setMarkerStyle()        
        self.__setDefaultFont(lexer)
        self.__setHighlightStyle(lexer)
        self.__setCaretStyle()
        
    def __setIndentStyle(self):
        editorStyle = Application.getSettings().getEditorStyle()
        indent = editorStyle.getIndent()
        
        self._editView.SetIndent(indent.getSize())
        self._editView.SetIndentationGuides(indent.getShowIndentGuide())
        self._editView.SetBackSpaceUnIndents(indent.getBackspaceUnindents())
        self._editView.SetTabIndents(indent.getTabIndes())
        self._editView.SetTabWidth(indent.getTabWidth())
        self._editView.SetUseTabs(indent.getUseTabs())
        self._editView.SetViewWhiteSpace(indent.getViewWhitespace())
        
    def __setEOLStyle(self):
        editorStyle = Application.getSettings().getEditorStyle()
        eol = editorStyle.getEOL()
        
        self._editView.SetEOLMode(stc.STC_EOL_LF)
        self._editView.SetViewEOL(eol.getShowEOL())
    
    def __setEdgeStyle(self):
        editorStyle = Application.getSettings().getEditorStyle()
        edge = editorStyle.getEdge()
        
        if edge.getVisible():
            self._editView.SetEdgeMode(stc.STC_EDGE_LINE)
            self._editView.SetEdgeColumn(edge.getMaxColumns())
        else:
            self._editView.SetEdgeMode(stc.STC_EDGE_NONE)
    
    def __setMarginStyle(self):
        self._editView.SetMarginType(0, stc.STC_MARGIN_NUMBER)
        self._editView.SetMarginWidth(0, 35)
        self._editView.StyleSetSpec(stc.STC_STYLE_LINENUMBER, "size:8,face:Courier New")
    
        self._editView.SetMarginType(1, stc.STC_MARGIN_SYMBOL)
        self._editView.SetMarginMask(1, stc.STC_MASK_FOLDERS)
        self._editView.SetMarginSensitive(1, True)
        self._editView.SetMarginWidth(1, 12)
    
    def __setMarkerStyle(self):
        editorStyle = Application.getSettings().getEditorStyle()
        marker = editorStyle.getMarker()
        
        style = EditorStyle.MARKER_STYLES[marker.getStyle()]
        fgColor = marker.getFgColor()
        bgColor = marker.getBgColor()
        
        for key, value in style.items():
            try:
                self._editView.MarkerDefine(key, value, fgColor, bgColor)
            except:
                continue
        
        self.Bind(stc.EVT_STC_MARGINCLICK, self.__onMarginClick)
        self.Bind(stc.EVT_STC_UPDATEUI, self._onUpdateUI)
    
    def __setCaretStyle(self):
        editorStyle = Application.getSettings().getEditorStyle()
        caret = editorStyle.getCaret()
        self._editView.SetCaretForeground(caret.getColor())
        
    def __setDefaultFont(self, lexer):
        editorStyle = Application.getSettings().getEditorStyle()
        font = editorStyle.getFont()
        
        if highlightSymbols.SYMBOLS.has_key(lexer):
            symbols = highlightSymbols.SYMBOLS[lexer]
            if symbols is None:
                symbols = highlightSymbols.NULL_SYMBOLS
            for symbol in symbols.values():
                self._editView.StyleSetSpec(symbol, font.getSettings())
    
    def __setHighlightStyle(self, lexer):
        if not highlightSymbols.SYMBOLS.has_key(lexer) or stc.STC_LEX_NULL == lexer:
            return
                
        editorStyle = Application.getSettings().getEditorStyle()
        highlightStyles = editorStyle.getHighlightStyles()
        if not highlightStyles.has_key(lexer):
            return
        
        highlight = highlightStyles[lexer]        
        
        self._editView.SetKeyWords(0, highlight.getKeywords())
        
        styles = highlight.getHighlightStyles()
        
        symbols = highlightSymbols.SYMBOLS[lexer]
        for key, value in styles.items():
            if symbols.has_key(key):
                self._editView.StyleSetSpec(symbols[key], value.getSettings())
        
    def __foldAll(self):
        lineCount = self._editView.GetLineCount()
        expanding = True

        # find out if we are folding or unfolding
        for lineNum in range(lineCount):
            if self._editView.GetFoldLevel(lineNum) & stc.STC_FOLDLEVELHEADERFLAG:
                expanding = not self._editView.GetFoldExpanded(lineNum)
                break

        lineNum = 0

        while lineNum < lineCount:
            level = self._editView.GetFoldLevel(lineNum)
            if level & stc.STC_FOLDLEVELHEADERFLAG and \
               (level & stc.STC_FOLDLEVELNUMBERMASK) == stc.STC_FOLDLEVELBASE:

                if expanding:
                    self._editView.SetFoldExpanded(lineNum, True)
                    lineNum = self.__expand(lineNum, True)
                    lineNum = lineNum - 1
                else:
                    lastChild = self._editView.GetLastChild(lineNum, -1)
                    self._editView.SetFoldExpanded(lineNum, False)

                    if lastChild > lineNum:
                        self._editView.HideLines(lineNum+1, lastChild)

            lineNum = lineNum + 1



    def __expand(self, line, doExpand, force=False, visLevels=0, level=-1):
        lastChild = self._editView.GetLastChild(line, level)
        line = line + 1

        while line <= lastChild:
            if force:
                if visLevels > 0:
                    self._editView.ShowLines(line, line)
                else:
                    self._editView.HideLines(line, line)
            else:
                if doExpand:
                    self._editView.ShowLines(line, line)

            if level == -1:
                level = self._editView.GetFoldLevel(line)

            if level & stc.STC_FOLDLEVELHEADERFLAG:
                if force:
                    if visLevels > 1:
                        self._editView.SetFoldExpanded(line, True)
                    else:
                        self._editView.SetFoldExpanded(line, False)

                    line = self.__expand(line, doExpand, force, visLevels-1)

                else:
                    if doExpand and self._editView.GetFoldExpanded(line):
                        line = self.__expand(line, True, force, visLevels-1)
                    else:
                        line = self.__expand(line, False, force, visLevels-1)
            else:
                line = line + 1

        return line
                
    def _onUpdateUI(self, evt):
        # check for matching braces
        braceAtCaret = -1
        braceOpposite = -1
        charBefore = None
        caretPos = self._editView.GetCurrentPos()

        if caretPos > 0:
            charBefore = self._editView.GetCharAt(caretPos - 1)
            styleBefore = self._editView.GetStyleAt(caretPos - 1)

        # check before
        if charBefore and chr(charBefore) in "[]{}()" and styleBefore == stc.STC_P_OPERATOR:
            braceAtCaret = caretPos - 1

        # check after
        if braceAtCaret < 0:
            charAfter = self._editView.GetCharAt(caretPos)
            styleAfter = self._editView.GetStyleAt(caretPos)

            if charAfter and chr(charAfter) in "[]{}()" and styleAfter == stc.STC_P_OPERATOR:
                braceAtCaret = caretPos

        if braceAtCaret >= 0:
            braceOpposite = self._editView.BraceMatch(braceAtCaret)

        if braceAtCaret != -1  and braceOpposite == -1:
            self._editView.BraceBadLight(braceAtCaret)
        else:
            self._editView.BraceHighlight(braceAtCaret, braceOpposite)
                
    def __onMarginClick(self, evt):
        # fold and unfold as needed
        if evt.GetMargin() == 1:
            if evt.GetShift() and evt.GetControl():
                self.__foldAll()
            else:
                lineClicked = self._editView.LineFromPosition(evt.GetPosition())

                if self._editView.GetFoldLevel(lineClicked) & stc.STC_FOLDLEVELHEADERFLAG:
                    if evt.GetShift():
                        self._editView.SetFoldExpanded(lineClicked, True)
                        self.__expand(lineClicked, True, True, 1)
                    elif evt.GetControl():
                        if self._editView.GetFoldExpanded(lineClicked):
                            self._editView.SetFoldExpanded(lineClicked, False)
                            self.__expand(lineClicked, False, True, 0)
                        else:
                            self._editView.SetFoldExpanded(lineClicked, True)
                            self.__expand(lineClicked, True, True, 100)
                    else:
                        self._editView.ToggleFold(lineClicked)
        
    def __onSavePointLeft(self, evt):
        self.getContentChangedEventHandler().invoke(self, None)
        
    def __onSavePointReached(self, evt):
        self.getContentSavedEventHandler().invoke(self, None)
        