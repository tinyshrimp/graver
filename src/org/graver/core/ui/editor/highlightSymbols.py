'''
Created on Jun 15, 2010

@author: tinyshrimp
'''

import wx.stc as stc

NULL_SYMBOLS = {    'default':stc.STC_STYLE_DEFAULT,
                    'linenumber':stc.STC_STYLE_LINENUMBER,
                    'bracelight':stc.STC_STYLE_BRACELIGHT,
                    'bracebad':stc.STC_STYLE_BRACEBAD,
                    'controlchar':stc.STC_STYLE_CONTROLCHAR,
                    'indentguide':stc.STC_STYLE_INDENTGUIDE,
                    'calltip':stc.STC_STYLE_CALLTIP,
                    'lastpredefined':stc.STC_STYLE_LASTPREDEFINED,
                    'max':stc.STC_STYLE_MAX
                }

ADA_SYMBOLS = {     'character':stc.STC_ADA_CHARACTER,
                    'charactereol':stc.STC_ADA_CHARACTEREOL,
                    'commentline':stc.STC_ADA_COMMENTLINE,
                    'default':stc.STC_ADA_DEFAULT,
                    'delimiter':stc.STC_ADA_DELIMITER,
                    'identifier':stc.STC_ADA_IDENTIFIER,
                    'illegal':stc.STC_ADA_ILLEGAL,
                    'label':stc.STC_ADA_LABEL,
                    'number':stc.STC_ADA_NUMBER,
                    'string':stc.STC_ADA_STRING,
                    'stringeol':stc.STC_ADA_STRINGEOL,
                    'word':stc.STC_ADA_WORD
               }

APDL_SYMBOLS = {    'argument':stc.STC_APDL_ARGUMENT,
                    'command':stc.STC_APDL_COMMAND,
                    'comment':stc.STC_APDL_COMMENT,
                    'commentblock':stc.STC_APDL_COMMENTBLOCK,
                    'default':stc.STC_APDL_DEFAULT,
                    'function':stc.STC_APDL_FUNCTION,
                    'number':stc.STC_APDL_NUMBER,
                    'operator':stc.STC_APDL_OPERATOR,
                    'processor':stc.STC_APDL_PROCESSOR,
                    'slashcommand':stc.STC_APDL_SLASHCOMMAND,
                    'starcommand':stc.STC_APDL_STARCOMMAND,
                    'string':stc.STC_APDL_STRING,
                    'word':stc.STC_APDL_WORD
                }

ASM_SYMBOLS = {     'character':stc.STC_ASM_CHARACTER,
                    'comment':stc.STC_ASM_COMMENT,
                    'commentblock':stc.STC_ASM_COMMENTBLOCK,
                    'cpuinstruction':stc.STC_ASM_CPUINSTRUCTION,
                    'default':stc.STC_ASM_DEFAULT,
                    'directive':stc.STC_ASM_DIRECTIVE,
                    'directiveoperand':stc.STC_ASM_DIRECTIVEOPERAND,
                    'extinstruction':stc.STC_ASM_EXTINSTRUCTION,
                    'identifier':stc.STC_ASM_IDENTIFIER,
                    'mathinstruction':stc.STC_ASM_MATHINSTRUCTION,
                    'number':stc.STC_ASM_NUMBER,
                    'operator':stc.STC_ASM_OPERATOR,
                    'register':stc.STC_ASM_REGISTER,
                    'string':stc.STC_ASM_STRING,
                    'stringeol':stc.STC_ASM_STRINGEOL
               }

ASN1_SYMBOLS = {    'attribute':stc.STC_ASN1_ATTRIBUTE,
                    'comment':stc.STC_ASN1_COMMENT,
                    'default':stc.STC_ASN1_DEFAULT,
                    'descriptor':stc.STC_ASN1_DESCRIPTOR,
                    'identifier':stc.STC_ASN1_IDENTIFIER,
                    'keyword':stc.STC_ASN1_KEYWORD,
                    'oid':stc.STC_ASN1_OID,
                    'operator':stc.STC_ASN1_OPERATOR,
                    'scalar':stc.STC_ASN1_SCALAR,
                    'string':stc.STC_ASN1_STRING,
                    'type':stc.STC_ASN1_TYPE
                }

