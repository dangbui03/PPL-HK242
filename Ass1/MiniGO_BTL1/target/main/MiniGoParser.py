# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\f\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\3\2\3\2\2\2\3")
        buf.write("\2\2\2\2\13\2\5\3\2\2\2\4\6\7\3\2\2\5\4\3\2\2\2\6\7\3")
        buf.write("\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\t\3\2\2\2\t\n\7\2\2\3")
        buf.write("\n\3\3\2\2\2\3\7")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'votien'", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'nil'", 
                     "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'!'", "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "TRUE", "FALSE", "ADD", "MINUS", "MULT", 
                      "DIV", "REM", "EQUAL", "DIFF", "LT", "GT", "LE", "GE", 
                      "OR", "FACT", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
                      "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMI", "COMMA", "ID", "FLOAT_LIT", "DEC_LIT", 
                      "BIN_LIT", "OCT_LIT", "HEX_LIT", "INT_LIT", "STR_LIT", 
                      "BOOL_LIT", "NIL_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    CONST=14
    VAR=15
    CONTINUE=16
    BREAK=17
    RANGE=18
    NIL=19
    TRUE=20
    FALSE=21
    ADD=22
    MINUS=23
    MULT=24
    DIV=25
    REM=26
    EQUAL=27
    DIFF=28
    LT=29
    GT=30
    LE=31
    GE=32
    OR=33
    FACT=34
    AND=35
    ASSIGN=36
    ADD_ASSIGN=37
    MINUS_ASSIGN=38
    MULT_ASSIGN=39
    DIV_ASSIGN=40
    REM_ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    SEMI=49
    COMMA=50
    ID=51
    FLOAT_LIT=52
    DEC_LIT=53
    BIN_LIT=54
    OCT_LIT=55
    HEX_LIT=56
    INT_LIT=57
    STR_LIT=58
    BOOL_LIT=59
    NIL_LIT=60
    WS=61
    LINE_COMMENT=62
    BLOCK_COMMENT=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(MiniGoParser.T__0)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.T__0):
                    break

            self.state = 7
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





