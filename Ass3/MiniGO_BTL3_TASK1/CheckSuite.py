# 2153289 - Bùi Hồ Hải Đăng
import unittest
from TestUtils import TestChecker
from AST import *
import inspect


class CheckSuite(unittest.TestCase):
    def test_001(self):
        input = Program([VarDecl("HAIDANG", None, IntLiteral(1)),
                         VarDecl("HAIDANG", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: HAIDANG", inspect.stack()[0].function))

    def test_002(self):
        input = Program([VarDecl("HAIDANG", None, IntLiteral(1)),
                         ConstDecl("HAIDANG", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Constant: HAIDANG", inspect.stack()[0].function))

    def test_003(self):
        input = Program([ConstDecl("HAIDANG", None, IntLiteral(1)),
                         VarDecl("HAIDANG", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: HAIDANG", inspect.stack()[0].function))

    def test_004(self):
        input = Program([ConstDecl("HAIDANG", None, IntLiteral(1)),
                         FuncDecl("HAIDANG", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Function: HAIDANG", inspect.stack()[0].function))

    def test_005(self):
        input = Program([FuncDecl("HAIDANG", [], VoidType(), Block([Return(None)])),
                         VarDecl("HAIDANG", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: HAIDANG", inspect.stack()[0].function))

    def test_006(self):
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: getInt", inspect.stack()[0].function))

    def test_007(self):
        input = Program([StructType("HAIDANG", [("HAIDANG", IntType())], []),
                         StructType("TIEN", [("HAIDANG", StringType()), ("TIEN", IntType()), ("TIEN", FloatType())], [])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Field: TIEN", inspect.stack()[0].function))

    def test_008(self):
        input = Program([MethodDecl("v", Id("TIEN"),
                         FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
                         StructType("TIEN", [("HAIDANG", IntType())], [])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Method: getInt", inspect.stack()[0].function))

    def test_009(self):
        input = Program([InterfaceType("HAIDANG", [Prototype("HAIDANG", [], VoidType()),
                                                   Prototype("HAIDANG", [IntType()], VoidType())])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Prototype: HAIDANG", inspect.stack()[0].function))

    def test_010(self):
        input = Program([FuncDecl("HAIDANG", [ParamDecl("a", IntType()), ParamDecl("a", IntType())],
                         VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_011(self):
        input = Program([FuncDecl("HAIDANG", [ParamDecl("b", IntType())],
                         VoidType(), Block([VarDecl("b", None, IntLiteral(1)),
                                            VarDecl("a", None, IntLiteral(1)),
                                            ConstDecl("a", None, IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_012(self):
        input = Program([FuncDecl("HAIDANG", [ParamDecl("b", IntType())],
                         VoidType(), Block([ForStep(VarDecl("a", None, IntLiteral(1)),
                                                    BinaryOp(
                                                        "<", Id("a"), IntLiteral(1)),
                                                    Assign(Id("a"), BinaryOp(
                                                        "+", Id("a"), IntLiteral(1))),
                                                    Block([ConstDecl("a", None, IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_013(self):
        input = Program([VarDecl("a", None, IntLiteral(1)),
                         VarDecl("b", None, Id("a")),
                         VarDecl("c", None, Id("d"))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_014(self):
        input = Program([FuncDecl("HAIDANG", [], IntType(), Block([Return(IntLiteral(1))])),
                         FuncDecl("foo", [], VoidType(), Block([VarDecl("b", None, FuncCall("HAIDANG", [])),
                                                                FuncCall(
                                                                    "foo_HAIDANG", []),
                                                                Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Function: foo_HAIDANG", inspect.stack()[0].function))

    def test_015(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("getInt", [], VoidType(),
                                  Block([ConstDecl("c", None, FieldAccess(Id("v"), "HAIDANG")),
                                         VarDecl("d", None, FieldAccess(Id("v"), "tien"))])))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_016(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []), MethodDecl("v", Id("TIEN"), FuncDecl(
            "getInt", [], VoidType(), Block([MethCall(Id("v"), "getInt", []), MethCall(Id("v"), "putInt", [])])))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_017(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []),
                         StructType("TIEN", [("v", IntType())], [])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_018(self):
        input = Program(
            [FuncDecl("putInt", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Function: putInt", inspect.stack()[0].function))

    def test_019(self):
        input = Program(
            [FuncDecl("getString", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Function: getString", inspect.stack()[0].function))

    def test_020(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("foo", [ParamDecl("v", IntType())], VoidType(), Block([Return(None)]))),
                         FuncDecl("foo", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_021(self):
        input = Program([ConstDecl("a", None, IntLiteral(2)),
                         FuncDecl("foo", [], VoidType(), Block([ConstDecl("a", None, IntLiteral(1)),
                                                                ForStep(VarDecl("a", None, IntLiteral(1)),
                                                                        BinaryOp(
                                                                            "<", Id("a"), IntLiteral(1)),
                                                                        Assign(
                                                                            Id("b"), IntLiteral(2)),
                                                                        Block([ConstDecl("b", None, IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Constant: b", inspect.stack()[0].function))

    def test_022(self):
        input = Program([ConstDecl("a", None, IntLiteral(2)),
                         FuncDecl("foo", [], VoidType(), Block([ConstDecl("a", None, IntLiteral(1)),
                                                                ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),
                                                                         Block([ConstDecl("a", None, IntLiteral(1)),
                                                                                ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),
                                                                                         Block([ConstDecl("a", None, IntLiteral(1)),
                                                                                                ConstDecl("b", None, IntLiteral(1))])),
                                                                                ConstDecl(
                                                                             "b", None, IntLiteral(1)),
                                                                             VarDecl("a", None, IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_023(self):
        input = Program([FuncDecl("foo", [], VoidType(), Block([VarDecl("a", None, IntLiteral(1)),
                                                                VarDecl(
                                                                    "b", None, IntLiteral(1)),
                                                                ForEach(Id("a"), Id("b"),
                                                                        ArrayLiteral([IntLiteral(3)], IntType(),
                                                                                     [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                                        Block([VarDecl("b", None, IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_024(self):
        input = Program([VarDecl("a", None, FuncCall("foo", [])),
                         FuncDecl("foo", [], IntType(), Block([VarDecl("a", None, FuncCall("koo", [])),
                                                               VarDecl("c", None, FuncCall(
                                                                   "getInt", [])),
                                                               FuncCall(
                                                                   "putInt", [Id("c")]),
                                                               FuncCall(
                                                                   "putIntLn", [Id("c")]),
                                                               Return(IntLiteral(1))])),
                         VarDecl("d", None, FuncCall("foo", [])),
                         FuncDecl("koo", [], IntType(), Block([VarDecl("a", None, FuncCall("foo", [])),
                                                               Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_025(self):
        input = Program([VarDecl("v", Id("TIEN"), None),
                         ConstDecl("b", None, FieldAccess(Id("v"), "b")),
                         StructType(
                             "TIEN", [("a", IntType()), ("b", IntType()), ("c", IntType())], []),
                         ConstDecl("a", None, FieldAccess(Id("v"), "a")),
                         ConstDecl("e", None, FieldAccess(Id("v"), "e"))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Field: e", inspect.stack()[0].function))

    def test_026(self):
        input = Program([VarDecl("v", IntType(), FloatLiteral(1.2))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: VarDecl("v",IntType(),FloatLiteral(1.2))""",
                                         inspect.stack()[0].function))

    def test_027(self):
        input = Program([StructType("S1", [("HAIDANG", IntType())], []),
                         StructType("S2", [("HAIDANG", IntType())], []),
                         InterfaceType(
                             "I1", [Prototype("HAIDANG", [], VoidType())]),
                         InterfaceType(
                             "I2", [Prototype("HAIDANG", [], VoidType())]),
                         MethodDecl("s", Id("S1"), FuncDecl(
                             "HAIDANG", [], VoidType(), Block([Return(None)]))),
                         VarDecl("a", Id("S1"), None),
                         VarDecl("b", Id("S2"), None),
                         VarDecl("c", Id("I1"), Id("a")),
                         VarDecl("d", Id("I2"), Id("b"))])
        self.assertTrue(TestChecker.test(input,
                                         """Redeclared Method: HAIDANG""",
                                         inspect.stack()[0].function))

    def test_028(self):
        input = Program([StructType("S1", [("HAIDANG", IntType())], []),
                         StructType("S2", [("HAIDANG", IntType())], []),
                         InterfaceType(
                             "I1", [Prototype("HAIDANG", [], VoidType())]),
                         InterfaceType(
                             "I2", [Prototype("HAIDANG", [], IntType())]),
                         MethodDecl("s", Id("S1"), FuncDecl(
                             "HAIDANG", [], VoidType(), Block([Return(None)]))),
                         VarDecl("a", Id("S1"), None),
                         VarDecl("b", Id("S2"), None),
                         VarDecl("c", Id("I2"), Id("a"))])
        self.assertTrue(TestChecker.test(input,
                                         """Redeclared Method: HAIDANG""",
                                         inspect.stack()[0].function))

    def test_029(self):
        input = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)])),
                         FuncDecl("foo1", [], IntType(), Block(
                             [Return(IntLiteral(1))])),
                         FuncDecl("foo2", [], FloatType(), Block([Return(IntLiteral(2))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: Return(IntLiteral(2))""",
                                         inspect.stack()[0].function))

    def test_030(self):
        input = Program([StructType("S1", [("v", IntType()), ("t", IntType())], []),
                         VarDecl("a", None, StructLiteral(
                             "S1", [("v", IntLiteral(1)), ("t", IntLiteral(2))])),
                         VarDecl("b", Id("S1"), Id("a")),
                         VarDecl("c", IntType(), Id("b"))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: VarDecl("c",IntType(),Id("b"))""",
                                         inspect.stack()[0].function))

    def test_031(self):
        input = Program([VarDecl("a", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
                         VarDecl("c", ArrayType([IntLiteral(3), IntLiteral(2)], IntType()), Id("a"))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),Id("a"))""",
                                         inspect.stack()[0].function))

    def test_032(self):
        input = Program([VarDecl("a", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
                         VarDecl("c", ArrayType([IntLiteral(2)], FloatType()), Id("a"))])
        self.assertTrue(TestChecker.test(input,
                                         """HAIDANG""",
                                         inspect.stack()[0].function))

    def test_033(self):

        input = Program([VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
                         VarDecl("b", None, ArrayCell(
                             Id("a"), [IntLiteral(1), IntLiteral(2)])),
                         VarDecl("c", IntType(), Id("b")),
                         VarDecl("d", ArrayType([IntLiteral(1)], StringType()), Id("b"))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))""",
                                         inspect.stack()[0].function))

    def test_034(self):
        input = Program([VarDecl("a", None, BinaryOp("+", StringLiteral("1"), StringLiteral("2"))),
                         VarDecl("c", StringType(), Id("a")),
                         VarDecl("b", None, BinaryOp("+", StringLiteral("1"), IntLiteral(1)))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: BinaryOp("+", StringLiteral("1"), IntLiteral(1))""",
                                         inspect.stack()[0].function))

    def test_035(self):
        input = Program([VarDecl("a", FloatType(), BinaryOp("*", IntLiteral(1), FloatLiteral(2.0))),
                         VarDecl("b", IntType(), BinaryOp(
                             "/", IntLiteral(1), IntLiteral(2))),
                         VarDecl("c", FloatType(), BinaryOp(
                             "/", IntLiteral(1), IntLiteral(2))),
                         FuncDecl("foo", [], IntType(), Block([Return(Id("b")), Return(Id("c"))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: Return(Id("c"))""",
                                         inspect.stack()[0].function))

    def test_036(self):
        input = Program([VarDecl("a", IntType(), BinaryOp("%", IntLiteral(1), IntLiteral(2))),
                         VarDecl("b", IntType(), BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: BinaryOp("%", IntLiteral(1), FloatLiteral(2.0))""",
                                         inspect.stack()[0].function))

    def test_037(self):
        input = Program([VarDecl("a", BoolType(), BinaryOp("||", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True))),
                         VarDecl("b", BoolType(), BinaryOp("&&", BooleanLiteral(True), IntLiteral(1)))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: BinaryOp("&&", BooleanLiteral(true), IntLiteral(1))""",
                                         inspect.stack()[0].function))

    def test_038(self):
        input = Program([
            StructType("S", [("foo", IntType())], []),
            MethodDecl("s", Id("S"), FuncDecl(
                "foo", [], VoidType(), Block([])))
        ])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_039(self):
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                VarDecl("a", IntType(), None),
                VarDecl("b", None, FieldAccess(Id("a"), "unknown")),
                Return(Id("a"))
            ]))
        ])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: FieldAccess(Id(\"a\"),\"unknown\")", inspect.stack()[0].function))

    def test_040(self):
        input = Program([VarDecl("a", BoolType(), BinaryOp(">", IntLiteral(1), IntLiteral(2))),
                         VarDecl("b", BoolType(), BinaryOp(
                             "<", FloatLiteral(1.0), FloatLiteral(2.0))),
                         VarDecl("c", BoolType(), BinaryOp(
                             "==", StringLiteral("1"), StringLiteral("2"))),
                         VarDecl("d", BoolType(), BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: BinaryOp(">", IntLiteral(1), FloatLiteral(2.0))""",
                                         inspect.stack()[0].function))

    def test_041(self):
        input = Program([StructType("TIEN", [("a", ArrayType([IntLiteral(2)], IntType()))], []),
                         InterfaceType(
                             "VO", [Prototype("foo", [], IntType())]),
                         MethodDecl("v", Id("TIEN"), FuncDecl(
                             "foo", [], IntType(), Block([Return(IntLiteral(1))]))),
                         FuncDecl("foo", [ParamDecl("a", Id("VO"))], VoidType(), Block([VarDecl("b", None,
                                                                                                StructLiteral("TIEN", [("a", ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)]))])),
                                                                                        FuncCall("foo", [Id("b")])]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: FuncCall("foo",[Id("b")])""",
                                         inspect.stack()[0].function))

    def test_042(self):
        input = Program([VarDecl("A", None, IntLiteral(1)),
                         StructType("A", [("a", IntType())], [])])
        self.assertTrue(TestChecker.test(input,
                                         """Redeclared Type: A""",
                                         inspect.stack()[0].function))

    def test_043(self):
        input = Program([StructType("S1", [("HAIDANG", IntType())], []),
                         InterfaceType(
                             "I1", [Prototype("HAIDANG", [], VoidType())]),
                         MethodDecl("s", Id("S1"), FuncDecl(
                             "HAIDANG", [], VoidType(), Block([Return(None)]))),
                         VarDecl("b", ArrayType(
                             [IntLiteral(2)], Id("S1")), None),
                         VarDecl("a", ArrayType([IntLiteral(2)], Id("I1")), Id("b"))])
        self.assertTrue(TestChecker.test(input,
                                         """Redeclared Method: HAIDANG""",
                                         inspect.stack()[0].function))

    def test_044(self):
        input = Program([VarDecl("a", ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))], IntType()), None),
                         VarDecl("b", ArrayType([IntLiteral(10)], IntType()), Id("a"))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_045(self):
        input = Program([FuncDecl("foo", [], VoidType(), Block(
            [FuncCall("putFloat", [FuncCall("getInt", [])])]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: FuncCall("putFloat",[FuncCall("getInt",[])])""",
                                         inspect.stack()[0].function))

    def test_046(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []),
                         FuncDecl("foo", [], Id("TIEN"), Block([Return(NilLiteral())]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_047(self):
        input = Program([FuncDecl("foo", [], ArrayType([IntLiteral(2)], FloatType()),
                         Block([Return(ArrayLiteral([IntLiteral(2)], FloatType(), [FloatLiteral(1.0), FloatLiteral(2.0)])),
                                Return(ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))""",
                                         inspect.stack()[0].function))

    def test_048(self):
        input = Program([FuncDecl("foo", [], IntType(),
                         Block([VarDecl("a", IntType(), None),
                                If(BinaryOp("<", Id("a"), IntLiteral(3)),
                                   Block([VarDecl("a", None, IntLiteral(1))]),
                                   If(BinaryOp(">", Id("a"), IntLiteral(2)),
                                      Block(
                                          [VarDecl("a", None, IntLiteral(2))]),
                                      None)),
                                Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_049(self):
        input = Program([FuncDecl("foo", [ParamDecl("a", ArrayType([IntLiteral(2)], FloatType()))], VoidType(),
                         Block([FuncCall("foo", [ArrayLiteral([IntLiteral(2)], FloatType(), [FloatLiteral(1.0), FloatLiteral(2.0)])]),
                                FuncCall("foo", [ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])""",
                                         inspect.stack()[0].function))

    def test_050(self):
        input = Program([FuncDecl("HAIDANG", [ParamDecl("a", ArrayType([IntLiteral(2)], IntType()))], VoidType(),
                         Block([FuncCall("HAIDANG", [ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: FuncCall("HAIDANG",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])""",
                                         inspect.stack()[0].function))

    def test_051(self):
        input = Program([ConstDecl("v", None, IntLiteral(3)),
                         ConstDecl("k", None, BinaryOp(
                             "+", Id("v"), IntLiteral(1))),
                         FuncDecl("foo", [ParamDecl("a", ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))], IntType()))],
                         VoidType(), Block([FuncCall("foo", [ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))], IntType(),
                                                                          [IntLiteral(1), IntLiteral(2), IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_052(self):
        input = Program([VarDecl("a", ArrayType([BinaryOp("%", IntLiteral(5), IntLiteral(2))], IntType()), None),
                         VarDecl("b", ArrayType([IntLiteral(1)], IntType()), Id("a"))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_053(self):
        input = Program([ConstDecl("a", None, IntLiteral(2)),
                         StructType(
                             "STRUCT", [("x", ArrayType([Id("a")], IntType()))], []),
                         MethodDecl("s", Id("STRUCT"),
                         FuncDecl("foo", [ParamDecl("x", ArrayType([Id("a")], IntType()))],
                                  ArrayType([Id("a")], IntType()), Block([Return(FieldAccess(Id("s"), "x"))]))),
                         FuncDecl("foo", [ParamDecl("x", ArrayType([Id("a")], IntType()))],
                         ArrayType([Id("a")], IntType()), Block([ConstDecl("a", None, IntLiteral(3)),
                                                                 Return(ArrayLiteral([Id("a")], IntType(), [IntLiteral(1), IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: Return(ArrayLiteral([Id("a")],IntType(),[IntLiteral(1),IntLiteral(2)]))""",
                                         inspect.stack()[0].function))

    def test_054(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([Assign(Id("a"), IntLiteral(1)), VarDecl("a", None, IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_055(self):
        input = Program([VarDecl("v", Id("TIEN"), None),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("foo", [ParamDecl("v", IntType())], IntType(), Block([Return(Id("v"))]))),
                         StructType("TIEN", [("HAIDANG", IntType())], [])])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_056(self):
        input = Program([FuncDecl("HAIDANG", [ParamDecl("b", IntType())], VoidType(),
                         Block([ForStep(VarDecl("a", None, IntLiteral(1)),
                                        BinaryOp("<", Id("c"), IntLiteral(1)),
                                        Assign(Id("a"), BinaryOp(
                                            "+", Id("a"), Id("c"))),
                                        Block([ConstDecl("c", None, IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Identifier: c", inspect.stack()[0].function))

    def test_057(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([VarDecl("v", IntType(), None),
                                ConstDecl("x", None, Id("v")),
                                VarDecl("k", FloatType(), Id("x")),
                                VarDecl("y", BoolType(), Id("x"))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: VarDecl("y",BoolType(),Id("x"))""",
                                         inspect.stack()[0].function))

    def test_058(self):
        input = Program([StructType("TIEN", [("v", IntType())], []),
                         VarDecl("v", Id("TIEN"), None),
                         FuncDecl("foo", [], VoidType(), Block([ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),
                                                                         Block([VarDecl("a", IntType(), FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))""",
                                         inspect.stack()[0].function))

    def test_059(self):
        input = Program([FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))])),
                         FuncDecl("HAIDANG", [], IntType(), Block([Return(FuncCall("HAIDANG", [])),
                                                                   FuncCall("foo", [])]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: FuncCall("foo",[])""",
                                         inspect.stack()[0].function))

    def test_060(self):
        input = Program([MethodDecl("v", Id("TIEN"),
                         FuncDecl("VO", [], VoidType(), Block([Return(None)]))),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("Tien", [], VoidType(), Block([Return(None)]))),
                         StructType("TIEN", [("HAIDANG", IntType()), ("Tien", IntType())], [])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Method: Tien", inspect.stack()[0].function))

    def test_061(self):
        input = Program([StructType("TIEN", [("HAIDANG", IntType())], []),
                         MethodDecl("v", Id("TIEN"),
                         FuncDecl("HAIDANG", [], VoidType(), Block([Return(None)])))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Method: HAIDANG", inspect.stack()[0].function))

    def test_062(self):
        input = Program([MethodDecl("v", Id("TIEN"),
                         FuncDecl("HAIDANG", [], VoidType(), Block([Return(None)]))),
                         StructType("TIEN", [("HAIDANG", IntType())], [])])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Method: HAIDANG", inspect.stack()[0].function))

    def test_063(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([Assign(Id("foo"), IntLiteral(1)), FuncCall("foo", [])]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_064(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([VarDecl("a", None, Id("foo"))]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Identifier: foo", inspect.stack()[0].function))

    def test_065(self):
        input = Program([FuncDecl("HAIDANG", [], VoidType(),
                         Block([VarDecl("array", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
                                VarDecl("index", IntType(), None),
                                VarDecl("value", FloatType(), None),
                                ForEach(Id("index"), Id("value"), Id("array"), Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))""",
                                         inspect.stack()[0].function))

    def test_066(self):
        input = Program([FuncDecl("HAIDANG", [], VoidType(),
                         Block([VarDecl("array", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
                                VarDecl("index", IntType(), None),
                                VarDecl("value", ArrayType(
                                    [IntLiteral(3)], IntType()), None),
                                ForEach(Id("index"), Id("value"), Id("array"),
                                Block([VarDecl("value", ArrayType([IntLiteral(2)], IntType()), None),
                                       ForEach(Id("index"), Id("value"), Id("array"), Block([Return(None)]))]))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))""",
                                         inspect.stack()[0].function))

    def test_067(self):
        input = Program([StructType("TIEN", [("a", IntType())], []),
                         InterfaceType(
                             "VO", [Prototype("fooA", [], VoidType())]),
                         MethodDecl("v", Id("TIEN"), FuncDecl(
                             "fooA", [], VoidType(), Block([Return(None)]))),
                         VarDecl("index", IntType(), None),
                         FuncDecl("HAIDANG", [], VoidType(),
                         Block([VarDecl("array", ArrayType([UnaryOp("-", UnaryOp("-", IntLiteral(3))),
                                                            BinaryOp("%", IntLiteral(7), IntLiteral(4))], Id("VO")), None),
                                VarDecl("value", ArrayType(
                                    [BinaryOp("-", IntLiteral(4), IntLiteral(1))], Id("VO")), None),
                                ForEach(Id("index"), Id("value"), Id("array"), Block([Return(None)]))])),
                         FuncDecl("HAIDANG1", [], VoidType(),
                         Block([VarDecl("array", ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(3)),
                                                            BinaryOp("*", IntLiteral(3), IntLiteral(1))], Id("TIEN")), None),
                                VarDecl("value", ArrayType(
                                    [BinaryOp("/", IntLiteral(9), IntLiteral(3))], Id("TIEN")), None),
                                ForEach(Id("index"), Id("value"), Id("array"), Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_068(self):
        input = Program([FuncDecl("foo", [ParamDecl("a", ArrayType([IntLiteral(2)], IntType()))],
                         VoidType(), Block([VarDecl("x", None, ArrayCell(Id("a"), [FloatLiteral(0.5)]))]))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: ArrayCell(Id(\"a\"),[FloatLiteral(0.5)])", inspect.stack()[0].function))

    def test_069(self):
        input = Program([VarDecl("x", None, BinaryOp(
            "+", BooleanLiteral(True), BooleanLiteral(False)))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_070(self):
        input = Program([FuncDecl("foo", [], IntType(),
                         Block([ForStep(VarDecl("i", None, IntLiteral(0)),
                                        BinaryOp("<", Id("i"), IntLiteral(1)),
                                        Assign(Id("i"), BinaryOp(
                                            "+", Id("i"), IntLiteral(1))),
                                        Block([Return(FloatLiteral(3.14))])),
                                Return(IntLiteral(0))]))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: Return(FloatLiteral(3.14))", inspect.stack()[0].function))

    def test_071(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([ForBasic(BooleanLiteral(True), Block([VarDecl("i", None, IntLiteral(10))]))]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_072(self):
        input = Program([VarDecl("a", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
                         FuncDecl("foo", [], VoidType(),
                         Block([ForStep(VarDecl("i", None, IntLiteral(0)),
                                        BinaryOp("<", Id("i"),
                                                 FloatLiteral(2.0)),
                                        Assign(Id("i"), BinaryOp(
                                            "+", Id("i"), IntLiteral(1))),
                                        Block([Assign(ArrayCell(Id("a"), [Id("i")]), Id("i"))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: BinaryOp(\"<\", Id(\"i\"), FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_073(self):
        input = Program([VarDecl("x", FloatType(), FloatLiteral(1.2)),
                         VarDecl("y", None, FieldAccess(Id("x"), "x"))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: FieldAccess(Id(\"x\"),\"x\")", inspect.stack()[0].function))

    def test_074(self):
        input = Program([VarDecl("a", None, NilLiteral())])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_075(self):
        input = Program([FuncDecl("foo", [], VoidType(), Block([Continue()]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_076(self):
        input = Program([FuncDecl("foo", [], IntType(), Block([Break()]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_077(self):
        input = Program([
            FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("i", None, Id("a")),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        ForStep(
                            VarDecl("i", None, IntLiteral(0)),
                            BinaryOp("<", Id("i"), IntLiteral(5)),
                            Assign(Id("i"), BinaryOp(
                                "+", Id("i"), IntLiteral(1))),
                            Block([
                                VarDecl("a", FloatType(), Id("i"))
                            ])
                        )
                    ])
                )
            ]))
        ])
        self.assertTrue(TestChecker.test(
            input, "HOANGLAM", inspect.stack()[0].function))

    def test_078(self):
        input = Program([FuncDecl("foo", [], IntType(),
                         Block([VarDecl("a", IntType(), None),
                                If(BooleanLiteral(True), Block([Return(IntLiteral(1))]), None)]))])
        self.assertTrue(TestChecker.test(
            input, "HAIDANG", inspect.stack()[0].function))

    def test_079(self):
        input = Program([FuncDecl("foo", [], IntType(),
                         Block([VarDecl("x", IntType(), IntLiteral(1)),
                                Return(BinaryOp("+", FloatLiteral(1.0), Id("x")))]))])
        self.assertTrue(TestChecker.test(input,
                                         """Type Mismatch: Return(BinaryOp("+", FloatLiteral(1.0), Id("x")))""",
                                         inspect.stack()[0].function))

    def test_080(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([VarDecl("arr", ArrayType([IntLiteral(2), IntLiteral(2)], IntType()), None),
                                ForEach(Id("idx"), Id("val"), Id("arr"),
                                Block([ForEach(Id("i"), Id("v"), Id("val"), Block([Return(None)]))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Identifier: idx", inspect.stack()[0].function))

    def test_081(self):
        input = Program([VarDecl("x", None, IntLiteral(10)),
                         FuncDecl("x", [], VoidType(), Block([]))])
        self.assertTrue(TestChecker.test(
            input, "Redeclared Function: x", inspect.stack()[0].function))

    def test_082(self):
        input = Program([VarDecl("a", StringType(), StringLiteral("1")),
                         VarDecl("b", IntType(), BinaryOp("+", Id("a"), IntLiteral(2)))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: BinaryOp(\"+\", Id(\"a\"), IntLiteral(2))", inspect.stack()[0].function))

    def test_083(self):
        input = Program([FuncDecl("foo", [], ArrayType([IntLiteral(2)], StringType()),
                         Block([VarDecl("arr", ArrayType([IntLiteral(2)], StringType()), None),
                                Return(ArrayCell(Id("arr"), [IntLiteral(0)]))]))])
        self.assertTrue(TestChecker.test(
            input, "Type Mismatch: Return(ArrayCell(Id(\"arr\"),[IntLiteral(0)]))", inspect.stack()[0].function))

    def test_084(self):
        input = Program([FuncDecl("foo", [], VoidType(),
                         Block([VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), None),
                                ForEach(Id("i"), Id("val"), Id("arr"),
                                Block([Assign(Id("val"), BinaryOp("+", Id("i"), FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestChecker.test(
            input, "Undeclared Identifier: i", inspect.stack()[0].function))