AU3_SYMBOLS = {     'comment':stc.STC_AU3_COMMENT,
                    'commentblock':stc.STC_AU3_COMMENTBLOCK,
                    'comobj':stc.STC_AU3_COMOBJ,
                    'default':stc.STC_AU3_DEFAULT,
                    'expand':stc.STC_AU3_EXPAND,
                    'function':stc.STC_AU3_FUNCTION,
                    'keyword':stc.STC_AU3_KEYWORD,
                    'macro':stc.STC_AU3_MACRO,
                    'number':stc.STC_AU3_NUMBER,
                    'operator':stc.STC_AU3_OPERATOR,
                    'preprocessor':stc.STC_AU3_PREPROCESSOR,
                    'sent':stc.STC_AU3_SENT,
                    'special':stc.STC_AU3_SPECIAL,
                    'string':stc.STC_AU3_STRING,
                    'udf':stc.STC_AU3_UDF,
                    'variable':stc.STC_AU3_VARIABLE
               }

AVE_SYMBOLS = {     'comment':stc.STC_AVE_COMMENT,
                    'default':stc.STC_AVE_DEFAULT,
                    'enum':stc.STC_AVE_ENUM,
                    'identifier':stc.STC_AVE_IDENTIFIER,
                    'number':stc.STC_AVE_NUMBER,
                    'operator':stc.STC_AVE_OPERATOR,
                    'string':stc.STC_AVE_STRING,
                    'stringeol':stc.STC_AVE_STRINGEOL,
                    'word':stc.STC_AVE_WORD,
                    'word1':stc.STC_AVE_WORD1,
                    'word2':stc.STC_AVE_WORD2,
                    'word3':stc.STC_AVE_WORD3,
                    'word4':stc.STC_AVE_WORD4,
                    'word5':stc.STC_AVE_WORD5,
                    'word6':stc.STC_AVE_WORD6
               }

BAAN_SYMBOLS = {    'comment':stc.STC_BAAN_COMMENT,
                    'commentdoc':stc.STC_BAAN_COMMENTDOC,
                    'default':stc.STC_BAAN_DEFAULT,
                    'identifier':stc.STC_BAAN_IDENTIFIER,
                    'number':stc.STC_BAAN_NUMBER,
                    'operator':stc.STC_BAAN_OPERATOR,
                    'preprocessor':stc.STC_BAAN_PREPROCESSOR,
                    'string':stc.STC_BAAN_STRING,
                    'stringeol':stc.STC_BAAN_STRINGEOL,
                    'word':stc.STC_BAAN_WORD,
                    'word2':stc.STC_BAAN_WORD2
                }

BASH_SYMBOLS = {    'backticks':stc.STC_SH_BACKTICKS,
                    'character':stc.STC_SH_CHARACTER,
                    'commentline':stc.STC_SH_COMMENTLINE,
                    'default':stc.STC_SH_DEFAULT,
                    'error':stc.STC_SH_ERROR,
                    'heredelim':stc.STC_SH_HERE_DELIM,
                    'hereq':stc.STC_SH_HERE_Q,
                    'identifier':stc.STC_SH_IDENTIFIER,
                    'number':stc.STC_SH_NUMBER,
                    'operator':stc.STC_SH_OPERATOR,
                    'param':stc.STC_SH_PARAM,
                    'scalar':stc.STC_SH_SCALAR,
                    'string':stc.STC_SH_STRING,
                    'word':stc.STC_SH_WORD
                }

BATCH_SYMBOLS = {   'command':stc.STC_BAT_COMMAND,
                    'comment':stc.STC_BAT_COMMENT,
                    'default':stc.STC_BAT_DEFAULT,
                    'hide':stc.STC_BAT_HIDE,
                    'identifier':stc.STC_BAT_IDENTIFIER,
                    'label':stc.STC_BAT_LABEL,
                    'operator':stc.STC_BAT_OPERATOR,
                    'word':stc.STC_BAT_WORD
                }

