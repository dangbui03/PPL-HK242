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
                "Dark", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl(
                "Dark", IntType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl(
                "Dark", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl(
                "Dark", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putFloat", [ParamDecl(
                "Dark", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl(
                "Dark", FloatType())], VoidType(), Block([])),
            FuncDecl("putBool", [ParamDecl(
                "Dark", BoolType())], VoidType(), Block([])),
        ]
        self.function_current: FuncDecl = None
        self.struct_members = {}  # Dictionary to track struct members (fields and methods)

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, l_typ: Type, r_typ: Type, 
                list_type_permission: List[Tuple[type, type]] = [],
                flag = False, c=None) -> bool:
        if isinstance(l_typ, Id):
            resolved_lhs = self.lookup(l_typ.name, self.list_type, lambda x: x.name)
            l_typ = resolved_lhs if resolved_lhs else l_typ
            
        if isinstance(r_typ, Id):
            resolved_rhs = self.lookup(r_typ.name, self.list_type, lambda x: x.name)
            r_typ = resolved_rhs if resolved_rhs else r_typ
        
        if isinstance(r_typ, StructType) and r_typ.name == "":
            return any(isinstance(l_typ, t) for t in [StructType, InterfaceType])
        
        if isinstance(l_typ, ArrayType) and isinstance(r_typ, ArrayType):
            if len(l_typ.dimens) != len(r_typ.dimens):
                return False
                
            if flag:
                for left_dim, right_dim in zip(l_typ.dimens, r_typ.dimens):
                    if self.evaluate_ast(left_dim, c) != self.evaluate_ast(right_dim, c):
                        return False
                return self.checkType(l_typ.eleType, r_typ.eleType, [], True, c)
            else:
                return self.checkType(l_typ.eleType, r_typ.eleType, 
                                    [(FloatType, IntType)], False, c)
        
        if not flag and (type(l_typ), type(r_typ)) in list_type_permission:
            if isinstance(l_typ, InterfaceType) and isinstance(r_typ, StructType):
                for interface_method in l_typ.methods:
                    struct_method = self.lookup(interface_method.name, 
                                            r_typ.methods, 
                                            lambda x: x.fun.name)
                    
                    if not struct_method:
                        return False
                        
                    if not self.checkType(struct_method.fun.retType, 
                                        interface_method.retType, 
                                        flag, c):
                        return False
                        
                    if len(struct_method.fun.params) != len(interface_method.params):
                        return False
                        
                    for struct_param, interface_param in zip(struct_method.fun.params, interface_method.params):
                        if not self.checkType(struct_param.parType, 
                                            interface_param, 
                                            list_type_permission, 
                                            flag, c):
                            return False
                
                return True
            return True
        
        if all(isinstance(t, (StructType, InterfaceType)) for t in [l_typ, r_typ]):
            return l_typ.name == r_typ.name
        
        return isinstance(l_typ, type(r_typ))

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
            # if self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name):
            #     raise Redeclared(Method(), ast.fun.name)

            # c.methods.append(ast)
            # return ast
            
            struct_name = ast.recType.name
            
            # Check if method name conflicts with any field in the struct
            for field_name, _ in c.elements:
                if field_name == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)
            
            if self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name):
                raise Redeclared(Method(), ast.fun.name)

            c.methods.append(ast)
            return ast

        used_names = {"getInt", "putInt", "putIntLn",
                      "getString", "putString", "putStringLn", "putLn"}

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
        
        # Initialize struct_members with field names
        for struct_type in self.list_type:
            if isinstance(struct_type, StructType):
                if struct_type.name not in self.struct_members:
                    self.struct_members[struct_type.name] = []
                for field_name, _ in struct_type.elements:
                    if field_name in self.struct_members[struct_type.name]:
                        raise Redeclared(Field(), field_name)
                    self.struct_members[struct_type.name].append(field_name)
        
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
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("putLn", FuntionType()),
                Symbol("getBool", FuntionType()),
                Symbol("putFloat", FuntionType()),
                
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
        # res = self.lookup(ast.name, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Function(), ast.name)
        if any(obj.name == ast.name for obj in c[0]):
            raise Redeclared(Function(), ast.name)
        oldfunc = self.function_current

        param_types = [self.visit(param.parType, c) for param in ast.params]
        ret_type = self.visit(ast.retType, c) if ast.retType else VoidType()
        local_env = [[]] + c
        self.function_current = ast

        for param in ast.params:
            param_sym = self.visitParamDecl(param, local_env)
            local_env[0].append(param_sym)

        self.visit(ast.body, local_env)
        self.function_current = oldfunc

        return Symbol(ast.name, FuntionType(), None)

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # TODO: Implement
        # res = self.lookup(ast.parName, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Parameter(), ast.parName)
        if any(obj.name == ast.parName for obj in c[0]):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        # TODO: Implement
        # Get the receiver type (struct type)
        recType = ast.recType
        receiver_type = self.lookup(
            ast.recType.name, self.list_type, lambda x: x.name)
        # or not isinstance(receiver_type, StructType):
        if not receiver_type and isinstance(recType, Id):
            raise Undeclared(Identifier(), ast.recType.name)
        if isinstance(recType, Id):
            recType = self.lookup(receiver_type.name,
                                  self.list_type, lambda x: x.name)

        # Check if method name already exists in the struct
        if self.lookup(ast.fun.name, receiver_type.methods, lambda x: x.fun.name):
            raise Redeclared(Method(), ast.fun.name)

        # Create local environment for method parameters
        methoddecl = Symbol(ast.recType.name, receiver_type, None)
        local_env = [[]] + c
        local_env[0].append(methoddecl)

        # Process parameters and add them to local environment
        for param in ast.fun.params:
            param_sym = self.visit(param, local_env)
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

        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res != None:  # Explicitly check for None
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
        found = False
        for sym in c[0]:
            if sym.name == ast.conName:
                found = True
                break
        if found:
            raise Redeclared(Constant(), ast.conName)

        LHS_type = ast.conType if ast.conType else None
        RHS_type = self.visit(ast.iniExpr, c) if ast.iniExpr else None

        initValue = self.compute_expression(ast.iniExpr, c)
        c[0].append(Symbol(ast.conName, RHS_type, initValue))
        return Symbol(ast.conName, RHS_type, initValue)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c

        for ele in ast.member:
            result = self.visit(ele, (acc, True)) if isinstance(
                ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        visit = self.visit(ast.cond, c)
        if not isinstance(visit, BoolType): raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        # Create a new scope for the for loop
        loop_env = [[]] + c
        
        # Visit the initialization statement
        init_result = self.visit(ast.init, loop_env)
        if isinstance(init_result, Symbol):
            loop_env[0] = [init_result] + loop_env[0]
        
        # Check condition type
        cond_type = self.visit(ast.cond, loop_env)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), loop_env)
        
        # # Visit the loop body with the loop environment
        # self.visit(ast.loop, loop_env)
        
        # # Visit the update statement
        # self.visit(ast.upda, loop_env)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        # type_array = self.visit(ast.arr, c)
        # if not isinstance(type_array, ArrayType):
        #     raise TypeMismatch(ast)
        # if len(type_array.dimens) == 1:
        #     value_type = type_array.eleType
        # else:
        #     value_type = ArrayType(type_array.dimens[1:], type_array.eleType)

        # self.visit(Block([VarDecl(ast.idx.name, IntType(), None),
        #             VarDecl(ast.value.name,
        #                     value_type,
        #                     None)] + ast.loop.member), c)
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        
        type_idx = self.visit(ast.idx, c)
        if not isinstance(type_idx, IntType):
            raise TypeMismatch(ast)
        
        type_value = self.visit(ast.value, c)
        if len(type_array.dimens) == 1:
            element_type = type_array.eleType
        else:
            element_type = ArrayType(type_array.dimens[1:], type_array.eleType)
            
        if not self.checkType(type_value, element_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)          

        self.visit(Block(ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = None
        for scope in c:
            result = self.lookup(ast.name, scope, lambda x: x.name)
            if result:
                res = result
                break
        if res and not isinstance(res.mtype, Function):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        # # First check if the function name is shadowed by a local variable
        # for scope in c:
        #     local_sym = self.lookup(ast.funName, scope, lambda x: x.name)
        #     if local_sym:
        #         # If we found a local symbol with the same name, it shadows the function
        #         raise Undeclared(Function(), ast.funName)
        
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)

        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.params, ast.args):
                arg_type = self.visit(arg, c)
                if res.name == "putFloat":
                    # putFloat không cho phép chuyển đổi int -> float
                    if not isinstance(arg_type, FloatType):
                        raise TypeMismatch(ast)
                if not self.checkType(param.parType, arg_type, [(FloatType, IntType)]):
                    raise TypeMismatch(ast)

            if is_stmt and isinstance(res.retType, VoidType):
                return res.retType
            if not is_stmt and not isinstance(res.retType, VoidType):
                return res.retType
            raise TypeMismatch(ast)
        else:
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
        demension = []
        for dim in ast.dimens:
            val = self.compute_expression(dim, c)
            if val is None or val < 0:
                raise TypeMismatch(ast)
            demension.append(val)
            
            if not isinstance(dim, Id):
                value = self.compute_expression(dim, c)
                if value is None or value < 0:
                    raise TypeMismatch(ast)
                demension.append(value)
            else:
                value = self.visit(dim, c)
                if not isinstance(value, IntType):
                    raise TypeMismatch(ast)
                demension.append(value.value)

        elemT = self.visit(ast.eleType, c)
        return ArrayType(demension, elemT)

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
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
                c[0] = [Symbol(ast.lhs.name, rhs_type, None)] + c[0]
        LHS_type = self.visit(ast.lhs, c)
        RHS_type = self.visit(ast.rhs, c)

        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            if len(LHS_type.dimens) != len(RHS_type.dimens):
                raise TypeMismatch(ast)
        if not self.checkType(LHS_type.eleType, RHS_type.eleType, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)
        return None

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        expr = self.visit(ast.expr, c)
        if not isinstance(expr, BoolType):
            raise TypeMismatch(ast)

        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            # TODO: Implement
            self.visit(ast.elseStmt, c)
        return None

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
                if isinstance(LHS_type, FloatType) or isinstance(RHS_type, FloatType):
                    return FloatType()
                if isinstance(LHS_type, StringType) or isinstance(RHS_type, StringType):
                    return StringType()
                return IntType()
        if ast.op in ['*', '/']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS_type, FloatType) or isinstance(RHS_type, FloatType):
                    return FloatType()
                if isinstance(LHS_type, StringType) or isinstance(RHS_type, StringType):
                    return StringType()
                return IntType()
        if ast.op == '%':
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS_type, IntType) and isinstance(RHS_type, FloatType):
                    raise TypeMismatch(ast)
                if isinstance(LHS_type, IntType) and isinstance(RHS_type, IntType):
                    return IntType()
        if ast.op in ['&&', '||']:
            if type(LHS_type) != type(RHS_type):
                raise TypeMismatch(ast)
            if (isinstance(LHS_type, StringType) and isinstance(RHS_type, StringType)) or \
               (isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType)):
                return BoolType()
        if ast.op in ['==', '!=']:
            if type(LHS_type) != type(RHS_type):
                raise TypeMismatch(ast)
            if (isinstance(LHS_type, StringType) and isinstance(RHS_type, StringType)) or \
               (isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType)):
                return BoolType()
        if ast.op in ['<', '>', '<=', '>=']:
            if type(LHS_type) != type(RHS_type):
                raise TypeMismatch(ast)
            if (isinstance(LHS_type, IntType) or isinstance(LHS_type, FloatType)) and \
               (isinstance(RHS_type, IntType) or isinstance(RHS_type, FloatType)):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        expr_type = self.visit(ast.body, c)
        # TODO: Implement
        if ast.op == '!':
            if isinstance(expr_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)

        elif ast.op in ['-']:
            if isinstance(expr_type, IntType):
                return IntType()
            elif isinstance(expr_type, FloatType):
                return FloatType()
            else:
                raise TypeMismatch(ast)

        raise TypeMismatch(ast) 

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        if not all(map(lambda item: self.checkType(self.visit(item, c), IntType()), ast.idx)):
            raise TypeMismatch(ast)

        if len(arr_type.dimens) == len(ast.idx):
            return arr_type.eleType
        elif len(arr_type.dimens) > len(ast.idx):
            return ArrayType(arr_type.dimens[len(ast.idx):], arr_type.eleType)
        raise TypeMismatch(ast)

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
        nested2recursive(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast: StructLiteral, c: List[List[Symbol]]) -> Type:
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return self.lookup(ast.name, self.list_type, lambda x: x.name)

    def visitNilLiteral(self, ast: NilLiteral,
                        c: List[List[Symbol]]) -> Type: return StructType("", [], [])
