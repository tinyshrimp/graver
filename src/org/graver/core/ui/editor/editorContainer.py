'''
Created on Jun 1, 2010

@author: tinyshrimp
'''

import wx
from wx import aui
from fnmatch import fnmatch

from org.graver.utils.instantiator import createClassInstance
from org.graver.application import Application
from org.graver.core.plugin.pane import Pane

class EditorContainer(Pane):
    def __init__(self, parent):
        Pane.__init__(self, parent, 'EditorContainer', '', pos=wx.CENTER, showCaption=False)
        
        self._openedDocuments = None
        
        Application.getDocumentManager().getDocumentOpenedEventHandler().add(self.__onDocumentOpened)
        Application.getDocumentManager().getDocumentClosedEventHandler().add(self.__onDocumentClosed)
        Application.getDocumentManager().getDocumentSavedEventHandler().add(self.__onDocumentSaved)
        Application.getDocumentManager().getDocumentChangedEventHandler().add(self.__onDocumentChanged)
        Application.getDocumentManager().getDocumentRenamedEventHandler().add(self.__onDocumentRenamed)
        Application.getDocumentManager().getSelectedDocumentChangedEventHandler().add(self.__selectDocument)
        
        self.__initializeComponent()
        
    def __initializeComponent(self):
        self._auiNotebook = aui.AuiNotebook(self)
        
        sizer = wx.BoxSizer()
        sizer.Add(self._auiNotebook, -1, wx.EXPAND)
        self.SetSizer(sizer)
        
        wx.CallAfter(self.Layout)
        
        self._auiNotebook.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.__onPageClose)
        self._auiNotebook.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.__onPageChanged)
        
    def __getOpenedDocuments(self):
        if self._openedDocuments is None:
            self._openedDocuments = {}
        return self._openedDocuments
    
    def __getFileEditor(self, filename):
        editorClass = ''
        
        filePatterns = Application.getSettings().getFileAssociations().keys()
        for filePattern in filePatterns:
            if fnmatch(filename, filePattern):
                editorClass = Application.getSettings().getFileAssociations()[filePattern]
                
        if editorClass is None or '' == editorClass:
            editorClass = Application.getSettings().getDefaultEditor()
                    
        if editorClass is None or '' == editorClass:
            return None
        
        editorClsObj = createClassInstance(editorClass)
        if editorClsObj is None:
            return None
        
        editor = editorClsObj(self)
        if editor is None:
            return None
        
        return editor
        
    def __onDocumentOpened(self, sender, evt):
        document = evt
        if document is None:
            return
        
        docName =  document.getName()
        if docName is None:
            return
        
        editor = self.__getFileEditor(docName)
        if editor is None:
            raise Exception('Cannot get the editor for file.\n Filename: %s' % docName)
        
        document.setEditor(editor)
        
        pageCaption = ''
        if '' == docName:
            pageCaption = 'Unsaved Document'
        else:
            pageCaption = docName
            
        if editor.openFile(document.getFullPath()):
            if self._auiNotebook.AddPage(document.getEditor(), pageCaption, True):
                self.__getOpenedDocuments()[document.getEditor()] = document
                Application.getDocumentManager().selectDocument(document.getFullPath())
        else:
            editor.close()
            dlg = wx.MessageDialog(None, 'Cannot open file: %s' % document.getFullPath(),
                                   'Error', wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            document.close()
            
    def __onDocumentClosed(self, sender, evt):
        document = evt
        if document is None:
            return
        
        editor = document.getEditor()
        pageIndex = self._auiNotebook.GetPageIndex(editor)
        if wx.NOT_FOUND == pageIndex:
            return
        self._auiNotebook.RemovePage(pageIndex)
            
    def __onDocumentSaved(self, sender, evt):
        pass
    
    def __onDocumentChanged(self, sender, evt):
        pass
    
    def __onDocumentRenamed(self, sender, evt):
        document = sender
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        
        index = self._auiNotebook.GetPageIndex(editor)
        if wx.NOT_FOUND == index:
            return
        
        self._auiNotebook.SetPageText(index, document.getName())
    
    def __selectDocument(self, sender, evt):
        document = evt
        if document is None:
            return
        
        editor = document.getEditor()
        if editor is None:
            return
        pageIndex = self._auiNotebook.GetPageIndex(editor)
        if pageIndex != wx.NOT_FOUND and pageIndex != self._auiNotebook.GetSelection():
            self._auiNotebook.SetSelection(pageIndex)
        
    def __onPageClose(self, evt):
        selectIndex = evt.GetSelection()
        if 0 <= selectIndex and self._auiNotebook.GetPageCount() > selectIndex:
            editor = self._auiNotebook.GetPage(selectIndex)
            if editor is None or not self.__getOpenedDocuments().has_key(editor):
                return
            
            closeAction = Application.getActionManager().getAction('DocumentActions.Close')
            if closeAction is not None:
                closeAction.execute(None)
    
    def __onPageChanged(self, evt):
        index = self._auiNotebook.GetSelection()
        editor = self._auiNotebook.GetPage(index)
        if self.__getOpenedDocuments().has_key(editor):
            document = self.__getOpenedDocuments()[editor]
            Application.getDocumentManager().selectDocument(document.getFullPath())
        