CAML_SYMBOLS = {    'char':stc.STC_CAML_CHAR,
                    'comment':stc.STC_CAML_COMMENT,
                    'comment1':stc.STC_CAML_COMMENT1,
                    'comment2':stc.STC_CAML_COMMENT2,
                    'comment3':stc.STC_CAML_COMMENT3,
                    'default':stc.STC_CAML_DEFAULT,
                    'identifier':stc.STC_CAML_IDENTIFIER,
                    'keyword':stc.STC_CAML_KEYWORD,
                    'keyword2':stc.STC_CAML_KEYWORD2,
                    'keyword3':stc.STC_CAML_KEYWORD3,
                    'linenum':stc.STC_CAML_LINENUM,
                    'number':stc.STC_CAML_NUMBER,
                    'operator':stc.STC_CAML_OPERATOR,
                    'string':stc.STC_CAML_STRING,
                    'tagname':stc.STC_CAML_TAGNAME
                }

CLW_SYMBOLS = {     'attribute':stc.STC_CLW_ATTRIBUTE,
                    'builtinproceduresfunction':stc.STC_CLW_BUILTIN_PROCEDURES_FUNCTION,
                    'comment':stc.STC_CLW_COMMENT,
                    'compilerdirective':stc.STC_CLW_COMPILER_DIRECTIVE,
                    'default':stc.STC_CLW_DEFAULT,
                    'deprecated':stc.STC_CLW_DEPRECATED,
                    'error':stc.STC_CLW_ERROR,
                    'integerconstant':stc.STC_CLW_INTEGER_CONSTANT,
                    'keyword':stc.STC_CLW_KEYWORD,
                    'label':stc.STC_CLW_LABEL,
                    'picturestring':stc.STC_CLW_PICTURE_STRING,
                    'realconstant':stc.STC_CLW_REAL_CONSTANT,
                    'runtimeexpressions':stc.STC_CLW_RUNTIME_EXPRESSIONS,
                    'standardequate':stc.STC_CLW_STANDARD_EQUATE,
                    'string':stc.STC_CLW_STRING,
                    'structuredatatype':stc.STC_CLW_STRUCTURE_DATA_TYPE,
                    'useridentifier':stc.STC_CLW_USER_IDENTIFIER
               }

CONF_SYMBOLS = {    'comment':stc.STC_CONF_COMMENT,
                    'default':stc.STC_CONF_DEFAULT,
                    'directive':stc.STC_CONF_DIRECTIVE,
                    'extension':stc.STC_CONF_EXTENSION,
                    'identifier':stc.STC_CONF_IDENTIFIER,
                    'ip':stc.STC_CONF_IP,
                    'number':stc.STC_CONF_NUMBER,
                    'operator':stc.STC_CONF_OPERATOR,
                    'parameter':stc.STC_CONF_PARAMETER,
                    'string':stc.STC_CONF_STRING
                }

CPP_SYMBOLS = {     'default':stc.STC_C_DEFAULT,
                    'comment':stc.STC_C_COMMENT,
                    'commentline':stc.STC_C_COMMENTLINE,
                    'commentdoc':stc.STC_C_COMMENTDOC,
                    'number':stc.STC_C_NUMBER,
                    'word':stc.STC_C_WORD,
                    'string':stc.STC_C_STRING,
                    'character':stc.STC_C_CHARACTER,
                    'uuid':stc.STC_C_UUID,
                    'preprocessor':stc.STC_C_PREPROCESSOR,
                    'operator':stc.STC_C_OPERATOR,
                    'identifier':stc.STC_C_IDENTIFIER,
                    'stringeol':stc.STC_C_STRINGEOL,
                    'verbatim':stc.STC_C_VERBATIM,
                    'regex':stc.STC_C_REGEX,
                    'commentlinedoc':stc.STC_C_COMMENTLINEDOC,
                    'word2':stc.STC_C_WORD2,
                    'commentdockeyword':stc.STC_C_COMMENTDOCKEYWORD,
                    'commentdockeyworderror':stc.STC_C_COMMENTDOCKEYWORDERROR,
                    'globalclass':stc.STC_C_GLOBALCLASS
                }

