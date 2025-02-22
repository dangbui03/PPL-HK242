#2153289 - Bùi Hồ Hải Đăng
import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const AltName = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const AltName = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const AltName = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const AltName = [1.]TypeID{1, 3};","Error on line 1 col 17: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const AltName = Individual{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const AltName = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const AltName = 1[2] + foo()[2] + TypeID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const AltName = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const AltName = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var var1 int = foo() + 3 / 4;
            var var2 = "Hello" / 4;   
            var var3 StrType;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("const AltName = a.b() + 2;","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func AltName(a1 int, b1 int) int {return;}
            func AltName1() [2][3] TypeID {return;};        
            func AltName2() {return;}
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Compute) AltName(a1 int) int {return;};  
            func (c Compute) AltName() TypeID {return;}      
            func (c Compute) AltName(a1 int, b1 [2]AltName) {return;}
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type AltNameStruct struct {
                field1 string;
                field2 [1][3]AltNameStruct;
            }
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type AltNameStruct struct {}
        ""","Error on line 2 col 39: }", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Compute interface {
                
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]TypeID;
                Reset()
                
                SayHey(name string);
                
            }
            type AltNameInterface interface {}
        ""","Error on line 11 col 45: }", inspect.stack()[0].function))
                
    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""
            func AltName() {
                var var1 int = foo() + 3 / 4;
                var var2 = "Hello" / 4;   
                var var3 StrType;
                
                const AltName = a.b() + 2;
            }
        ""","successful", inspect.stack()[0].function))

    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""
            func AltName() {
                v1 := foo() + 3 / 4;
                v1.c[2][4] := 1 + 2;
            }
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""
            func AltName() {
                if (x > 10) {return; }
                if (x > 10) {
                  return;
                } else if (x == 10) {
                    var var3 StrType;
                } else {
                    var var3 TypeID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""
            func AltName() {
                for i1 < 10 {return; }
                for i1 := 0; i1 < 10; i1 += 1 {return; }
                for idx, val := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))

    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""
            func AltName() {
                for i1 < 10 {break;}
                break;
                continue;
                return 1;
                return;
                foo(2 + x, 4 / y); m.goo();
             }
        ""","successful", inspect.stack()[0].function))
       
    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const constA = 0b11;
        ""","successful", inspect.stack()[0].function))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = [true]int{1};
        ""","Error on line 2 col 32: true", inspect.stack()[0].function))
        
    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = [2]int{};
        ""","Error on line 2 col 38: }", inspect.stack()[0].function))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = TypeID {};
        ""","successful", inspect.stack()[0].function))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = TypeID {a: 2, b: 2 + 2 + TypeID {a: 1}};
        ""","successful", inspect.stack()[0].function))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = 1 && 2 && 3 || 1 || 1;
        ""","successful", inspect.stack()[0].function))
    
    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = a >= 2 <= "string" > a[2][3] < TypeID{A: 2} >= [2]TypeS{2};
        ""","successful", inspect.stack()[0].function))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = a.b.a.c.e.g;
        ""","successful", inspect.stack()[0].function))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = a[2][3][a + 2];
        ""","successful", inspect.stack()[0].function))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = a.a.a[2].foo(1);
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            var var3 AltName = foo().a[2].goo();
        ""","successful", inspect.stack()[0].function))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""
            const constK = -a + -!-!c - ---[2]int{2};
        ""","successful", inspect.stack()[0].function))

    def test_034(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var varC [2][3]TypeID
        ""","successful", inspect.stack()[0].function))

    def test_035(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const constA =;
        ""","Error on line 2 col 26: ;", inspect.stack()[0].function))
        
    def test_036(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Sum(a1 int, b1 [2]int) [2]TypeID {return ;}
        ""","successful", inspect.stack()[0].function))
        
    def test_037(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Sum() {return ;}
        ""","successful", inspect.stack()[0].function))
        
    def test_038(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute struct {
                val int;
                fieldA [2]int;
                fieldB [2]TypeID;
                c Compute
            }
        ""","successful", inspect.stack()[0].function))
        
    def test_039(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute struct {
                a int = 2;
            }
        ""","Error on line 3 col 22: =", inspect.stack()[0].function))
        
    def test_040(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute interface {
                Add(x, y [2]TypeID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
        ""","successful", inspect.stack()[0].function))
        
    def test_041(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute interface {Reset()}
        ""","Error on line 2 col 43: }", inspect.stack()[0].function))
        
    def test_042(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute interface {
                Add(x int, c, d TypeID); Add()
            }
        ""","successful", inspect.stack()[0].function))
        
    def test_043(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Sum(a1 int, b1 int) int {return ;};
        ""","successful", inspect.stack()[0].function))
        
    def test_044(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (obj int) Sum(a1 int) int {return ;}
        ""","Error on line 2 col 22: int", inspect.stack()[0].function))
        
    def test_045(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))

    def test_046(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                 var var1 int;
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_047(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                 var var1 = var1[2].b;
            };
        ""","successful", inspect.stack()[0].function))

    def test_048(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                a += 2;
                a -= a[2].b();
                a /= 2;
                a *= 2;
                a %= 2;
            };
        ""","successful", inspect.stack()[0].function))

    def test_049(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                a.c[2].e[3].k += 2;
            };
        ""","successful", inspect.stack()[0].function))

    def test_050(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                a.foo() += 2;
            };
        ""","Error on line 3 col 24: +=", inspect.stack()[0].function))

    def test_051(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
               a[2+3&&2] += foo().b[2];
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_052(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                if (x.foo().b[2]) {
                    a := 2;
                } else if (a && b) {
                    return;
                } else {
                    a := 2;
                }
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_053(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for true + 2 + foo().b {return; }
            };
        ""","successful", inspect.stack()[0].function))
   
    def test_054(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for i1 := 0; i1 < 10; i1 += 1 {
                   return;
                }
            };
        ""","successful", inspect.stack()[0].function))
    
    def test_055(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for idx, val := range 23 {return;
                }
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_056(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                break;
                continue;
                break; continue; break;
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_057(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                return;
                return 2 + a[2].b();
                return; return a;
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_058(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                a.foo(2 + 3, a {a:2});
                foo(2 + 3, a {a:2});
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_059(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                a[2][3].foo(2 + 3, a {a:2});
            };
        ""","successful", inspect.stack()[0].function))
        
    def test_060(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""
            const constA = [1]int{{1, 0x1}, TypeID{}, {{TypeID{}}}}
        ""","successful", inspect.stack()[0].function))
        
    def test_061(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for i[2] := 1; foo().a.b(); i := 1 {
                    return;
                }
            };
        ""","Error on line 3 col 25: :=", inspect.stack()[0].function))
        
    def test_062(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for var varB [2]TypeID = 1 + 2 / 4; foo().a.b(); i := 1 {
                    return;
                }
            };
        ""","successful", inspect.stack()[0].function))

    def test_063(self):
        self.assertTrue(TestParser.test("""
            const constA = [TypeID][2][TypeVT]int{{{1}}}
        ""","successful", inspect.stack()[0].function))

    def test_064(self):
        self.assertTrue(TestParser.test("""
            var varA;
        ""","Error on line 2 col 20: ;", inspect.stack()[0].function))
    def test_065(self):
        self.assertTrue(TestParser.test("""
            var varA = {1, 2};
        ""","Error on line 2 col 23: {", inspect.stack()[0].function))
    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute struct {val int}
        ""","Error on line 2 col 40: }", inspect.stack()[0].function))
    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            type Compute interface {Reset();} type Individual struct{val int;}
        ""","Error on line 2 col 46: type", inspect.stack()[0].function))
    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (obj c) Sum(a1 int, a2 int) {return ;}
        ""","successful", inspect.stack()[0].function))
    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (obj c) Sum(a1 int) {return ;};

            func Sum(a1 int) {return ;}; var varC int;

            var varC int; type Compute struct{c int;}; type Compute struct{c int;} var varC int;
        ""","Error on line 6 col 83: var", inspect.stack()[0].function))
    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            var varC int func (obj c) Sum(a1 int) {return ;}
        ""","Error on line 2 col 25: func", inspect.stack()[0].function))
    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            const constA = 2 func (obj c) Sum(a1 int) {return ;}
        ""","Error on line 2 col 29: func", inspect.stack()[0].function))
    def test_072(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for var varI [2] int = 0; foo().a.b(); varI[3] := 1 {
                    return;
                }
            };
        ""","Error on line 3 col 59: [", inspect.stack()[0].function))
    def test_073(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                return return 2 + a[2].b()
            };
        ""","Error on line 3 col 23: return", inspect.stack()[0].function))
    def test_074(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                break continue
            };
        ""","Error on line 3 col 22: continue", inspect.stack()[0].function))
    def test_075(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                return (2 + 3).b;
                return -1.c;
            };
        ""","Error on line 4 col 26: c", inspect.stack()[0].function))
    def test_076(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func (p Individual) Welcome() string {
                if (1) {return;}
                else if (1)
                {}
            };
        ""","Error on line 4 col 16: else", inspect.stack()[0].function))
    def test_077(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for var varB; foo().a.b(); i := 1 {
                    return;
                }
            };
        ""","Error on line 3 col 28: ;", inspect.stack()[0].function))
    def test_078(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Sum() {
                for var b int; foo().a.b(); i := 1 {
                    return;
                }
            };
        ""","Error on line 3 col 29: ;", inspect.stack()[0].function))
    def test_079(self):
        self.assertTrue(TestParser.test("""
            const constA = [TypeID][2][TypeVT]int{{{1}}, TypeID, a, {b}}
        ""","successful", inspect.stack()[0].function))
