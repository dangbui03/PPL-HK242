from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, v, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        # Danh sách hàm có sẵn + hàm user (sẽ thêm sau)
        self.list_function: List[FuncDecl] = [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putFloat", [ParamDecl("VOTIEN", FloatType())], VoidType(), Block([])),

        ]
        # Dùng để biết hàm hiện tại, phục vụ kiểm tra return
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, LHS_type: Type, RHS_type: Type, 
                list_type_permission: List[Tuple[type, type]] = [], 
                strict: bool = False, c=None) -> bool:
        # Nếu LHS_type hoặc RHS_type là Id, tra cứu kiểu thực tế từ self.list_type
        if isinstance(LHS_type, Id):
            foundL = self.lookup(LHS_type.name, self.list_type, lambda x: x.name)
            if foundL:
                LHS_type = foundL
        if isinstance(RHS_type, Id):
            foundR = self.lookup(RHS_type.name, self.list_type, lambda x: x.name)
            if foundR:
                RHS_type = foundR

        # Nếu RHS_type là StructType vô danh (ví dụ từ nil) thì cho phép nếu LHS là StructType hoặc InterfaceType
        if isinstance(RHS_type, StructType) and RHS_type.name == "":
            return isinstance(LHS_type, (StructType, InterfaceType))

        # Xử lý ArrayType: kiểm tra số chiều và giá trị của từng chiều
        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            if strict:
                for ldim, rdim in zip(LHS_type.dimens, RHS_type.dimens):
                    if self.evaluate_ast(ldim, c) != self.evaluate_ast(rdim, c):
                        return False
                return self.checkType(LHS_type.eleType, RHS_type.eleType, [], strict=True, c=c)
            else:
                # Kiểm tra số chiều phải bằng nhau
                if len(LHS_type.dimens) != len(RHS_type.dimens):
                    return False
                return self.checkType(LHS_type.eleType, RHS_type.eleType, [(FloatType, IntType)], strict=False, c=c)

        # Nếu không ở chế độ strict và quy tắc chuyển đổi số áp dụng
        if not strict and (type(LHS_type), type(RHS_type)) in list_type_permission:
            if isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, StructType):
                for proto in LHS_type.methods:
                    found_meth = self.lookup(proto.name, RHS_type.methods, lambda x: x.fun.name)
                    if not found_meth:
                        return False
                    if not self.checkType(found_meth.fun.retType, proto.retType, strict=strict, c=c):
                        return False
                    if len(found_meth.fun.params) != len(proto.params):
                        return False
                    for p_f, p_i in zip(found_meth.fun.params, proto.params):
                        if not self.checkType(p_f.parType, p_i, list_type_permission, strict=strict, c=c):
                            return False
                return True
            return True

        # Nếu cả LHS và RHS đều là StructType hoặc InterfaceType, chỉ so sánh theo tên
        if isinstance(LHS_type, (StructType, InterfaceType)) and isinstance(RHS_type, (StructType, InterfaceType)):
            return (LHS_type.name == RHS_type.name)

        # Trường hợp còn lại, so sánh theo kiểu lớp
        return isinstance(LHS_type, type(RHS_type))


    def visitProgram(self, ast: Program, c: None):
        # 1) Tạo một set/tập chứa tên built-in
        used_names = {"getInt","putInt","putIntLn","getString","putString","putStringLn","putLn"}

        def visitMethodDecl(method_decl: MethodDecl, struct_type: StructType):
            # Tạm giữ code cũ, ...
            if any(m.fun.name == method_decl.fun.name for m in struct_type.methods):
                raise Redeclared(Method(), method_decl.fun.name)
            # ...
            struct_type.methods.append(method_decl)
            return method_decl

        # 2) Duyệt qua tất cả decl **trước** khi visit(...) chúng
        #    để phát hiện sớm Redeclared name
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                # Nếu decl.varName trùng used_names => Redeclared
                if decl.varName in used_names:
                    raise Redeclared(Variable(), decl.varName)
                used_names.add(decl.varName)

            elif isinstance(decl, ConstDecl):
                if decl.conName in used_names:
                    raise Redeclared(Constant(), decl.conName)
                used_names.add(decl.conName)

            elif isinstance(decl, FuncDecl):
                if decl.name in used_names:
                    raise Redeclared(Function(), decl.name)
                used_names.add(decl.name)

            elif isinstance(decl, StructType):
                # Quan trọng: Kiểm tra "A" có trong used_names
                if decl.name in used_names:
                    # => "Redeclared Type: A"
                    raise Redeclared(StaticErrorType(), decl.name)
                used_names.add(decl.name)

            elif isinstance(decl, InterfaceType):
                # Tương tự struct
                if decl.name in used_names:
                    raise Redeclared(StaticErrorType(), decl.name)
                used_names.add(decl.name)

        # 3) Thu thập self.list_type
        self.list_type = reduce(
            lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc,
            ast.decl,
            []
        )

        # 4) Thu thập hàm (FuncDecl)
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))
        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)), 
            list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        # 6) Cuối cùng, duyệt Var/Const/FuncDecl
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance((result := self.visit(ele, acc)), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda item: isinstance(item, Decl), ast.decl),
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("putLn", FuntionType()),
            ]]
        )


    def visitStructType(self, ast: StructType, c: List[Union[StructType, InterfaceType]]) -> StructType:
        # Kiểm tra nếu trùng với hàm built-in hoặc hàm user
        if any(f.name == ast.name for f in self.list_function):
            # Tức struct "putLn" đụng với hàm "putLn"
            raise Redeclared(StaticErrorType(), ast.name)
        # Kiểm tra nếu đã có struct/interface cùng tên
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is not None:
            raise Redeclared(StaticErrorType(), ast.name)
        
        # Phần kiểm tra field cũ
        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            if any(e[0] == element[0] for e in c):
                raise Redeclared(Field(), element[0])
            return element

        ast.elements = reduce(lambda acc, ele: [visitElements(ele, acc)] + acc, ast.elements, [])
        return ast


    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        if self.lookup(ast.name, c, lambda x: x.name):
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]) -> InterfaceType:
        if any(f.name == ast.name for f in self.list_function):
            raise Redeclared(StaticErrorType(), ast.name)
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is not None:
            raise Redeclared(StaticErrorType(), ast.name)  
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        if self.lookup(ast.name, c[0], lambda x: x.name) is not None:
            raise Redeclared(Function(), ast.name)
        
        # Ghi nhớ hàm cũ (nếu đang lồng)
        old_func = self.function_current
        self.function_current = ast  # Lưu hàm hiện tại

        # Tạo scope mới cho tham số hàm
        new_c = [[]] + c
        
        # Thêm từng tham số
        for param in ast.params:
            sym = self.visitParamDecl(param, new_c)
            new_c[0].append(sym)

        # Duyệt thân hàm
        self.visit(ast.body, new_c)

        # Khôi phục function_current
        self.function_current = old_func

        # Trả về Symbol để gom vào scope
        return Symbol(ast.name, FuntionType(), None)

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        new_c = [[]] + c
        recTypeObj = ast.recType
        if isinstance(recTypeObj, Id):
            actualType = self.lookup(recTypeObj.name, self.list_type, lambda x: x.name)
            if not actualType:
                raise Undeclared(Identifier(), recTypeObj.name)
            recTypeObj = actualType

        # Lưu receiver như 1 param
        new_c[0].append(Symbol(ast.receiver, recTypeObj, None))

        # Ghi nhớ hàm cũ
        old_func = self.function_current
        self.function_current = ast.fun

        # Thêm tham số của method
        for param in ast.fun.params:
            new_c[0].append(self.visitParamDecl(param, new_c))

        # Duyệt thân
        self.visit(ast.fun.body, new_c)

        # Phục hồi hàm cũ
        self.function_current = old_func
        return ast
        
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        
        LHS_type = ast.varType if ast.varType else None
        RHS_type = self.visit(ast.varInit, c) if ast.varInit else None

        if RHS_type is None:
            return Symbol(ast.varName, LHS_type, None)
        elif LHS_type is None:
            return Symbol(ast.varName, RHS_type, None)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, LHS_type, None)
        raise TypeMismatch(ast)
        
    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)
        iniType = self.visit(ast.iniExpr, c)
        iniValue = self.evaluate_ast(ast.iniExpr, c)  # Tính giá trị của biểu thức khởi tạo
        sym = Symbol(ast.conName, iniType, iniValue)
        c[0].append(sym)  # Thêm vào scope hiện hành
        return sym
    
    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c 
        for ele in ast.member:
            # Nếu là FuncCall/MethCall, check stmt vs expr
            result = self.visit(ele, (acc, True)) if isinstance(ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            # Nếu trả về Symbol => khai báo (Var/ConstDecl) => thêm vào scope
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        # điều kiện phải Bool
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        # Ta cho init và thân for chung 1 scope => bắt redeclared
        new_c = [[]] + c
        symbol = self.visit(ast.init, new_c)
        if isinstance(symbol, Symbol):
            new_c[0].append(symbol)
        if not isinstance(self.visit(ast.cond, new_c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), new_c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        new_dim = type_array.dimens[1:]
        if len(new_dim) == 0:
            val_type = type_array.eleType
        else:
            val_type = ArrayType(new_dim, type_array.eleType)

        self.visit(Block([
            VarDecl(ast.idx.name, IntType(), None),
            VarDecl(ast.value.name, val_type, None)
        ] + ast.loop.member), c)
        
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        # Tìm trong các scope
        res = next(filter(None, [self.lookup(ast.name, scope, lambda x: x.name) for scope in c]), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)
        
    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if not res:
            raise Undeclared(Function(), ast.funName)

        if len(res.params) != len(ast.args):
            raise TypeMismatch(ast)

        for param, arg in zip(res.params, ast.args):
            argType = self.visit(arg, c)
            # Nếu tham số là mảng thì kiểm tra chặt chẽ (không cho phép chuyển đổi kiểu phần tử)
            if isinstance(param.parType, ArrayType):
                if not self.checkType(param.parType, argType, [], strict=True, c=c):
                    raise TypeMismatch(ast)
            else:
                if res.name == "putFloat":
                    # putFloat không cho phép chuyển đổi int -> float
                    if not isinstance(argType, FloatType):
                        raise TypeMismatch(ast)
                else:
                    # Cho phép chuyển đổi số đối với các kiểu khác (int -> float)
                    if not self.checkType(param.parType, argType, [(FloatType, IntType)], c=c):
                        raise TypeMismatch(ast)

        if is_stmt and not isinstance(res.retType, VoidType):
            raise TypeMismatch(ast)
        if not is_stmt and isinstance(res.retType, VoidType):
            raise TypeMismatch(ast)

        return res.retType



    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)
        # Nếu là Id => tra cứu
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)
        
        res = self.lookup(ast.field, receiver_type.elements, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        return res[1]

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)

        # Tìm method
        if isinstance(receiver_type, StructType):
            res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name)
            if not res:
                raise Undeclared(Method(), ast.metName)
            if len(res.fun.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.fun.params, ast.args):
                argType = self.visit(arg, c)
                if not self.checkType(param.parType, argType, [(FloatType, IntType), (InterfaceType, StructType)]):
                    raise TypeMismatch(ast)
            if is_stmt and not isinstance(res.fun.retType, VoidType):
                raise TypeMismatch(ast)
            if not is_stmt and isinstance(res.fun.retType, VoidType):
                raise TypeMismatch(ast)
            return res.fun.retType
        else:
            # InterfaceType
            res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
            if not res:
                raise Undeclared(Method(), ast.metName)
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.params, ast.args):
                argType = self.visit(arg, c)
                if not self.checkType(param, argType, [(FloatType, IntType), (InterfaceType, StructType)]):
                    raise TypeMismatch(ast)
            if is_stmt and not isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            if not is_stmt and isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            return res.retType

    # Kiểu
    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def evaluate_ast(self, expr, c):
        if c is None:
            c = []
        if isinstance(expr, IntLiteral):
            return expr.value
        if isinstance(expr, BinaryOp):
            l = self.evaluate_ast(expr.left, c)
            r = self.evaluate_ast(expr.right, c)
            if l is None or r is None:
                return None
            if expr.op == '+':
                return l + r
            elif expr.op == '-':
                return l - r
            elif expr.op == '*':
                return l * r
            elif expr.op == '/':
                return l // r  # hoặc chia theo yêu cầu
        if isinstance(expr, Id):
            # Duyệt qua các scope và trả về giá trị nếu đã được lưu
            for scope in c:
                for sym in scope:
                    if sym.name == expr.name and sym.value is not None:
                        return sym.value
        return None

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        newDims = []
        for dimExpr in ast.dimens:
            val = self.evaluate_ast(dimExpr, c)
            if val is None or val < 0:
                raise TypeMismatch(ast)
            newDims.append(val)

        elemT = self.visit(ast.eleType, c)
        return ArrayType(newDims, elemT)


    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        """
        c là danh sách các scope [scope_hiện_tại, scope_trên_nữa, ...]
        """
        # Nếu bên trái phép gán là 1 Id (ví dụ 'a'), ta thử tìm biến 'a' trong từng scope.
        # Nếu không thấy ở bất kỳ scope nào => tự động khai báo mới trong scope[0].
        if isinstance(ast.lhs, Id):
            found_symbol = None
            for scope in c:  
                sym = self.lookup(ast.lhs.name, scope, lambda x: x.name)
                if sym:
                    found_symbol = sym
                    break
            
            # Nếu chưa thấy biến 'a' trong toàn bộ các scope => auto-declare
            if not found_symbol:
                # Lấy kiểu của RHS để gán cho 'a'
                rhs_type = self.visit(ast.rhs, c)
                # Thêm mới vào scope[0] (scope cục bộ nhất)
                c[0].append(Symbol(ast.lhs.name, rhs_type, None))
        
        # Sau khi đảm bảo biến (hoặc field) bên trái đã có, mình mới kiểm tra kiểu
        LHS_type = self.visit(ast.lhs, c)  # Lấy kiểu của bên trái
        RHS_type = self.visit(ast.rhs, c)  # Lấy kiểu của bên phải

        # Kiểm tra xem 2 kiểu có hợp lệ để gán không
        # list_type_permission cho phép float := int, interface := struct, ...
        if not self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)

        
    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: 
        return None

    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: 
        return None

    def visitReturn(self, ast, c: List[List[Symbol]]) -> None:
        if ast.expr:  # Có biểu thức trả về
            return_type = self.visit(ast.expr, c)
            # Expected type là kiểu khai báo của hàm (self.function_current.retType)
            # Dùng strict=True để yêu cầu kiểu trả về phải khớp hoàn toàn
            if not self.checkType(self.function_current.retType, return_type, [], strict=True):
                raise TypeMismatch(ast)
        elif not isinstance(self.function_current.retType, VoidType):
            raise TypeMismatch(ast)
        return None


    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)

        # Ví dụ xử lý các toán tử so sánh => trả về Bool
        if ast.op in ['<', '>', '<=', '>=', '&&', '||', '==', '!=']:
            if type(LHS_type) != type(RHS_type):
                raise TypeMismatch(ast)
            if isinstance(LHS_type, (IntType, FloatType)) and isinstance(RHS_type, (IntType, FloatType)):
                return BoolType()
            if isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType):
                return BoolType()
            if isinstance(LHS_type, StringType) and isinstance(RHS_type, StringType):
                return BoolType()
            
            else:
                raise TypeMismatch(ast)

        if ast.op in ['+', '*', '/']:
            # Cho phép int+int, float+float, int+float, float+int, string+string
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS_type, StringType) and isinstance(RHS_type, StringType):
                    return StringType()
                if isinstance(LHS_type, FloatType) or isinstance(RHS_type, FloatType):
                    return FloatType()
                return IntType()
            # Nếu cả 2 là string => string
            if isinstance(LHS_type, StringType) and isinstance(RHS_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            raise TypeMismatch(ast)
        if ast.op in ['%']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS_type, IntType) and isinstance(RHS_type, FloatType):
                    raise TypeMismatch(ast)
                return IntType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        unary_type = self.visit(ast.body, c)
        if ast.op == '!':
            if not isinstance(unary_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()
        elif ast.op == '-':
            if isinstance(unary_type, IntType):
                return IntType()
            if isinstance(unary_type, FloatType):
                return FloatType()
            raise TypeMismatch(ast)
        else:
            raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
        # Kiểm tra tất cả chỉ số phải Int
        if not all(map(lambda idxExpr: self.checkType(self.visit(idxExpr, c), IntType(), []), ast.idx)):
            raise TypeMismatch(ast)

        # Nếu truy cập đủ số chiều => kiểu phần tử
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            # Còn dư chiều => sub-array
            new_dim = array_type.dimens[len(ast.idx):]
            return ArrayType(new_dim, array_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return IntType()

    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return FloatType()

    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return BoolType()

    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return StringType()

    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        def nested2recursive(dat):
            if isinstance(dat, list):
                for value in dat:
                    nested2recursive(value)
            elif isinstance(dat, Expr):
                self.visit(dat, c)
        
        nested2recursive(ast.value)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type: 
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return self.lookup(ast.name, self.list_type, lambda x: x.name)
    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type: 
        # nil coi như struct vô danh
        return StructType("", [], [])