CSOUND_SYMBOLS = {  'aratevar':stc.STC_CSOUND_ARATE_VAR,
                    'comment':stc.STC_CSOUND_COMMENT,
                    'commentblock':stc.STC_CSOUND_COMMENTBLOCK,
                    'default':stc.STC_CSOUND_DEFAULT,
                    'globalvar':stc.STC_CSOUND_GLOBAL_VAR,
                    'headerstmt':stc.STC_CSOUND_HEADERSTMT,
                    'identifier':stc.STC_CSOUND_IDENTIFIER,
                    'instr':stc.STC_CSOUND_INSTR,
                    'iratevar':stc.STC_CSOUND_IRATE_VAR,
                    'kratevar':stc.STC_CSOUND_KRATE_VAR,
                    'number':stc.STC_CSOUND_NUMBER,
                    'opcode':stc.STC_CSOUND_OPCODE,
                    'operator':stc.STC_CSOUND_OPERATOR,
                    'param':stc.STC_CSOUND_PARAM,
                    'stringeol':stc.STC_CSOUND_STRINGEOL,
                    'userkeyword':stc.STC_CSOUND_USERKEYWORD
                  }

CSS_SYMBOLS = {     'attribute':stc.STC_CSS_ATTRIBUTE,
                    'class':stc.STC_CSS_CLASS,
                    'comment':stc.STC_CSS_COMMENT,
                    'default':stc.STC_CSS_DEFAULT,
                    'directive':stc.STC_CSS_DIRECTIVE,
                    'doublestring':stc.STC_CSS_DOUBLESTRING,
                    'id':stc.STC_CSS_ID,
                    'identifier':stc.STC_CSS_IDENTIFIER,
                    'identifier2':stc.STC_CSS_IDENTIFIER2,
                    'important':stc.STC_CSS_IMPORTANT,
                    'operator':stc.STC_CSS_OPERATOR,
                    'pseudoclass':stc.STC_CSS_PSEUDOCLASS,
                    'singlestring':stc.STC_CSS_SINGLESTRING,
                    'tag':stc.STC_CSS_TAG,
                    'unknownidentifier':stc.STC_CSS_UNKNOWN_IDENTIFIER,
                    'unknownpseudoclass':stc.STC_CSS_UNKNOWN_PSEUDOCLASS,
                    'value':stc.STC_CSS_VALUE
               }

