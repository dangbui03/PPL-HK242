"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"}","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3}","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30}","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + x[2] + ID[2].b.b","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2]","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo()","successful", inspect.stack()[0].function))
    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const a = 0b11;                         
        ""","successful", inspect.stack()[0].function))
    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN 1;                         
        ""","Error on line 2 col 25: 1", inspect.stack()[0].function))
    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 27: int", inspect.stack()[0].function))
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))
    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", inspect.stack()[0].function))
    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        ""","successful", inspect.stack()[0].function))
    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k =  (1, 2);                         
        ""","Error on line 2 col 25: ,", inspect.stack()[0].function))
    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var c [2][3]ID
        ""","Error on line 2 col 26: \n", inspect.stack()[0].function))
    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))
    def test_069(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                func Add(x int, y [2]int) [2]id {}
    ""","successful", inspect.stack()[0].function))
    def test_071(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                func Add(a) [2]id {}
    ""","Error on line 2 col 22: )", inspect.stack()[0].function))
    def test_077(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                type Calculator struct {
                                            
                    value int;
                    a [2]int; a [2]ID;
                    c Calculator                    
                }
    ""","successful", inspect.stack()[0].function))
    def test_078(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                type Calculator struct {
                    c Calculator
                    c Cal a int;         
                }
    ""","Error on line 4 col 22: a", inspect.stack()[0].function))
    def test_084(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                type Calculator interface {
                    Add(x int,c,d ID); Add()
            }
    ""","successful", inspect.stack()[0].function))
    def test_086(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                type Calculator interface {}
                type Person struct{};
    ""","successful", inspect.stack()[0].function))
    def test_087(self):
            """Declared"""
            self.assertTrue(TestParser.test("""    
                type Calculator interface {};
    ""","successful", inspect.stack()[0].function))
    def test_091(self):
            """Declared"""
            self.assertTrue(TestParser.test("""
                func (c c) Add(x, c int) {}
    ""","Error on line 2 col 28: ,", inspect.stack()[0].function))
    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                        func Add(){
                                            const a = a[2].b
                                            var a = a[2].b; var a = "s";
                                        }""","successful", inspect.stack()[0].function))
    def test_095(self):
            """Declared"""
            self.assertTrue(TestParser.test("""
                                            
                func (c c) Add(x int) {}
                                            
                func Add(x int) {} var c int;
                                            
                var c int; type Calculator struct{} type Calculator struct{} var c int;
    ""","Error on line 7 col 48: type", inspect.stack()[0].function))