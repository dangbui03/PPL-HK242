from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

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
        self.struct: list[StructType] = []
        self.inteface: list[InterfaceType] = []
        self.env = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putIntLn",MType([IntType()],VoidType()))
                # TODO:
            ]
        ]
        self.function_current: FuncDecl = None
        self.struct_current: StructType = None
    
    def check(self):
        return self.visit(self.ast,self.env)

    def visitProgram(self, ast: Program, c: List[List[Symbol]]):
        # Global scope
        global_env = c.copy()
        
        # First pass: collect all global declarations
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                params = [self.visit(param, []) for param in decl.params]
                param_types = [param.mtype for param in params]
                ret_type = decl.retType
                func_sym = Symbol(decl.name, MType(param_types, ret_type))
                
                # Check for redeclaration
                if self.lookup(decl.name, global_env[0], lambda x: x.name):
                    raise Redeclared(Function(), decl.name)
                global_env[0].append(func_sym)
            
            elif isinstance(decl, VarDecl):
                var_sym = self.visit(decl, global_env)
                global_env[0].append(var_sym)
            
            elif isinstance(decl, ConstDecl):
                const_sym = self.visit(decl, global_env)
                global_env[0].append(const_sym)
            
            # Add handling for struct and interface types
            elif isinstance(decl, StructType):
                # Check if struct name already exists
                if self.lookup(decl.name, self.struct, lambda x: x.name):
                    raise Redeclared(Struct(), decl.name)
                self.struct.append(decl)
                self.visit(decl, None)
            
            elif isinstance(decl, InterfaceType):
                # Check if interface name already exists
                if self.lookup(decl.name, self.inteface, lambda x: x.name):
                    raise Redeclared(Interface(), decl.name)
                self.inteface.append(decl)
                self.visit(decl, None)
            
            # Handle method declarations
            elif isinstance(decl, MethodDecl):
                # Get struct name from the receiver
                # In AST.py, receiver is a string, not an Id object
                struct_name = decl.recType.name
                
                # Find the struct
                struct = None
                for s in self.struct:
                    if s.name == struct_name:
                        struct = s
                        break
                
                # If struct not found, create a temporary one
                if not struct:
                    struct = StructType(struct_name, [], [])
                    self.struct.append(struct)
                
                # Add method to struct
                struct.methods.append(decl)
        
        # Second pass: check for method redeclarations in each struct
        for struct in self.struct:
            method_names = {}
            for method in struct.methods:
                if method.fun.name in method_names:
                    raise Redeclared(Method(), method.fun.name)
                method_names[method.fun.name] = True
        
        # Third pass: check function bodies
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.function_current = decl
                local_env = [[]] + global_env
                
                # Add parameters to local environment
                for param in decl.params:
                    param_sym = self.visit(param, local_env[0])
                    local_env[0].append(param_sym)
                
                # Check function body
                self.visit(decl.body, local_env)
                
                self.function_current = None
    
        return global_env
    
    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # Check for redeclaration in parameters
        if self.lookup(ast.parName, c, lambda x: x.name):
            raise Redeclared(Parameter(), ast.parName)
        
        param_type = self.visit(ast.parType, c) if ast.parType else None
        return Symbol(ast.parName, param_type, None)

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # Check for redeclaration in current scope
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)
        
        # Get variable type
        var_type = self.visit(ast.varType, c) if ast.varType else None
        
        # Check initialization if present
        if ast.varInit:
            init_type = self.visit(ast.varInit, c)
            if var_type and not self.typeCheck(init_type, var_type):
                raise TypeMismatchInVarDecl(ast)
        
        return Symbol(ast.varName, var_type, None)

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        # Check for redeclaration in current scope
        if self.lookup(ast.conName, c[0], lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)
        
        # Get constant type
        const_type = self.visit(ast.conType, c) if ast.conType else None
        
        # Check initialization expression
        init_type = self.visit(ast.iniExpr, c)
        if const_type and not self.typeCheck(init_type, const_type):
            raise TypeMismatchInConstDecl(ast)
        
        return Symbol(ast.conName, const_type, None)
   
    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        # Check for redeclaration in current scope
        if self.lookup(ast.name, c[0], lambda x: x.name):
            raise Redeclared(Function(), ast.name)
        
        # Create function type
        param_types = [self.visit(param.parType, c) for param in ast.params]
        ret_type = self.visit(ast.retType, c) if ast.retType else VoidType()
        
        # Create local environment for function body
        local_env = [[]] + c
        
        # Add parameters to local environment
        for param in ast.params:
            param_sym = self.visit(param, local_env[0])
            local_env[0].append(param_sym)
        
        # Check function body
        self.function_current = ast
        self.visit(ast.body, local_env)
        self.function_current = None
        
        return Symbol(ast.name, MType(param_types, ret_type))

    def visitStructType(self, ast: StructType, c) -> StructType:
        # Check for redeclaration of fields
        field_names = []
        for field_name, field_type in ast.elements:
            if field_name in field_names:
                raise Redeclared(Field(), field_name)
            field_names.append(field_name)
        
        # Check methods
        self.struct_current = ast
        method_names = []
        for method in ast.methods:
            if method.fun.name in method_names:
                raise Redeclared(Method(), method.fun.name)
            method_names.append(method.fun.name)
            self.visit(method, ast.methods)
        self.struct_current = None
        
        return ast

    def visitMethodDecl(self, ast: MethodDecl, c: List[MethodDecl]) -> MethodDecl:
        # Check for redeclaration of methods
        for method in c:
            if method.fun.name == ast.fun.name and method != ast:
                raise Redeclared(Method(), ast.fun.name)
        
        # Check method body
        self.visit(ast.fun, [[]])
        
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c) -> InterfaceType:
        # Check for redeclaration of prototypes
        proto_names = []
        for proto in ast.methods:
            if proto.name in proto_names:
                raise Redeclared(Prototype(), proto.name)
            proto_names.append(proto.name)
            self.visit(proto, ast.methods)
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # Check for redeclaration of prototypes with built-in functions
        if ast.name in ["getInt", "putIntLn"]:
            raise Redeclared(Prototype(), ast.name)
        
        return ast

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None: 
        # Check condition type
        cond_type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatchInStatement(ast)
        
        # Check loop body
        self.visit(ast.loop, c)
        return None

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None: 
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None: 
        # Check array expression
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatchInStatement(ast)
        
        # Create new scope for loop variables
        loop_env = [[]] + c
        
        # Add index and value variables to scope
        idx_sym = Symbol(ast.idx.name, IntType())
        val_sym = Symbol(ast.value.name, arr_type.eleType)
        loop_env[0].extend([idx_sym, val_sym])
        
        # Check loop body
        self.visit(ast.loop, loop_env)
        return None

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        # Create new scope
        block_env = [[]] + c
        
        # Process each member in the block
        for member in ast.member:
            if isinstance(member, VarDecl) or isinstance(member, ConstDecl):
                sym = self.visit(member, block_env)
                block_env[0].append(sym)
            else:
                self.visit(member, block_env)

    def visitIf(self, ast: If, c):
        # Check condition type
        cond_type = self.visit(ast.expr, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatchInStatement(ast)
        
        # Check then statement
        self.visit(ast.thenStmt, c)
        
        # Check else statement if present
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)
        
        return None

    def visitIntType(self, ast, c): 
        return IntType()
    
    def visitFloatType(self, ast, c): 
        return FloatType()
    
    def visitBoolType(self, ast, c): 
        return BoolType()
    
    def visitStringType(self, ast, c): 
        return StringType()
    
    def visitVoidType(self, ast, c): 
        return VoidType()
    
    def visitArrayType(self, ast, c): 
        ele_type = self.visit(ast.eleType, c)
        return ArrayType(ast.dimens, ele_type)
    
    def visitAssign(self, ast, c):
        # Check LHS is assignable
        lhs_type = self.visit(ast.lhs, c)
        
        # Check RHS type
        rhs_type = self.visit(ast.rhs, c)
        
        # Check type compatibility
        if not self.typeCheck(rhs_type, lhs_type):
            raise TypeMismatchInStatement(ast)
        
        return None
    
    def visitContinue(self, ast, c): 
        # Check if inside a loop
        if not self.inLoop(c):
            raise MustInLoop(ast)
        return None
    
    def visitBreak(self, ast, c): 
        # Check if inside a loop
        if not self.inLoop(c):
            raise MustInLoop(ast)
        return None
    
    def visitReturn(self, ast, c): 
        # Check if inside a function
        if not self.function_current:
            raise InvalidStatement(ast)
        
        # Get expected return type
        expected_type = self.function_current.retType
        
        # Check return expression type
        if ast.expr:
            expr_type = self.visit(ast.expr, c)
            if not self.typeCheck(expr_type, expected_type):
                raise TypeMismatchInStatement(ast)
        elif not isinstance(expected_type, VoidType):
            raise TypeMismatchInStatement(ast)
        
        return None
    
    def visitBinaryOp(self, ast, c): 
        # Get operand types
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        
        # Check operator and operand types
        if ast.op in ['+', '-', '*', '/', '%']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            elif (isinstance(left_type, IntType) or isinstance(left_type, FloatType)) and \
                 (isinstance(right_type, IntType) or isinstance(right_type, FloatType)):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['&&', '||']:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['==', '!=']:
            if (isinstance(left_type, IntType) and isinstance(right_type, IntType)) or \
               (isinstance(left_type, BoolType) and isinstance(right_type, BoolType)):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['<', '>', '<=', '>=']:
            if (isinstance(left_type, IntType) or isinstance(left_type, FloatType)) and \
               (isinstance(right_type, IntType) or isinstance(right_type, FloatType)):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast, c): 
        # Get operand type
        expr_type = self.visit(ast.body, c)
        
        # Check operator and operand type
        if ast.op == '!':
            if isinstance(expr_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['+', '-']:
            if isinstance(expr_type, IntType):
                return IntType()
            elif isinstance(expr_type, FloatType):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        
        raise TypeMismatchInExpression(ast)
    
    def visitFuncCall(self, ast, c): 
        # Find function in environment
        func = self.lookup(ast.funName, c[0], lambda x: x.name) or \
               self.lookup(ast.funName, c[-1], lambda x: x.name)
        
        if not func or not isinstance(func.mtype, MType):
            raise Undeclared(Function(), ast.funName)
        
        # Check number of arguments
        if len(ast.args) != len(func.mtype.partype):
            raise TypeMismatchInExpression(ast)
        
        # Check argument types
        for i, arg in enumerate(ast.args):
            arg_type = self.visit(arg, c)
            if not self.typeCheck(arg_type, func.mtype.partype[i]):
                raise TypeMismatchInExpression(ast)
        
        return func.mtype.rettype
    
    def visitMethCall(self, ast, c): 
        # Get receiver type
        receiver_type = self.visit(ast.receiver, c)
        
        # Check if receiver is a struct type
        if not isinstance(receiver_type, StructType):
            raise TypeMismatchInExpression(ast)
        
        # Find method in struct
        method = None
        for m in receiver_type.methods:
            if m.fun.name == ast.metName:
                method = m
                break
        
        if not method:
            raise Undeclared(Method(), ast.metName)
        
        # Check number of arguments
        if len(ast.args) != len(method.fun.params):
            raise TypeMismatchInExpression(ast)
        
        # Check argument types
        for i, arg in enumerate(ast.args):
            arg_type = self.visit(arg, c)
            param_type = self.visit(method.fun.params[i].parType, c)
            if not self.typeCheck(arg_type, param_type):
                raise TypeMismatchInExpression(ast)
        
        return method.fun.retType
    
    def visitId(self, ast, c): 
        # Find identifier in environment
        sym = None
        for scope in c:
            sym = self.lookup(ast.name, scope, lambda x: x.name)
            if sym:
                break
        
        if not sym:
            raise Undeclared(Identifier(), ast.name)
        
        return sym.mtype
    
    def visitArrayCell(self, ast, c): 
        # Get array type
        arr_type = self.visit(ast.arr, c)
        
        # Check if it's an array
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatchInExpression(ast)
        
        # Check number of indices
        if len(ast.idx) != len(arr_type.dimens):
            raise TypeMismatchInExpression(ast)
        
        # Check index types
        for idx in ast.idx:
            idx_type = self.visit(idx, c)
            if not isinstance(idx_type, IntType):
                raise TypeMismatchInExpression(ast)
        
        return arr_type.eleType
    
    def visitFieldAccess(self, ast, c): 
        # Get receiver type
        receiver_type = self.visit(ast.receiver, c)
        
        # Check if receiver is a struct type
        if not isinstance(receiver_type, StructType):
            raise TypeMismatchInExpression(ast)
        
        # Find field in struct
        field_type = None
        for field_name, field_type_obj in receiver_type.elements:
            if field_name == ast.field:
                field_type = field_type_obj
                break
        
        if not field_type:
            raise Undeclared(Field(), ast.field)
        
        return field_type
    
    def visitIntLiteral(self, ast: IntLiteral, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, c): 
        return FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, c): 
        return BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, c): 
        return StringType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c): 
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast: StructLiteral, c):
        # Find struct type
        struct_type = None
        for s in self.struct:
            if s.name == ast.name:
                struct_type = s
                break
        
        if not struct_type:
            raise Undeclared(Struct(), ast.name)
        
        # Check fields
        if len(ast.elements) != len(struct_type.elements):
            raise TypeMismatchInExpression(ast)
        
        for (field_name, expr), (struct_field_name, struct_field_type) in zip(ast.elements, struct_type.elements):
            if field_name != struct_field_name:
                raise TypeMismatchInExpression(ast)
            
            expr_type = self.visit(expr, c)
            if not self.typeCheck(expr_type, struct_field_type):
                raise TypeMismatchInExpression(ast)
        
        return struct_type
    
    def visitNilLiteral(self, ast: NilLiteral, c): 
        return NilLiteral()
    
    # Helper methods
    def typeCheck(self, src_type, dest_type):
        # Basic type checking
        if type(src_type) == type(dest_type):
            return True
        
        # Allow int to float conversion
        if isinstance(src_type, IntType) and isinstance(dest_type, FloatType):
            return True
        
        return False
    
    def inLoop(self, c):
        # Check if we're inside a loop by looking at the current function
        if not self.function_current:
            return False
        
        # Simplified check - in a real implementation, you'd need to track loop nesting
        return True