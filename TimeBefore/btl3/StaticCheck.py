# Bùi Hồ Hải Đăng - 2153289
from AST import *
from AST import VoidType
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
        
class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    def comparType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if len(LHS.size) != len(RHS.size): return False
            for i in range(len(LHS.size)):
                if LHS.size[i] != RHS.size[i]: return False
            return type(LHS.eleType) is type(RHS.eleType)
        else:
            if type(LHS) != type(RHS): return False
        return True
    

    def comparListType(self, listLHS, listRHS):
        if len(listLHS) != len(listRHS):
            return False
        for lhs, rhs in zip(listLHS, listRHS):
            if not self.comparType(lhs, rhs):
                return False
        return True
    
    def setTypeArray(self, typeArray, typeArrayZcode):
        
        print(len(typeArray.size), typeArrayZcode.eleType[0])
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        
        if len(typeArray.size) == 1: 
            #TODO implement
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    return False
            return True
        else: 
            #TODO implement   
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    # If the element type is Zcode, set its type to typeArray.eleType
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    # If the element type is ArrayZcode, recursively call setTypeArray
                    result = self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode[i])
                    if not result:
                        return False
            return True
            
    def visitProgram(self, ast, param):
        for i in ast.decl: self.visit(i, param)

        for func_name, func_zcode in self.listFunction.items():
            if func_zcode.body is False:
                raise NoDefinition(func_name)

        has_main = False
        for func_name, func_zcode in self.listFunction.items():
            if func_name == "main":
                if func_zcode.param == []:
                    if (type(func_zcode.typ) is VoidType) is True:
                        has_main = True
                        break
        if has_main is False:
            raise NoEntryPoint(ast) 
        

    def visitVarDecl(self, ast, param):
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        
        param[0][ast.name.name] = VarZcode(ast.varType)

        if ast.varInit:
            lType = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            rType = self.visit(ast.varInit, param)
            print(lType, rType.eleType if type(rType) is ArrayZcode else rType)
            
            if isinstance(lType, Zcode) and isinstance(rType, Zcode):
                raise TypeCannotBeInferred(ast)
            if isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                raise TypeCannotBeInferred(ast) 
            if not isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType):
                    raise TypeMismatchInStatement(ast)
                elif type(lType) is ArrayType:
                    print("hi")
                    if not self.setTypeArray(lType, rType):
                        raise TypeMismatchInStatement(ast)
            if isinstance(lType, Zcode) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                lType.typ = rType
            if isinstance(rType, Zcode) and (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType):
                rType.typ = lType
            if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                if not self.comparType(lType, rType):
                    raise TypeMismatchInStatement(ast)        

    def visitFuncDecl(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        
        for func_name, func_zcode in self.listFunction.items():
            if func_name == ast.name.name:
                if func_zcode.body is True:
                    raise Redeclared(Function(), ast.name.name)
                elif func_zcode.body is False and ast.body is None:
                    raise Redeclared(Function(), ast.name.name)        
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        for paramDecl in ast.param:
            if paramDecl.name.name in listParam:
                raise Redeclared(Parameter(), paramDecl.name.name)
            typ = self.visit(paramDecl.varType, param)
            listParam[paramDecl.name.name] = VarZcode(typ)
            typeParam.append(typ)   
        
        self.Return = False
        
        if ast.body is None:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            return
        if method:
            if self.comparListType(method.param, typeParam) is False:
                raise Redeclared(Function(), ast.name.name)
            self.listFunction[ast.name.name].body = True
            self.function = self.listFunction.get(ast.name.name)
            self.visit(ast.body, [listParam] + param)
            if self.Return is False:
                    if self.function.typ is None:
                        self.function.typ = VoidType()
                    elif not self.comparType(self.listFunction[ast.name.name].typ, VoidType()):
                        raise TypeMismatchInStatement(Return(None))
        else: 
            self.function = self.listFunction.get(ast.name.name)
            if ast.body:
                self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
                self.function = self.listFunction.get(ast.name.name)
                self.visit(ast.body, [listParam] + param)
                if self.Return is False:
                    if self.listFunction[ast.name.name].typ is None:
                        self.listFunction[ast.name.name].typ = VoidType()
                    elif not self.comparType(self.listFunction[ast.name.name].typ, VoidType()):
                        raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast, param):
        var_zcode = VarZcode()
        arr_zcode = ArrayZcode([])
        for scope in param:
            if ast.name in scope:
                var_zcode = scope[ast.name]
                if var_zcode.typ is None:
                    return var_zcode
                return var_zcode.typ
        raise Undeclared(Identifier(), ast.name)


    def visitCallExpr(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        if method is None:
            raise Undeclared(Function(), ast.name.name) 
        
        listLHS = method.param
        listRHS = []
        for arg in ast.args:
            listRHS.append(self.visit(arg, param))
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for lType, rType in zip(listLHS, listRHS):
            if isinstance(lType, Zcode) and isinstance(rType, Zcode):
                raise TypeCannotBeInferred(ast)
            if isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                raise TypeCannotBeInferred(ast) 
            if not isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                if type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType:
                    raise TypeMismatchInExpression(ast)
                elif type(lType) is ArrayType:
                    if self.setTypeArray(lType, rType) is False:
                        raise TypeMismatchInStatement(ast)
            if isinstance(lType, Zcode) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                lType.typ = rType
                lType = rType
            if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType) and isinstance(rType, Zcode):
                rType.typ = lType
                rType = lType
            if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                if not self.comparType(lType, rType):
                    raise TypeMismatchInExpression(ast)
            
        if method.typ is None:
            return method
        elif self.comparType(method.typ, VoidType):
            raise TypeMismatchInExpression(ast)
        else:
            return method.typ

    def visitCallStmt(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO implement
        if method is None:
            raise Undeclared(Function(), ast.name.name) 
          
        listLHS = method.param
        listRHS = []
        for arg in ast.args:
            listRHS.append(self.visit(arg, param))
        #print(listLHS, listRHS)

        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
        
        for lType, rType in zip(listLHS, listRHS):
            if isinstance(lType, Zcode) and isinstance(rType, Zcode):
                raise TypeCannotBeInferred(ast)
            if isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                raise TypeCannotBeInferred(ast) 
            if not isinstance(lType, Zcode) and isinstance(rType, ArrayZcode):
                if type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType:
                    raise TypeMismatchInStatement(ast)
                elif type(lType) is ArrayType:
                    if self.setTypeArray(lType, rType) is False:
                        raise TypeMismatchInStatement(ast)
            if isinstance(lType, Zcode) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                lType.typ = rType
                lType = rType
            if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType) and isinstance(rType, Zcode):
                rType.typ = lType
                rType = lType
            if (type(lType) is StringType or type(lType) is BoolType or type(lType) is NumberType or type(lType) is ArrayType) and (type(rType) is StringType or type(rType) is BoolType or type(rType) is NumberType or type(rType) is ArrayType):
                if not self.comparType(lType, rType):
                    raise TypeMismatchInStatement(ast)
        
        if method.typ is None:
            method.typ = VoidType()
        elif not self.comparType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        else:
            return method.typ

    def visitIf(self, ast, param):
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        if not isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                raise TypeMismatchInStatement(ast)
            elif type(LHS) is ArrayType:
                if self.setTypeArray(LHS, RHS) is False:
                    raise TypeMismatchInStatement(ast)
        if isinstance(RHS, Zcode):
            RHS = LHS
        if not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, [{}] + param)
        
        if ast.elifStmt != []:
            for expr, stmt in ast.elifStmt:
                RHS2 = self.visit(expr, param)
                
                if not isinstance(LHS, Zcode) and isinstance(RHS2, ArrayZcode):
                    if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                        raise TypeMismatchInStatement(ast)
                    elif type(LHS) is ArrayType:
                        if self.setTypeArray(LHS, RHS2) is False:
                            raise TypeMismatchInStatement(ast)
                if isinstance(RHS2, Zcode):
                    RHS2 = LHS
                elif not self.comparType(LHS, RHS2):
                    raise TypeMismatchInStatement(ast)
                
                self.visit(stmt, [{}] + param)
                
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
     
    def visitFor(self, ast, param):
        LHS = NumberType()
        RHS = self.visit(ast.name, param)

        if not isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                raise TypeMismatchInStatement(ast)
            elif type(LHS) is ArrayType:
                if self.setTypeArray(LHS, RHS) is False:
                    raise TypeMismatchInStatement(ast)
        if isinstance(RHS, Zcode):
            RHS = LHS
        if not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

        LHS2 = BoolType()
        RHS2 = self.visit(ast.condExpr, param)

        if not isinstance(LHS2, Zcode) and isinstance(RHS2, ArrayZcode):
            if type(LHS2) is StringType or type(LHS2) is BoolType or type(LHS2) is NumberType:
                raise TypeMismatchInStatement(ast)
            elif type(LHS2) is ArrayType:
                if self.setTypeArray(LHS2, RHS2) is False:
                    raise TypeMismatchInStatement(ast)
        if isinstance(RHS2, Zcode):
            RHS2 = LHS2
        elif not self.comparType(LHS2, RHS2):
            raise TypeMismatchInStatement(ast)

        LHS3 = NumberType()
        RHS3 = self.visit(ast.updExpr, param)
        
        if not isinstance(LHS3, Zcode) and isinstance(RHS3, ArrayZcode):
            if type(LHS3) is StringType or type(LHS3) is BoolType or type(LHS3) is NumberType:
                raise TypeMismatchInStatement(ast)
            elif type(LHS3) is ArrayType:
                if self.setTypeArray(LHS3, RHS3) is False:
                    raise TypeMismatchInStatement(ast)
        if isinstance(RHS3, Zcode):
            RHS3 = LHS3
        elif not self.comparType(LHS3, RHS3):
            raise TypeMismatchInStatement(ast)
        
        self.BlockFor += 1
        self.visit(ast.body, [{}] + param) 
        self.BlockFor -= 1 
        
    def visitReturn(self, ast, param):
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()

        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            #print("hi")
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            #print("hi2")
            raise TypeCannotBeInferred(ast) 
        if not isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
                if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                    raise TypeMismatchInStatement(ast)
                elif type(LHS) is ArrayType:
                    if self.setTypeArray(LHS, RHS) is False:
                        raise TypeMismatchInStatement(ast)
        if isinstance(LHS, Zcode) and (type(RHS) is StringType or type(RHS) is BoolType or type(RHS) is NumberType or type(RHS) is ArrayType or type(RHS) is VoidType):
            #print("hi2")
            self.function.typ = RHS
            LHS = RHS
        elif isinstance(RHS, Zcode) and (type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType or type(LHS) is ArrayType or type(LHS) is VoidType):
            RHS.typ = LHS
            RHS = LHS
        if not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        
        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ast) 
        if not isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                raise TypeMismatchInStatement(ast)
            elif type(LHS) is ArrayType:
                if self.setTypeArray(LHS, RHS) is False:
                    raise TypeMismatchInStatement(ast)
        if isinstance(LHS, Zcode) and (type(RHS) is StringType or type(RHS) is BoolType or type(RHS) is NumberType or type(RHS) is ArrayType):
                LHS.typ = RHS
                LHS = RHS
        elif isinstance(RHS, Zcode) and (type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType or type(LHS) is ArrayType):
            RHS.typ = LHS
            RHS = LHS
        if not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
            

    def visitBinaryOp(self, ast, param):
        op = ast.op

        if op in ['+', '-', '*', '/', '%']:
            left = self.visit(ast.left, param)
            LHS = NumberType()
            if isinstance(left, Zcode):
                left.typ = LHS
            elif not self.comparType(LHS, left):
                # print("oe")
                raise TypeMismatchInExpression(ast)
        if op in ['=', '!=', '<', '>', '>=', '<=']:
            left = self.visit(ast.left, param)
            LHS = NumberType()
            if isinstance(left, Zcode):
                left.typ = LHS
            elif not self.comparType(LHS, left):
                raise TypeMismatchInExpression(ast)
        if op in ['and', 'or']:
            left = self.visit(ast.left, param)
            LHS = BoolType()
            if isinstance(left, Zcode):
                # print("huhu")
                left.typ = LHS
            elif not self.comparType(LHS, left):
                raise TypeMismatchInExpression(ast)
        if op in ['...', '==']:
            left = self.visit(ast.left, param)
            LHS = StringType()
            if isinstance(left, Zcode):
                left.typ = LHS
            elif not self.comparType(LHS, left):
                raise TypeMismatchInExpression(ast)

        left2 = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        if op in ['+', '-', '*', '/', '%']:
            if isinstance(left2, Zcode):
                left2.typ = NumberType()
                
            if isinstance(right, Zcode):
                right.typ = NumberType()
            
            right2 = self.visit(ast.right, param)
            if self.comparType(left2, NumberType()) and self.comparType(right2, NumberType()):
                return NumberType()
            # print("hu1", left2, right)
            raise TypeMismatchInExpression(ast)
        if op in ['=', '!=', '<', '>', '>=', '<=']:
            # print("hu1", left2, right)
            if isinstance(left2, Zcode):
                left2.typ = NumberType()
                
            if isinstance(right, Zcode):
                right.typ = NumberType()
                
            right2 = self.visit(ast.right, param)
            if self.comparType(left2, NumberType()) and self.comparType(right2, NumberType()):
                return BoolType()

            raise TypeMismatchInExpression(ast)
        if op in ['and', 'or']:
            # print("hu1", left2, right)
            if isinstance(left2, Zcode):
                left2.typ = BoolType()
                
            if isinstance(right, Zcode):
                right.typ = BoolType()
            
            right2 = self.visit(ast.right, param)
            if self.comparType(left2, BoolType()) and self.comparType(right2, BoolType()):
                return BoolType()

            raise TypeMismatchInExpression(ast)
        if op in ['...', '==']:
            # print("hu1", left2, right)
            if isinstance(left2, Zcode):
                left2.typ = StringType()
                
            if isinstance(right, Zcode):
                right.typ = StringType()
            
            right2 = self.visit(ast.right, param)
            if self.comparType(left2, StringType()) and self.comparType(right2, StringType()):
                return StringType()

            raise TypeMismatchInExpression(ast)
            
    def visitUnaryOp(self, ast, param):
        right = self.visit(ast.operand, param)
        op = ast.op
 
        if op in ['+', '-']:
            RHS = NumberType()
            if isinstance(right, Zcode):
                right.typ = RHS
            elif not self.comparType(RHS, right):
                raise TypeMismatchInExpression(ast)
        elif op in ['not']:
            RHS = BoolType()
            if isinstance(right, Zcode):
                right.typ = RHS
            elif not self.comparType(RHS, right):
                raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, param):
        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType or (isinstance(left, (BoolType, StringType, NumberType))):
            raise TypeMismatchInExpression(ast)

        for idx in ast.idx:
            LHS = NumberType()
            RHS = self.visit(idx, param)
            if not isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
                if type(LHS) is StringType or type(LHS) is BoolType or type(LHS) is NumberType:
                    raise TypeMismatchInExpression(ast)
                elif type(LHS) is ArrayType:
                    if self.setTypeArray(LHS, RHS) is False:
                        raise TypeMismatchInExpression(ast)
            if not self.comparType(LHS, RHS):
                raise TypeMismatchInExpression(ast)

        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        if len(left.size) == len(ast.idx):
            return left.eleType
        return ArrayType(left.size[len(ast.idx):], left.eleType)

    def visitArrayLiteral(self, ast, param):
        typ = None
        for item in ast.value:

            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break

        if typ is None:
            #TODO implement
            return ArrayZcode([self.visit(item, param) for item in ast.value])

        elif type(typ) in [StringType, BoolType, NumberType]:
            #TODO implement      
            for item in ast.value:
                RHS = self.visit(item, param)
                if isinstance(RHS, Zcode):
                    RHS.typ = typ
                if not self.comparType(typ, RHS):
                    raise TypeMismatchInExpression(ast)
                if not self.comparType(typ, RHS) and isinstance(RHS, ArrayZcode):
                    return ArrayZcode(ast.value)

        else: 
            #TODO implement
            for item in ast.value:
                RHS = self.visit(item, param)
                if isinstance(RHS, Zcode):
                    RHS.typ = typ
                if isinstance(RHS, ArrayType):
                    if typ.size != RHS.size:
                        raise TypeMismatchInExpression(ast)
                if isinstance(RHS, ArrayZcode):
                    self.setTypeArray(typ, RHS)
            # return ArrayType([len(ast.value)], typ)

    def visitBlock(self, ast, param):
        paramNew = [{}] + param
        for item in ast.stmt: 
            self.visit(item,paramNew)             
    def visitContinue(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()