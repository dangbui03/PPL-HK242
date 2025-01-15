# Generated from d:/HCMUT/PPL/2/BTL1/Ass1/MiniGO_BTL1/main/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,67,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,3,2,24,8,2,1,2,1,2,1,2,3,2,
        29,8,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,3,5,40,8,5,1,5,1,5,
        1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,11,14,41,0,12,1,0,0,0,2,14,1,0,0,
        0,4,30,1,0,0,0,6,32,1,0,0,0,8,36,1,0,0,0,10,39,1,0,0,0,12,13,5,0,
        0,1,13,1,1,0,0,0,14,15,5,8,0,0,15,16,5,52,0,0,16,17,5,9,0,0,17,18,
        5,46,0,0,18,19,3,4,2,0,19,20,5,47,0,0,20,3,1,0,0,0,21,23,3,6,3,0,
        22,24,3,10,5,0,23,22,1,0,0,0,23,24,1,0,0,0,24,31,1,0,0,0,25,26,3,
        6,3,0,26,28,3,4,2,0,27,29,3,10,5,0,28,27,1,0,0,0,28,29,1,0,0,0,29,
        31,1,0,0,0,30,21,1,0,0,0,30,25,1,0,0,0,31,5,1,0,0,0,32,33,5,52,0,
        0,33,34,3,8,4,0,34,35,5,50,0,0,35,7,1,0,0,0,36,37,7,0,0,0,37,9,1,
        0,0,0,38,40,5,1,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,
        42,5,2,0,0,42,11,1,0,0,0,4,23,28,30,39
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\r'", "'\\n'", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'nil'", 
                     "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'!'", "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                      "ADD", "MINUS", "MULT", "DIV", "REM", "EQUAL", "DIFF", 
                      "LT", "GT", "LE", "GE", "OR", "FACT", "AND", "ASSIGN", 
                      "ADD_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
                      "REM_ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "ID", 
                      "FLOAT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
                      "INT_LIT", "STR_LIT", "BOOL_LIT", "NIL_LIT", "WS", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_struct_decl = 1
    RULE_list_field = 2
    RULE_field = 3
    RULE_type = 4
    RULE_newline = 5

    ruleNames =  [ "program", "struct_decl", "list_field", "field", "type", 
                   "newline" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    NIL=20
    TRUE=21
    FALSE=22
    ADD=23
    MINUS=24
    MULT=25
    DIV=26
    REM=27
    EQUAL=28
    DIFF=29
    LT=30
    GT=31
    LE=32
    GE=33
    OR=34
    FACT=35
    AND=36
    ASSIGN=37
    ADD_ASSIGN=38
    MINUS_ASSIGN=39
    MULT_ASSIGN=40
    DIV_ASSIGN=41
    REM_ASSIGN=42
    DOT=43
    LPAREN=44
    RPAREN=45
    LBRACE=46
    RBRACE=47
    LBRACK=48
    RBRACK=49
    SEMI=50
    COMMA=51
    ID=52
    FLOAT_LIT=53
    DEC_LIT=54
    BIN_LIT=55
    OCT_LIT=56
    HEX_LIT=57
    INT_LIT=58
    STR_LIT=59
    BOOL_LIT=60
    NIL_LIT=61
    WS=62
    LINE_COMMENT=63
    BLOCK_COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(MiniGoParser.TYPE)
            self.state = 15
            self.match(MiniGoParser.ID)
            self.state = 16
            self.match(MiniGoParser.STRUCT)
            self.state = 17
            self.match(MiniGoParser.LBRACE)
            self.state = 18
            self.list_field()
            self.state = 19
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def newline(self):
            return self.getTypedRuleContext(MiniGoParser.NewlineContext,0)


        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field




    def list_field(self):

        localctx = MiniGoParser.List_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_field)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.field()
                self.state = 23
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.newline()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.field()
                self.state = 26
                self.list_field()
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 27
                    self.newline()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MiniGoParser.ID)
            self.state = 33
            self.type_()
            self.state = 34
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type




    def type_(self):

        localctx = MiniGoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_newline




    def newline(self):

        localctx = MiniGoParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 38
                self.match(MiniGoParser.T__0)


            self.state = 41
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





