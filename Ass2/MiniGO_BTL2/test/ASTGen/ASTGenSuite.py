# Bùi Hồ Hải Đăng - 2153289
import unittest
from TestUtils import TestAST
from AST import *
import inspect

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const Darkie = chu( 1 ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[IntLiteral(1)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        input = """const Darkie = chu( 1.0,true,false,nil,\"Darkie\" ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("\"Darkie\"")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const Darkie = chu( id ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[Id("id")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const Darkie = chu( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const Darkie = chu( a > b <= c ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        input = """const Darkie = chu( a[2][3] ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const Darkie = chu( a.b.c ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        input = """const Darkie = chu( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const Darkie = chu( a * (1+2) ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const Darkie = chu( Darkie {}, Darkie {a: 1} ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[StructLiteral("Darkie",[]),StructLiteral("Darkie",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const Darkie = chu( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl("Darkie",None,FuncCall("chu",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """
            var Darkie = 1;
            var Darkie int;
            var Votine int = 1;
"""
        expect = Program([VarDecl("Darkie", None,IntLiteral(1)),
			VarDecl("Darkie",IntType(), None),
			VarDecl("Votine",IntType(),IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """
            func chu() int {return;}
            func chu(a int, b int) {return;}
"""
        expect = Program([FuncDecl("chu",[],IntType(),Block([Return(None)])),
			FuncDecl("chu",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """
            func (Darkie v) chu(Darkie int) {return;}
"""
        expect = Program([MethodDecl("Darkie",Id("v"),FuncDecl("chu",[ParamDecl("Darkie",IntType())],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_015(self):
        input = """
            type Darkie struct {
                a int;
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_016(self):
        input = """
            type Darkie struct {
                a int;
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """
            func Darkie() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """
            func Darkie() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """
            func Darkie() {
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """
            func Darkie() {
                chu(1, 2);
                a[2].chu(1,3);
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([FuncCall("chu",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"chu",[IntLiteral(1),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """
            func Darkie() {
                if(1) {return;}
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """
            func Darkie() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """
            func Darkie() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), 
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_024(self):
        input = """
            func Darkie() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """
            func Darkie() {
                for index, value := range array[2] {return;}
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """
            const a = true + false - true;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_027(self):
        input = """
            const a = 1 && 2 || 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        input = """
            const a = 1 + 2 && 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_029(self):
        input = """
            const a = 1 - 2 % 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_030(self):
        input = """
            const a = 1 + -2 - 1;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_031(self):
        input = """
            const a = [1]ID{Darkie{}};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("Darkie",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_032(self):
        input = """
            const a = [1][3]float{1.0e+2};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral("1.0e+2")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_033(self):
        input = """
            const a = ID{a: 1, b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_034(self):
        input = """
            const a = ID{a: [1]int{1}};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_035(self):
        input = """
            const a = ID{b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_036(self):
        input = """
            const a = 0 && 1 && 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("&&", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_037(self):
        input = """
            const a = 0 || 1 || 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_038(self):
        input = """
            const a = 0 >= 1 <= 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_039(self):
        input = """
            const a = 0 + 1 - 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_040(self):
        input = """
            const a = 0 * 1 / 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("/", BinaryOp("*", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_041(self):
        input = """
            const a = !-!2;
"""
        expect = Program([ConstDecl("a",None,UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2)))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_042(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_043(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_044(self):
        input = """
            const a = 1 >= 2 + 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_045(self):
        input = """
            const a = a[1][2][3][4];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_046(self):
        input = """
            const a = a[1 + 2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_047(self):
        input = """
            const a = a.b.c.d.e;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_048(self):
        input = """
            const a = ID {}.a;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(StructLiteral("ID",[]),"a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_049(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_050(self):
        input = """
            const a = a.b().c().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_051(self):
        input = """
            const a = a().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(FuncCall("a",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_052(self):
        input = """
            const a = a[1].b.c()[2].d.e();
"""
        expect = Program([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_053(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("\"a\""))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_054(self):
        input = """
            const a = f() + f(1 + 2, 3.);
"""
        expect = Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral("3.")])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_055(self):
        input = """
            const a = chu()[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FuncCall("chu",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_056(self):
        input = """
            const a = a;
"""
        expect = Program([ConstDecl("a",None,Id("a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_057(self):
        input = """
            var a Darkie = 1.;
"""
        expect = Program([VarDecl("a",Id("Darkie"),FloatLiteral("1."))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_058(self):
        "thêm type array vào AST anh có thông bao trong nhóm task 3"
        input = """
            var a [2][3]int;
"""
        expect = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_059(self):
        input = """
            var a = 1;
"""
        expect = Program([VarDecl("a", None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_060(self):
        input = """
            type Darkie struct {
                a int;
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_061(self):
        input = """
            type Darkie struct {
                a int;
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_062(self):
        input = """
            type Darkie struct {
                a  int;
                b  boolean;
                
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType()),("b",BoolType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_063(self):
        input = """
            type Darkie struct {
                a  int;
                b  boolean;
                c  [2]Darkie;
            }
"""
        expect = Program([StructType("Darkie",[("a",IntType()),("b",BoolType()),("c",ArrayType([IntLiteral(2)],Id("Darkie")))],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_064(self):
        input = """
            type Darkie interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_065(self):
        input = """
            type Darkie interface {
                Add(a int) ;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_066(self):
        input = """
            type Darkie interface {
                Add(a int, b int) ;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_067(self):
        input = """
            type Darkie interface {
                Add(a, c int, b int) ;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[IntType(),IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_068(self):
        input = """
            type Darkie interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_069(self):
        input = """
            type Darkie interface {
                Add() [2]string;
                Add() ID;
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_070(self):
        input = """
            type Darkie interface {
                Add();
            }
"""
        expect = Program([InterfaceType("Darkie",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_071(self):
        input = """
            func chu() {return;}
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_072(self):
        input = """
            func chu(a [2]ID) {return;}
"""
        expect = Program([FuncDecl("chu",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_073(self):
        input = """
            func chu(a int, b [1]int) {return;}
"""
        expect = Program([FuncDecl("chu",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_074(self):
        input = """
            func chu() [2]int {return;}
"""
        expect = Program([FuncDecl("chu",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_075(self):
        input = """
            func (Cat c) chu() {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("chu",[],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_076(self):
        input = """
            func  (Cat c) chu(a [2]ID) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("chu",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_077(self):
        input = """
            func  (Cat c) chu(a int, b [1]int) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("chu",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_078(self):
        input = """
            func  (Cat c) chu() [2]int {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("chu",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_079(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {chu();} 
            func chu(){return;}
            func  (Cat c) chu() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("chu",[],VoidType())]),
			FuncDecl("chu",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("chu",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_080(self):
        input = """
            func chu(a,b,c,d [ID][2][c] ID ){return;}
"""
        expect = Program([FuncDecl("chu",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_081(self):
        input = """
            func chu(){
                const a = 1.;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral("1."))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_082(self):
        input = """
            func chu(){
                var a = 1.;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([VarDecl("a", None,FloatLiteral("1."))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_083(self):
        input = """
            func chu(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_084(self):
        input = """
            func chu(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_085(self):
        input = """
            func chu(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_086(self):
        input = """
            func chu(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_087(self):
        input = """
            func chu(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_088(self):
        input = """
            func chu(){
                a["s"][chu()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("chu",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_089(self):
        input = """
            func chu(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_090(self):
        input = """
            func chu(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_091(self):
        input = """
            func chu(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_092(self):
        input = """
            func chu(){
                return;
                return chu() + 2;
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("chu",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_093(self):
        input = """
            func chu(){
                chu();
                chu(chu(), 2);
                a.chu();
                a[2].c.chu(chu(), 2);
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([FuncCall("chu",[]),FuncCall("chu",[FuncCall("chu",[]),IntLiteral(2)]),MethCall(Id("a"),"chu",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"chu",[FuncCall("chu",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_094(self):
        input = """
            func chu(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_095(self):
        input = """
            func chu(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_096(self):
        input = """
            func chu(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("chu",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_097(self):
        input = """
            func Darkie() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_098(self):
        input = """
            func Darkie() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_099(self):
        input = """
            func Darkie() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_100(self):
        input = """
            func Darkie() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
"""
        expect = Program([FuncDecl("Darkie",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("\"2\"")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("\"THANKS YOU, PPL1 \""))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
