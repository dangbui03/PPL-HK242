import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_001(self):
        self.assertTrue(TestLexer.test("if", "if,<EOF>", inspect.stack()[0].function))
    def test_002(self):
        self.assertTrue(TestLexer.test("+", "+,<EOF>", inspect.stack()[0].function))
    def test_003(self):
        self.assertTrue(TestLexer.test("[]", "[,],<EOF>", inspect.stack()[0].function))
    def test_004(self):
        self.assertTrue(TestLexer.test("_AnotherName", "_AnotherName,<EOF>", inspect.stack()[0].function))
    def test_005(self):
        self.assertTrue(TestLexer.test("34", "34,<EOF>", inspect.stack()[0].function))
    def test_006(self):
        self.assertTrue(TestLexer.test("0x1A", "0x1A,<EOF>", inspect.stack()[0].function))
    def test_007(self):
        self.assertTrue(TestLexer.test("7.8e-2", "7.8e-2,<EOF>", inspect.stack()[0].function))
    def test_008(self):
        self.assertTrue(TestLexer.test(""" "AnotherName \\r" """, "\"AnotherName \\r\",<EOF>", inspect.stack()[0].function))
    def test_009(self):
        self.assertTrue(TestLexer.test("// AnotherName", "<EOF>", inspect.stack()[0].function))
    def test_010(self):
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA", "SHIBA,<EOF>", inspect.stack()[0].function))
    def test_011(self):
        self.assertTrue(TestLexer.test("^", "ErrorToken ^", inspect.stack()[0].function))
    def test_012(self):
        self.assertTrue(TestLexer.test(""" "AnotherName\n" """, "Unclosed string: \"AnotherName", inspect.stack()[0].function))
    def test_013(self):
        self.assertTrue(TestLexer.test(""" "AnotherName\\f" """, "Illegal escape in string: \"AnotherName\\f", inspect.stack()[0].function))
    def test_014(self):
        inp = "else for return func type struct interface string int float boolean const var continue break range nil true false"
        exp = "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_015(self):
        inp = "+ - * / % == != > < <= >= && || ! = += -= *= /= %= :="
        exp = "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_016(self):
        self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))
    def test_017(self):
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))
    def test_018(self):
        self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))
    def test_019(self):
        self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))
    def test_020(self):
        self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))
    def test_021(self):
        self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))
    def test_022(self):
        self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))
    def test_023(self):
        self.assertTrue(TestLexer.test("-0789", "-,0,789,<EOF>", inspect.stack()[0].function))
    def test_024(self):
        self.assertTrue(TestLexer.test("0b110", "0b110,<EOF>", inspect.stack()[0].function))
    def test_025(self):
        self.assertTrue(TestLexer.test("0b2f", "0,b2f,<EOF>", inspect.stack()[0].function))
    def test_026(self):
        self.assertTrue(TestLexer.test("-0O55", "-,0O55,<EOF>", inspect.stack()[0].function))
    def test_027(self):
        self.assertTrue(TestLexer.test("0xaf0", "0xaf0,<EOF>", inspect.stack()[0].function))
    def test_028(self):
        self.assertTrue(TestLexer.test("111.222e-033", "111.222e-033,<EOF>", inspect.stack()[0].function))
    def test_029(self):
        self.assertTrue(TestLexer.test("2.5Ee3", "2.5,Ee3,<EOF>", inspect.stack()[0].function))
    def test_030(self):
        self.assertTrue(TestLexer.test("00.3e4", "00.3e4,<EOF>", inspect.stack()[0].function))
    def test_031(self):
        self.assertTrue(TestLexer.test(""" "anothername" """, "\"anothername\",<EOF>", inspect.stack()[0].function))
    def test_032(self):
        self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))
    def test_033(self):
        self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))
    def test_034(self):
        self.assertTrue(TestLexer.test(" ^ ", "ErrorToken ^", inspect.stack()[0].function))
    def test_035(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", inspect.stack()[0].function))
    def test_036(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", inspect.stack()[0].function))
    def test_037(self):
        self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))
    def test_038(self):
        self.assertTrue(TestLexer.test("?", "ErrorToken ?", inspect.stack()[0].function))
    def test_039(self):
        self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))
    def test_040(self):
        self.assertTrue(TestLexer.test(""" 123" """, "123,Unclosed string: \" ", inspect.stack()[0].function))
    def test_041(self):
        self.assertTrue(TestLexer.test(""" "123
        " """, "Unclosed string: \"123", inspect.stack()[0].function))
    def test_042(self):
        self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))
    def test_043(self):
        self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))
    def test_044(self):
        inp = """
            else
            }
            ]
            )
        """
        exp = "else,},;,],;,),;,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_045(self):
        inp = """
            nil
        """
        self.assertTrue(TestLexer.test(inp, "nil,;,<EOF>", inspect.stack()[0].function))

    def test_046(self):
        self.assertTrue(TestLexer.test("if", "if,<EOF>", inspect.stack()[0].function))
    def test_047(self):
        self.assertTrue(TestLexer.test("+", "+,<EOF>", inspect.stack()[0].function))
    def test_048(self):
        self.assertTrue(TestLexer.test("[]", "[,],<EOF>", inspect.stack()[0].function))
    def test_049(self):
        self.assertTrue(TestLexer.test("_AnotherName", "_AnotherName,<EOF>", inspect.stack()[0].function))
    def test_050(self):
        self.assertTrue(TestLexer.test("34", "34,<EOF>", inspect.stack()[0].function))
    def test_051(self):
        self.assertTrue(TestLexer.test("0x1A", "0x1A,<EOF>", inspect.stack()[0].function))
    def test_052(self):
        self.assertTrue(TestLexer.test("7.8e-2", "7.8e-2,<EOF>", inspect.stack()[0].function))
    def test_053(self):
        self.assertTrue(TestLexer.test(""" "AnotherName \\r" """, "\"AnotherName \\r\",<EOF>", inspect.stack()[0].function))
    def test_054(self):
        self.assertTrue(TestLexer.test("// AnotherName", "<EOF>", inspect.stack()[0].function))
    def test_055(self):
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA", "SHIBA,<EOF>", inspect.stack()[0].function))
    def test_056(self):
        self.assertTrue(TestLexer.test("^", "ErrorToken ^", inspect.stack()[0].function))
    def test_057(self):
        self.assertTrue(TestLexer.test(""" "AnotherName\n" """, "Unclosed string: \"AnotherName", inspect.stack()[0].function))
    def test_058(self):
        self.assertTrue(TestLexer.test(""" "AnotherName\\f" """, "Illegal escape in string: \"AnotherName\\f", inspect.stack()[0].function))
    def test_059(self):
        inp = "else for return func type struct interface string int float boolean const var continue break range nil true false"
        exp = "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_060(self):
        inp = "+ - * / % == != > < <= >= && || ! = += -= *= /= %= :="
        exp = "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_061(self):
        self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))
    def test_062(self):
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))
    def test_063(self):
        self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))
    def test_064(self):
        self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))
    def test_065(self):
        self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))
    def test_066(self):
        self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))
    def test_067(self):
        self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))
    def test_068(self):
        self.assertTrue(TestLexer.test("-07999999", "-,0,7999999,<EOF>", inspect.stack()[0].function))
    def test_069(self):
        self.assertTrue(TestLexer.test("0b110", "0b110,<EOF>", inspect.stack()[0].function))
    def test_070(self):
        self.assertTrue(TestLexer.test("0b6f", "0,b6f,<EOF>", inspect.stack()[0].function))
    def test_071(self):
        self.assertTrue(TestLexer.test("-0O55", "-,0O55,<EOF>", inspect.stack()[0].function))
    def test_072(self):
        self.assertTrue(TestLexer.test("0xaf0", "0xaf0,<EOF>", inspect.stack()[0].function))
    def test_073(self):
        self.assertTrue(TestLexer.test("111.222e-033", "111.222e-033,<EOF>", inspect.stack()[0].function))
    def test_074(self):
        self.assertTrue(TestLexer.test("2.5Ee3", "2.5,Ee3,<EOF>", inspect.stack()[0].function))
    def test_075(self):
        self.assertTrue(TestLexer.test("00.3e4", "00.3e4,<EOF>", inspect.stack()[0].function))
    def test_076(self):
        self.assertTrue(TestLexer.test(""" "anothername" """, "\"anothername\",<EOF>", inspect.stack()[0].function))
    def test_077(self):
        self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))
    def test_078(self):
        self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))
    def test_079(self):
        self.assertTrue(TestLexer.test(" ^ ", "ErrorToken ^", inspect.stack()[0].function))
    def test_080(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", inspect.stack()[0].function))
    def test_081(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", inspect.stack()[0].function))
    def test_082(self):
        self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))
    def test_083(self):
        self.assertTrue(TestLexer.test("?", "ErrorToken ?", inspect.stack()[0].function))
    def test_084(self):
        self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))
    def test_085(self):
        self.assertTrue(TestLexer.test(""" 123" """, "123,Unclosed string: \" ", inspect.stack()[0].function))
    def test_086(self):
        self.assertTrue(TestLexer.test(""" "123
        " """, "Unclosed string: \"123", inspect.stack()[0].function))
    def test_087(self):
        self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))
    def test_088(self):
        self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))
    def test_089(self):
        inp = """
            if
            }
            ]
            )
        """
        exp = "if,},;,],;,),;,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, inspect.stack()[0].function))
    def test_090(self):
        inp = """
            nil
        """
        self.assertTrue(TestLexer.test(inp, "nil,;,<EOF>", inspect.stack()[0].function))
