'''
Created on Jun 15, 2010

@author: tinyshrimp
'''

import wx.stc as stc

LANGUAGES = {'py':stc.STC_LEX_PYTHON, 
             'xml':stc.STC_LEX_XML, 
             'c':stc.STC_LEX_CPP, 
             'cpp':stc.STC_LEX_CPP, 
             'h':stc.STC_LEX_CPP,
             'htm':stc.STC_LEX_HTML,
             'html':stc.STC_LEX_HTML,
             'css':stc.STC_LEX_CSS}

LANGUAGE_MAP = {'container':stc.STC_LEX_CONTAINER,
                'python':stc.STC_LEX_PYTHON,
                'cpp':stc.STC_LEX_CPP,
                'html':stc.STC_LEX_HTML,
                'xml':stc.STC_LEX_XML,
                'perl':stc.STC_LEX_PERL,
                'sql':stc.STC_LEX_SQL,
                'vb':stc.STC_LEX_VB,
                'properties':stc.STC_LEX_PROPERTIES,
                'errorlist':stc.STC_LEX_ERRORLIST,
                'makefile':stc.STC_LEX_MAKEFILE,
                'batch':stc.STC_LEX_BATCH,
                'xcode':stc.STC_LEX_XCODE,
                'latex':stc.STC_LEX_LATEX,
                'lua':stc.STC_LEX_LUA,
                'diff':stc.STC_LEX_DIFF,
                'conf':stc.STC_LEX_CONF,
                'pascal':stc.STC_LEX_PASCAL,
                'ave':stc.STC_LEX_AVE,
                'ada':stc.STC_LEX_ADA,
                'lisp':stc.STC_LEX_LISP,
                'ruby':stc.STC_LEX_RUBY,
                'eiffel':stc.STC_LEX_EIFFEL,
                'eiffelkw':stc.STC_LEX_EIFFELKW,
                'tcl':stc.STC_LEX_TCL,
                'nncrontab':stc.STC_LEX_NNCRONTAB,
                'bullant':stc.STC_LEX_BULLANT,
                'vbscript':stc.STC_LEX_VBSCRIPT,
                'baan':stc.STC_LEX_BAAN,
                'matlab':stc.STC_LEX_MATLAB,
                'scriptol':stc.STC_LEX_SCRIPTOL,
                'asm':stc.STC_LEX_ASM,
                'cppnocase':stc.STC_LEX_CPPNOCASE,
                'fortran':stc.STC_LEX_FORTRAN,
                'f77':stc.STC_LEX_F77,
                'css':stc.STC_LEX_CSS,
                'pov':stc.STC_LEX_POV,
                'lout':stc.STC_LEX_LOUT,
                'escript':stc.STC_LEX_ESCRIPT,
                'ps':stc.STC_LEX_PS,
                'nsis':stc.STC_LEX_NSIS,
                'mmixal':stc.STC_LEX_MMIXAL,
                'clw':stc.STC_LEX_CLW,
                'clwnocase':stc.STC_LEX_CLWNOCASE,
                'lot':stc.STC_LEX_LOT,
                'yaml':stc.STC_LEX_YAML,
                'tex':stc.STC_LEX_TEX,
                'metapost':stc.STC_LEX_METAPOST,
                'powerbasic':stc.STC_LEX_POWERBASIC,
                'forth':stc.STC_LEX_FORTH,
                'erlang':stc.STC_LEX_ERLANG,
                'octave':stc.STC_LEX_OCTAVE,
                'mssql':stc.STC_LEX_MSSQL,
                'verilog':stc.STC_LEX_VERILOG,
                'kix':stc.STC_LEX_KIX,
                'gui4cli':stc.STC_LEX_GUI4CLI,
                'specman':stc.STC_LEX_SPECMAN,
                'au3':stc.STC_LEX_AU3,
                'apdl':stc.STC_LEX_APDL,
                'bash':stc.STC_LEX_BASH,
                'asn1':stc.STC_LEX_ASN1,
                'vhdl':stc.STC_LEX_VHDL,
                'caml':stc.STC_LEX_CAML,
                'blitzbasic':stc.STC_LEX_BLITZBASIC,
                'purebasic':stc.STC_LEX_PUREBASIC,
                'haskell':stc.STC_LEX_HASKELL,
                'phpscript':stc.STC_LEX_PHPSCRIPT,
                'tads3':stc.STC_LEX_TADS3,
                'rebol':stc.STC_LEX_REBOL,
                'smalltalk':stc.STC_LEX_SMALLTALK,
                'flagship':stc.STC_LEX_FLAGSHIP,
                'csound':stc.STC_LEX_CSOUND,
                'freebasic':stc.STC_LEX_FREEBASIC,
                'innosetup':stc.STC_LEX_INNOSETUP,
                'opal':stc.STC_LEX_OPAL,
                'spice':stc.STC_LEX_SPICE,
                'automatic':stc.STC_LEX_AUTOMATIC}