HTML_SYMBOLS = {    'hbacommentline':stc.STC_HBA_COMMENTLINE,
                    'hbadefault':stc.STC_HBA_DEFAULT,
                    'hbaidentifier':stc.STC_HBA_IDENTIFIER,
                    'hbanumber':stc.STC_HBA_NUMBER,
                    'hbastart':stc.STC_HBA_START,
                    'hbastring':stc.STC_HBA_STRING,
                    'hbastringeol':stc.STC_HBA_STRINGEOL,
                    'hbaword':stc.STC_HBA_WORD,
                    'hjacomment':stc.STC_HJA_COMMENT,
                    'hjacommentdoc':stc.STC_HJA_COMMENTDOC,
                    'hjacommentline':stc.STC_HJA_COMMENTLINE,
                    'hjadefault':stc.STC_HJA_DEFAULT,
                    'hjadoublestring':stc.STC_HJA_DOUBLESTRING,
                    'hjakeyword':stc.STC_HJA_KEYWORD,
                    'hjanumber':stc.STC_HJA_NUMBER,
                    'hjaregex':stc.STC_HJA_REGEX,
                    'hjasinglestring':stc.STC_HJA_SINGLESTRING,
                    'hjastart':stc.STC_HJA_START,
                    'hjastringeol':stc.STC_HJA_STRINGEOL,
                    'hjasymbols':stc.STC_HJA_SYMBOLS,
                    'hjaword':stc.STC_HJA_WORD,
                    'hjcomment':stc.STC_HJ_COMMENT,
                    'hjcommentdoc':stc.STC_HJ_COMMENTDOC,
                    'hjcommentline':stc.STC_HJ_COMMENTLINE,
                    'hjdefault':stc.STC_HJ_DEFAULT,
                    'hjdoublestring':stc.STC_HJ_DOUBLESTRING,
                    'hjkeyword':stc.STC_HJ_KEYWORD,
                    'hjnumber':stc.STC_HJ_NUMBER,
                    'hjregex':stc.STC_HJ_REGEX,
                    'hjsinglestring':stc.STC_HJ_SINGLESTRING,
                    'hjstart':stc.STC_HJ_START,
                    'hjstringeol':stc.STC_HJ_STRINGEOL,
                    'hjsymbols':stc.STC_HJ_SYMBOLS,
                    'hjword':stc.STC_HJ_WORD,
                    'asp':stc.STC_H_ASP,
                    'aspat':stc.STC_H_ASPAT,
                    'attribute':stc.STC_H_ATTRIBUTE,
                    'attrubuteunknown':stc.STC_H_ATTRIBUTEUNKNOWN,
                    'cdata':stc.STC_H_CDATA,
                    'comment':stc.STC_H_COMMENT,
                    'default':stc.STC_H_DEFAULT,
                    'doublestring':stc.STC_H_DOUBLESTRING,
                    'entity':stc.STC_H_ENTITY,
                    'number':stc.STC_H_NUMBER,
                    'other':stc.STC_H_OTHER,
                    'question':stc.STC_H_QUESTION,
                    'script':stc.STC_H_SCRIPT,
                    'sgml1stparam':stc.STC_H_SGML_1ST_PARAM,
                    'sgml1stparamcomment':stc.STC_H_SGML_1ST_PARAM_COMMENT,
                    'sgmlblockdefault':stc.STC_H_SGML_BLOCK_DEFAULT,
                    'sgmlcommand':stc.STC_H_SGML_COMMAND,
                    'sgmlcomment':stc.STC_H_SGML_COMMENT,
                    'sgmldefault':stc.STC_H_SGML_DEFAULT,
                    'sgmldoublestring':stc.STC_H_SGML_DOUBLESTRING,
                    'sgmlentity':stc.STC_H_SGML_ENTITY,
                    'sgmlerror':stc.STC_H_SGML_ERROR,
                    'sgmlsimplestring':stc.STC_H_SGML_SIMPLESTRING,
                    'sgmlspecial':stc.STC_H_SGML_SPECIAL,
                    'singlestring':stc.STC_H_SINGLESTRING,
                    'tag':stc.STC_H_TAG,
                    'tagend':stc.STC_H_TAGEND,
                    'tagunknown':stc.STC_H_TAGUNKNOWN,
                    'value':stc.STC_H_VALUE,
                    'xccomment':stc.STC_H_XCCOMMENT,
                    'xmlend':stc.STC_H_XMLEND,
                    'xmlstart':stc.STC_H_XMLSTART
                }


