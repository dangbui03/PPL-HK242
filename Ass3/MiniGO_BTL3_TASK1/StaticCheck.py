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
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] = [
                FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl(
                "VOTIEN", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl(
                "VOTIEN", IntType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl(
                "VOTIEN", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl(
                "VOTIEN", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putFloat", [ParamDecl(
                "VOTIEN", FloatType())], VoidType(), Block([])),
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS_type) == StructType and RHS_type.name == "":
            return isinstance(LSH_type, (StructType, InterfaceType))

        LSH_type = self.lookup(LSH_type.name, self.list_type, lambda x: x.name) if isinstance(
            LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(
            RHS_type, Id) else RHS_type
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                # Check if struct implements interface
                for proto in LSH_type.methods:
                    method = self.lookup(
                        proto.name, RHS_type.methods, lambda x: x.fun.name)
                    if not method:
                        return False
                    # Check method signature
                    if len(method.fun.params) != len(proto.params):
                        return False
                    if type(method.fun.retType) != type(proto.retType):
                        return False
                    for i in range(len(method.fun.params)):
                        if type(method.fun.params[i].parType) != type(proto.params[i]):
                            return False
                return True
            return True

        if isinstance(LSH_type, Id) and isinstance(RHS_type, Id):
            return LSH_type.name == RHS_type.name

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            if len(LSH_type.dimens) != len(RHS_type.dimens):
                return False
            for i in range(len(LSH_type.dimens)):
                if LSH_type.dimens[i].value != RHS_type.dimens[i].value:
                    return False
            return self.checkType(LSH_type.eleType, RHS_type.eleType, list_type_permission)
        return type(LSH_type) == type(RHS_type)

    def compute_expression(self, node, context):
        # Khởi tạo context mặc định là một từ điển rỗng nếu không được cung cấp
        if context is None:
            context = {}

        # Xử lý giá trị nguyên
        if isinstance(node, IntLiteral):
            return node.value

        # Xử lý phép toán nhị phân
        if isinstance(node, BinaryOp):
            left_value = self.compute_expression(node.left, context)
            right_value = self.compute_expression(node.right, context)
            
            # Kiểm tra giá trị hợp lệ
            if left_value is None or right_value is None:
                return None
            
            # Thực hiện phép toán dựa trên toán tử
            operator = node.op
            if operator == '+':
                return left_value + right_value
            elif operator == '-':
                return left_value - right_value
            elif operator == '*':
                return left_value * right_value
            elif operator == '/':
                return left_value // right_value  # Sử dụng chia lấy nguyên

        # Xử lý biến (identifier)
        if isinstance(node, Id):
            variable_name = node.name
            # Tìm giá trị của biến trong context
            if variable_name in context and context[variable_name] is not None:
                return context[variable_name]

        # Trả về None nếu không thể tính toán
        return None
    
    def visitProgram(self, ast: Program, c: None):
        # global_env = c.copy()
        
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            # TODO: Implement
            if self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name):
                raise Redeclared(Method(), ast.fun.name)

            c.methods.append(ast)
            return ast
        
        # used_names = {"getInt","putInt","putIntLn","getString","putString","putStringLn","putLn"}
        # for decl in ast.decl:
        #     if isinstance(decl, VarDecl):
        #         # Nếu decl.varName trùng used_names => Redeclared
        #         if decl.varName in used_names:
        #             raise Redeclared(Variable(), decl.varName)
        #         used_names.add(decl.varName)

        #     elif isinstance(decl, ConstDecl):
        #         if decl.conName in used_names:
        #             raise Redeclared(Constant(), decl.conName)
        #         used_names.add(decl.conName)

        #     elif isinstance(decl, FuncDecl):
        #         if decl.name in used_names:
        #             raise Redeclared(Function(), decl.name)
        #         used_names.add(decl.name)

        #     elif isinstance(decl, StructType):
        #         # Quan trọng: Kiểm tra "A" có trong used_names
        #         if decl.name in used_names:
        #             # => "Redeclared Type: A"
        #             raise Redeclared(StaticErrorType(), decl.name)
        #         used_names.add(decl.name)

        #     elif isinstance(decl, InterfaceType):
        #         # Tương tự struct
        #         if decl.name in used_names:
        #             raise Redeclared(StaticErrorType(), decl.name)
        #         used_names.add(decl.name)
        
        used_names = {"getInt", "putInt", "putIntLn", "getString", "putString", "putStringLn", "putLn"}

        for decl in ast.decl:
            match decl:
                case VarDecl(varName=name):
                    if name in used_names:
                        raise Redeclared(Variable(), name)
                    used_names.add(name)
                case ConstDecl(conName=name):
                    if name in used_names:
                        raise Redeclared(Constant(), name)
                    used_names.add(name)
                case FuncDecl(name=name):
                    if name in used_names:
                        raise Redeclared(Function(), name)
                    used_names.add(name)
                case StructType(name=name) | InterfaceType(name=name):
                    if name in used_names:
                        raise Redeclared(StaticErrorType(), name)
                    used_names.add(name)
                
        self.list_type = reduce(lambda acc, ele: [self.visit(
            ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_function = self.list_function + \
            list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(
                item.recType.name, self.list_type, lambda x: x.name)),
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result :=
                 self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:],
            filter(lambda item: isinstance(item, Decl), ast.decl),
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                # TODO: Implement
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("putLn", FuntionType()),
            ]]
        )

    def visitStructType(self, ast: StructType, c: List[Union[StructType, InterfaceType]]) -> StructType:
        # Check if there's already a type with the same name
        # res = self.lookup(ast.name, c, lambda x: x.name)
        # if res is not None:
        #     raise Redeclared(StaticErrorType(), ast.name)
        if ast.name in c:
            raise Redeclared(StaticErrorType(), ast.name)
        
        for function in self.list_function:
            if function.name == ast.name:
                raise Redeclared(StaticErrorType(), ast.name)

        # res =  # TODO: Implement

        def visitElements(element: Tuple[str, Type], c: List[Tuple[str, Type]]) -> Tuple[str, Type]:
            # TODO: Implement
            res = self.lookup(element[0], c, lambda x: x[0])
            if not res is None:
                raise Redeclared(Field(), element[0])

            return element

        ast.elements = reduce(
            lambda acc, ele: [visitElements(ele, acc)] + acc, ast.elements, [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # TODO: Implement
        # res = self.lookup(ast.name, c, lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Prototype(), ast.name)
        if any(obj.name == ast.name for obj in c):
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        ast.methods = reduce(
            lambda acc, ele: [self.visit(ele, acc)] + acc, ast.methods, [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        # TODO: Implement
                
        # res = self.lookup(ast.name, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Function(), ast.name)
        if any(obj.name == ast.name for obj in c[0]):
            raise Redeclared(Prototype(), ast.name)
        oldfunc = self.function_current
        
        param_types = [self.visit(param.parType, c) for param in ast.params]
        ret_type = self.visit(ast.retType, c) if ast.retType else VoidType()
        local_env = [[]] + c

        for param in ast.params:
            param_sym = self.visit(param, local_env[0])
            local_env[0].append(param_sym)
        
        self.function_current = ast
        self.visit(ast.body, local_env)
        self.function_current = oldfunc
            
        return Symbol(ast.name, FuntionType(), None)
        # self.visit(ast.body, [list(reduce(lambda acc, ele: [
        #            self.visit(ele, acc)] + acc, ast.params, []))] + c)
        # return Symbol(ast.name, FuntionType(), ast.body)
        # TODO: Implement

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # TODO: Implement
        # res = self.lookup(ast.parName, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Parameter(), ast.parName)
        if any(obj.name == ast.name for obj in c[0]):
            raise Redeclared(Parameter(), ast.name)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        # TODO: Implement
        # Get the receiver type (struct type)
        receiver_type = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if not receiver_type or not isinstance(receiver_type, StructType):
            raise Undeclared(Type(), ast.recType.name)
            
        # Check if method name already exists in the struct
        if self.lookup(ast.fun.name, receiver_type.methods, lambda x: x.fun.name):
            raise Redeclared(Method(), ast.fun.name)
            
        # Create local environment for method parameters
        local_env = [[Symbol(ast.receiver, receiver_type, None)]] + c
        
        # Process parameters and add them to local environment
        for param in ast.fun.params:
            param_sym = self.visit(param, local_env[0])
            local_env[0].append(param_sym)
        
        # Visit method body with the local environment
        self.function_current = ast.fun
        self.visit(ast.fun.body, local_env)
        self.function_current = None
        
        # Return symbol for the method
        return Symbol(ast.fun.name, FuntionType(), ast.fun.body)

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # res = self.lookup(ast.varName, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Variable(), ast.varName)
        
        if ast.varName in c[0]:
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
        # TODO: Implement
        # res = self.lookup(ast.conName, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Constant(), ast.conName)
        
        if ast.conName in c[0]:
            raise Redeclared(Constant(), ast.conName)
        
        LHS_type = ast.conType if ast.conType else None
        RHS_type = self.visit(ast.iniExpr, c) if ast.iniExpr else None
        
        initValue = self.compute_expression(ast.iniExpr, c)
        c[0].append(Symbol(ast.conName, LHS_type, initValue))
        return Symbol(ast.conName, LHS_type, initValue)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c

        for ele in ast.member:
            result = self.visit(ele, (acc, True)) if isinstance(
                ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        visit = self.visit(ast.cond, c)
        if not isinstance(visit, BoolType):
        # TODO: Implement:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        symbol = self.visit(ast.init, [[]] + c)
        if isinstance(symbol, Symbol):
            # cập nhật c
            c[0] = [symbol] + c[0]

        if not isinstance(symbol.mtype, (IntType, FloatType)):
            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)

        self.visit(Block([VarDecl(ast.key.name, type_array.eleType, None),
                          VarDecl(ast.value.name,
                                  type_array.eleType,
                                  None)] + ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(lambda env: ast.name in env, c), False)
        if res and not isinstance(res.mtype, Function):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.params, ast.args):
                arg_type = self.visit(arg, c)
                if not self.checkType(param.parType, arg_type, [(FloatType, IntType)]):
                    raise TypeMismatch(ast)

            if is_stmt and isinstance(res.retType, VoidType):
                return res.retType
            if not is_stmt and not isinstance(res.retType, VoidType):
                return res.retType
            raise TypeMismatch(ast)
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(
            receiver_type, Id) else receiver_type
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
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(
            receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name) if isinstance(
            receiver_type, StructType) else self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
        if res:
            if type(receiver_type) == StructType:
                if len(res.fun.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for param, arg in zip(res.fun.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if not self.checkType(param.parType, arg_type, [(FloatType, IntType)]):
                        raise TypeMismatch(ast)
                if is_stmt and isinstance(res.fun.retType, VoidType):
                    return res.fun.retType
                if not is_stmt and not isinstance(res.fun.retType, VoidType):
                    return res.fun.retType
                raise TypeMismatch(ast)
            if type(receiver_type) == InterfaceType:
                if len(res.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for param, arg in zip(res.params, ast.args):
                    if not self.checkType(param, self.visit(arg, c), [(FloatType, IntType)]):
                        raise TypeMismatch(ast)

                if is_stmt and isinstance(res.retType, VoidType):
                    return res.retType
                if not is_stmt and not isinstance(res.retType, VoidType):
                    return res.retType
                raise TypeMismatch(ast)
        raise Undeclared(Method(), ast.metName)

    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitFloatType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitBoolType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        # TODO: Implement, ast.dimens))
        list(map(lambda item: self.visit(item, c), ast.dimens))
        return ast

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        LHS_type = self.visit(ast.lhs, c)
        RHS_type = self.visit(ast.rhs, c)
        # TODO: Implement]):
        if not self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            # TODO: Implement
            self.visit(Block(ast.elseStmt.member), c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitReturn(self, ast, c: List[List[Symbol]]) -> None:
        expected_type = self.function_current.retType
        if ast.expr:
            expr_type = self.visit(ast.expr, c)
            if not self.checkType(expected_type, expr_type, [(FloatType, IntType), (InterfaceType, StructType)]):
                raise TypeMismatch(ast)
        elif not isinstance(expected_type, VoidType):
            raise TypeMismatch(ast)
        return None
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)

        if ast.op in ['+']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_type) == StringType:
                    return StringType()
                elif type(LHS_type) == FloatType:
                    return FloatType()
                elif type(RHS_type) == FloatType:
                    return FloatType()
                elif type(LHS_type) == IntType:
                    return IntType()
        
        if ast.op in ['-', '*', '/']:
            if (isinstance(LHS_type, IntType) or isinstance(LHS_type, FloatType)) and \
               (isinstance(RHS_type, IntType) or isinstance(RHS_type, FloatType)):
                if isinstance(LHS_type, FloatType) or isinstance(RHS_type, FloatType):
                    return FloatType()
                return IntType()
                
        if ast.op == '%':
            if isinstance(LHS_type, IntType) and isinstance(RHS_type, IntType):
                return IntType()
                
        if ast.op in ['&&', '||']:
            if isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType):
                return BoolType()
                
        if ast.op in ['==', '!=']:
            if (isinstance(LHS_type, IntType) and isinstance(RHS_type, IntType)) or \
               (isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType)):
                return BoolType()
                
        if ast.op in ['<', '>', '<=', '>=']:
            if (isinstance(LHS_type, IntType) or isinstance(LHS_type, FloatType)) and \
               (isinstance(RHS_type, IntType) or isinstance(RHS_type, FloatType)):
                return BoolType()
                
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        expr_type=self.visit(ast.body, c)
        # TODO: Implement
        if ast.op == '!':
            if isinstance(expr_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)
        
        elif ast.op in ['+', '-']:
            if isinstance(expr_type, IntType):
                return IntType()
            elif isinstance(expr_type, FloatType):
                return FloatType()
            else:
                raise TypeMismatch(ast)
        
        raise TypeMismatch(ast)

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        # array_type=  # TODO: Implement
        # if not isinstance(array_type, ArrayType):
        #     raise TypeMismatch(ast)

        # if not all(map(lambda item: self.checkType(self.visit(item, c),  # TODO: Implement), ast.idx)):
        #     raise TypeMismatch(ast)
        # if len(array_type.dimens) == len(ast.idx):
        #     return  # TODO: Implement
        # elif len(array_type.dimens) > len(ast.idx):
        #     return  # TODO: Implement
        # raise TypeMismatch(ast)
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        
        if len(ast.idx) != len(arr_type.dimens):
            raise TypeMismatch(ast)
        
        for idx in ast.idx:
            idx_type = self.visit(idx, c)
            if not isinstance(idx_type, IntType):
                raise TypeMismatch(ast)
        
        return arr_type.eleType

    def visitIntLiteral(
        self, ast, c: List[List[Symbol]]) -> Type: return IntType()
    def visitFloatLiteral(
        self, ast, c: List[List[Symbol]]) -> Type: return FloatType()
    def visitBooleanLiteral(
        self, ast, c: List[List[Symbol]]) -> Type: return BoolType()
    def visitStringLiteral(
        self, ast, c: List[List[Symbol]]) -> Type: return StringType()
    def visitArrayLiteral(self, ast: ArrayLiteral, c: List[List[Symbol]]) -> Type:
        def nested2recursive(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat, list):
                list(map(lambda value: nested2recursive(value, c), dat))
            else:
                self.visit(dat, c)
        nested2recursive(ast.value, c) # TODO: Implement)
        return ArrayType(ast.dimens, ast.eleType)
    def visitStructLiteral(self, ast: StructLiteral, c: List[List[Symbol]]) -> Type:
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return StructType(ast.name, [], [])# TODO: Implement
    def visitNilLiteral(self, ast: NilLiteral,
                        c: List[List[Symbol]]) -> Type: return StructType("", [], [])
