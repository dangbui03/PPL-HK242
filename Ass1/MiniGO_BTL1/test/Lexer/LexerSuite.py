"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))
        
    def test_014(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" 
            const a = 2;
""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))
    def test_015(self):
        """skip"""
        self.assertTrue(TestLexer.test(""" /*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", inspect.stack()[0].function))
    def test_030(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-20", "0,10.010e-20,<EOF>", inspect.stack()[0].function))

    def test_053(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))
    def test_073(self):
        """Keywords"""
        self.assertTrue(TestLexer.test(""" // /*
                                       */""", "\n,*,/,<EOF>", inspect.stack()[0].function))
    #!!! 87 test yêu cầu code chấm sau