PERL_SYMBOLS = {    'default':stc.STC_PL_DEFAULT,
                    'error':stc.STC_PL_ERROR,
                    'commentline':stc.STC_PL_COMMENTLINE,
                    'pod':stc.STC_PL_POD,
                    'number':stc.STC_PL_NUMBER,
                    'word':stc.STC_PL_WORD,
                    'string':stc.STC_PL_STRING,
                    'character':stc.STC_PL_CHARACTER,
                    'punctuation':stc.STC_PL_PUNCTUATION,
                    'preprocessor':stc.STC_PL_PREPROCESSOR,
                    'operator':stc.STC_PL_OPERATOR,
                    'identifier':stc.STC_PL_IDENTIFIER,
                    'scaler':stc.STC_PL_SCALAR,
                    'array':stc.STC_PL_ARRAY,
                    'hash':stc.STC_PL_HASH,
                    'symboltable':stc.STC_PL_SYMBOLTABLE,
                    'variableindexer':stc.STC_PL_VARIABLE_INDEXER,
                    'regex':stc.STC_PL_REGEX,
                    'regsubst':stc.STC_PL_REGSUBST,
                    'longquote':stc.STC_PL_LONGQUOTE,
                    'backticks':stc.STC_PL_BACKTICKS,
                    'datasection':stc.STC_PL_DATASECTION,
                    'heredelim':stc.STC_PL_HERE_DELIM,
                    'hereq':stc.STC_PL_HERE_Q,
                    'hereqq':stc.STC_PL_HERE_QQ,
                    'hereqx':stc.STC_PL_HERE_QX,
                    'stringq':stc.STC_PL_STRING_Q,
                    'stringqq':stc.STC_PL_STRING_QQ,
                    'stringqx':stc.STC_PL_STRING_QX,
                    'stringqr':stc.STC_PL_STRING_QR,
                    'stringqw':stc.STC_PL_STRING_QW,
                    'podverb':stc.STC_PL_POD_VERB
                }

PYTHON_SYMBOLS = {  'default':stc.STC_P_DEFAULT, 
                    'commentline':stc.STC_P_COMMENTLINE,  
                    'number':stc.STC_P_NUMBER,  
                    'string':stc.STC_P_STRING,  
                    'character':stc.STC_P_CHARACTER, 
                    'word':stc.STC_P_WORD,  
                    'triple':stc.STC_P_TRIPLE,  
                    'tripledouble':stc.STC_P_TRIPLEDOUBLE,  
                    'classname':stc.STC_P_CLASSNAME,  
                    'defname':stc.STC_P_DEFNAME, 
                    'operator':stc.STC_P_OPERATOR,  
                    'identifier':stc.STC_P_IDENTIFIER,  
                    'commentblock':stc.STC_P_COMMENTBLOCK,  
                    'stringeol':stc.STC_P_STRINGEOL,
                    'word2':stc.STC_P_WORD2,
                    'decorator':stc.STC_P_DECORATOR
                }

RUBY_SYMBOLS = {    'default':stc.STC_RB_DEFAULT,
                    'error':stc.STC_RB_ERROR,
                    'commentline':stc.STC_RB_COMMENTLINE,
                    'pod':stc.STC_RB_POD,
                    'number':stc.STC_RB_NUMBER,
                    'word':stc.STC_RB_WORD,
                    'string':stc.STC_RB_STRING,
                    'character':stc.STC_RB_CHARACTER,
                    'classname':stc.STC_RB_CLASSNAME,
                    'defname':stc.STC_RB_DEFNAME,
                    'operator':stc.STC_RB_OPERATOR,
                    'identifier':stc.STC_RB_IDENTIFIER,
                    'regex':stc.STC_RB_REGEX,
                    'global':stc.STC_RB_GLOBAL,
                    'symbol':stc.STC_RB_SYMBOL,
                    'modulename':stc.STC_RB_MODULE_NAME,
                    'instancevar':stc.STC_RB_INSTANCE_VAR,
                    'classvar':stc.STC_RB_CLASS_VAR,
                    'backticks':stc.STC_RB_BACKTICKS,
                    'datasection':stc.STC_RB_DATASECTION,
                    'heredelim':stc.STC_RB_HERE_DELIM,
                    'hereq':stc.STC_RB_HERE_Q,
                    'hereqq':stc.STC_RB_HERE_QQ,
                    'hereqx':stc.STC_RB_HERE_QX,
                    'stringq':stc.STC_RB_STRING_Q,
                    'stringqq':stc.STC_RB_STRING_QQ,
                    'stringqx':stc.STC_RB_STRING_QX,
                    'stringqr':stc.STC_RB_STRING_QR,
                    'stringqw':stc.STC_RB_STRING_QW,
                    'worddemoted':stc.STC_RB_WORD_DEMOTED,
                    'stdin':stc.STC_RB_STDIN,
                    'stdout':stc.STC_RB_STDOUT,
                    'stderr':stc.STC_RB_STDERR,
                    'upperbound':stc.STC_RB_UPPER_BOUND
                }

TCL_SYMBOLS = {     'default':stc.STC_TCL_DEFAULT,
                    'comment':stc.STC_TCL_COMMENT,
                    'commentline':stc.STC_TCL_COMMENTLINE,
                    'number':stc.STC_TCL_NUMBER,
                    'wordinquote':stc.STC_TCL_WORD_IN_QUOTE,
                    'inquote':stc.STC_TCL_IN_QUOTE,
                    'operator':stc.STC_TCL_OPERATOR,
                    'identifier':stc.STC_TCL_IDENTIFIER,
                    'substitution':stc.STC_TCL_SUBSTITUTION,
                    'subbrace':stc.STC_TCL_SUB_BRACE,
                    'modifier':stc.STC_TCL_MODIFIER,
                    'expand':stc.STC_TCL_EXPAND,
                    'word':stc.STC_TCL_WORD,
                    'word2':stc.STC_TCL_WORD2,
                    'word3':stc.STC_TCL_WORD3,
                    'word4':stc.STC_TCL_WORD4,
                    'word5':stc.STC_TCL_WORD5,
                    'word6':stc.STC_TCL_WORD6,
                    'word7':stc.STC_TCL_WORD7,
                    'word8':stc.STC_TCL_WORD8,
                    'commentbox':stc.STC_TCL_COMMENT_BOX,
                    'blockcomment':stc.STC_TCL_BLOCK_COMMENT
                }

XML_SYMBOLS = {     'default':stc.STC_H_DEFAULT,
                    'tag':stc.STC_H_TAG,
                    'tagunknown':stc.STC_H_TAGUNKNOWN,
                    'attribute':stc.STC_H_ATTRIBUTE,
                    'attributeunknown':stc.STC_H_ATTRIBUTEUNKNOWN,
                    'number':stc.STC_H_NUMBER,
                    'doublestring':stc.STC_H_DOUBLESTRING,
                    'singlestring':stc.STC_H_SINGLESTRING,
                    'other':stc.STC_H_OTHER,
                    'comment':stc.STC_H_COMMENT,
                    'entity':stc.STC_H_ENTITY,
                    'tagend':stc.STC_H_TAGEND,
                    'xmlstart':stc.STC_H_XMLSTART,
                    'xmlend':stc.STC_H_XMLEND,
                    'script':stc.STC_H_SCRIPT,
                    'asp':stc.STC_H_ASP,
                    'aspat':stc.STC_H_ASPAT,
                    'cdata':stc.STC_H_CDATA,
                    'question':stc.STC_H_QUESTION,
                    'value':stc.STC_H_VALUE,
                    'xccomment':stc.STC_H_XCCOMMENT,
                    'sgmldefault':stc.STC_H_SGML_DEFAULT,
                    'sgmlcommand':stc.STC_H_SGML_COMMAND,
                    'sgml1stparam':stc.STC_H_SGML_1ST_PARAM,
                    'sgmldoublestring':stc.STC_H_SGML_DOUBLESTRING,
                    'sgmlsimplestring':stc.STC_H_SGML_SIMPLESTRING,
                    'sgmlerror':stc.STC_H_SGML_ERROR,
                    'sgmlspecial':stc.STC_H_SGML_SPECIAL,
                    'sgmlentity':stc.STC_H_SGML_ENTITY,
                    'sgmlcomment':stc.STC_H_SGML_COMMENT,
                    'sgml1stparamcomment':stc.STC_H_SGML_1ST_PARAM_COMMENT,
                    'sgmlblockdefault':stc.STC_H_SGML_BLOCK_DEFAULT
                }


'''
symbols' map for all languages
'''
SYMBOLS = { stc.STC_LEX_NULL:NULL_SYMBOLS,
            stc.STC_LEX_ADA:ADA_SYMBOLS,
            stc.STC_LEX_APDL:APDL_SYMBOLS,
            stc.STC_LEX_ASM:ASM_SYMBOLS,
            stc.STC_LEX_ASN1:ASN1_SYMBOLS,
            stc.STC_LEX_AU3:AU3_SYMBOLS,
            stc.STC_LEX_AVE:AVE_SYMBOLS,
            stc.STC_LEX_BAAN:BAAN_SYMBOLS,
            stc.STC_LEX_BASH:BASH_SYMBOLS,
            stc.STC_LEX_CAML:CAML_SYMBOLS,
            stc.STC_LEX_CLW:CLW_SYMBOLS,
            stc.STC_LEX_CONF:CONF_SYMBOLS,
            stc.STC_LEX_CPP:CPP_SYMBOLS,
            stc.STC_LEX_CSOUND:CSOUND_SYMBOLS,
            stc.STC_LEX_CSS:CSS_SYMBOLS,
            stc.STC_LEX_HTML:HTML_SYMBOLS,
            stc.STC_LEX_PERL:PERL_SYMBOLS,
            stc.STC_LEX_PYTHON:PYTHON_SYMBOLS,
            stc.STC_LEX_RUBY:RUBY_SYMBOLS,
            stc.STC_LEX_XML:XML_SYMBOLS,
            stc.STC_LEX_SQL:None,
            stc.STC_LEX_VB:None,
            stc.STC_LEX_PROPERTIES:None,
            stc.STC_LEX_ERRORLIST:None,
            stc.STC_LEX_MAKEFILE:None,
            stc.STC_LEX_BATCH:BATCH_SYMBOLS,
            stc.STC_LEX_XCODE:None,
            stc.STC_LEX_LATEX:None,
            stc.STC_LEX_LUA:None,
            stc.STC_LEX_DIFF:None,
            stc.STC_LEX_PASCAL:None,
            stc.STC_LEX_LISP:None,
            stc.STC_LEX_EIFFEL:None,
            stc.STC_LEX_EIFFELKW:None,
            stc.STC_LEX_TCL:None,
            stc.STC_LEX_NNCRONTAB:None,
            stc.STC_LEX_VBSCRIPT:None,
            stc.STC_LEX_MATLAB:None,
            stc.STC_LEX_SCRIPTOL:None,
            stc.STC_LEX_FORTRAN:None,
            stc.STC_LEX_F77:None,
            stc.STC_LEX_POV:None,
            stc.STC_LEX_LOUT:None,
            stc.STC_LEX_ESCRIPT:None,
            stc.STC_LEX_PS:None,
            stc.STC_LEX_NSIS:None,
            stc.STC_LEX_MMIXAL:None,
            stc.STC_LEX_LOT:None,
            stc.STC_LEX_YAML:None,
            stc.STC_LEX_TEX:None,
            stc.STC_LEX_METAPOST:None,
            stc.STC_LEX_POWERBASIC:None,
            stc.STC_LEX_FORTH:None,
            stc.STC_LEX_ERLANG:None,
            stc.STC_LEX_OCTAVE:None,
            stc.STC_LEX_MSSQL:None,
            stc.STC_LEX_VERILOG:None,
            stc.STC_LEX_KIX:None,
            stc.STC_LEX_GUI4CLI:None,
            stc.STC_LEX_SPECMAN:None,
            stc.STC_LEX_VHDL:None,
            stc.STC_LEX_PUREBASIC:None,
            stc.STC_LEX_HASKELL:None,
            stc.STC_LEX_PHPSCRIPT:None,
            stc.STC_LEX_TADS3:None,
            stc.STC_LEX_REBOL:None,
            stc.STC_LEX_SMALLTALK:None,
            stc.STC_LEX_FLAGSHIP:None,
            stc.STC_LEX_FREEBASIC:None,
            stc.STC_LEX_INNOSETUP:None,
            stc.STC_LEX_OPAL:None,
            stc.STC_LEX_SPICE:None}