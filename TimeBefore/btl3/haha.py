"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 15/4/2024
"""

from AST import *
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
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
    def __str__(self):
        return f"VarZcode(type={self.typ})"

class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"

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
    
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}  {str(value)}")       
    
    def check(self):
        self.visit(self.ast, [{}])
        return None

    def LHS_RHS_stmt(self,LHS : Type, RHS : Type, ast):
        # print(f"LHS_RHS_stmt {LHS} {RHS}")
        #! ĐỌC TRONG DISCORD
        if isinstance(LHS, CannotBeInferredZcode) and isinstance(RHS, CannotBeInferredZcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS): raise TypeMismatchInStatement(ast)
        if isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, Zcode):
            LHS.typ = RHS
        if isinstance(RHS, Zcode):
            RHS.typ = LHS
        if not self.comparType(LHS, RHS): 
            raise TypeMismatchInStatement(ast)
        
        
        
    def LHS_RHS_expr(self, LHS : Type, RHS : Type,ast) -> bool:
        # print(f"LHS_RHS_EXPR {LHS} {RHS}")
        #! ĐỌC TRONG DISCORD
        if isinstance(LHS, CannotBeInferredZcode) and isinstance(RHS, CannotBeInferredZcode):
            return True
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            return True
        if isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            return True
        if isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS): raise TypeMismatchInStatement(ast)
        if isinstance(RHS, ArrayZcode):
            return True
        if isinstance(LHS, Zcode):
            LHS.typ = RHS
        if isinstance(RHS, Zcode):
            RHS.typ = LHS
        if not self.comparType(LHS, RHS): 
            raise TypeMismatchInStatement(ast)
        return False
        

    def comparType(self, LHS : Type, RHS : Type) -> bool:
    # """_comparListType
    #     #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
    #     #* TH1 nếu LHS và RHS khác kích thước -> Flase
    #     #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    # """    
        if type(LHS) is not type(RHS): return False
        elif type(LHS) is ArrayType:
            if len(LHS.size) != len(RHS.size): return False
            for i in range(len(LHS.size)):
                if LHS.size[i] != RHS.size[i]: return False
            return type(LHS.eleType) is type(RHS.eleType)
        return True
           
    def setTypeArray(self, typeArray, typeArrayZcode):
        #* Trường hợp size khác nhau
            if typeArray.size[0] != len(typeArrayZcode.eleType):
                return False
            
            # Case where the elements inside the array are primitive types (1-dimensional array)
            if len(typeArray.size) == 1:
                # Loop through each element in typeArrayZcode
                for i in range(len(typeArrayZcode.eleType)):
                    if isinstance(typeArrayZcode.eleType[i], Zcode):
                        # If the element is Zcode, set its type to typeArray.eleType
                        typeArrayZcode.eleType[i].typ = typeArray.eleType
                    elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                        # If the element is ArrayZcode, return False
                        return False
                return True
            
            # Case where the elements inside the array are array types (multi-dimensional array)
            else:
                # Loop through each element in typeArrayZcode
                for i in range(len(typeArrayZcode.eleType)):
                    if isinstance(typeArrayZcode.eleType[i], Zcode):
                        # If the element is Zcode, set its type to ArrayType(typeArray.size[1:], typeArray.eleType)
                        typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                    elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                        # If the element is ArrayZcode, recursively call setTypeArray
                        result = self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode[i])
                        if not result:
                            return False
                return True

    def visitProgram(self, ast, param):
        for i in ast.decl: self.visit(i, param)
        
        #TODO implement dùng for duyệt qua self.listFunction nếu item[i].body == Flase thì nén ra lỗi
        #TODO implement kiểm tra main có None hay không, main.param có rỗng hay không, main.typ có phải là VoidType hay không
        for func_name, func_zcode in self.listFunction.items():
            if func_zcode.body is False:
                raise NoDefinition(func_name)

        has_main = False
        for func_name, func_zcode in self.listFunction.items():
            if func_name == "main":
                # print(func_name, func_zcode.param == [], type(func_zcode.typ) is VoidType)
                if func_zcode.param == []:
                    if (type(func_zcode.typ) is VoidType) is True:
                        has_main = True
                        break
        if has_main is False:
            raise NoEntryPoint(ast) 
        
    def visitVarDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        if param[0].get(ast.name.name): raise Redeclared(Variable(), ast.name.name)
        
        param[0][ast.name.name] = VarZcode(ast.varType)
        
        if ast.varInit:
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
            LHS = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            RHS = self.visit(ast.varInit, param)
            self.LHS_RHS_stmt(LHS, RHS, ast)

    def visitFuncDecl(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared

        #^th1: KHAI BÁO TRƯỚC 1 PHẦN KHÔNG CÓ BODY
        if ast.body is None:
            typeParam = [] #! tìm ra listtype
            #TODO: implement 
            
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            return

         
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        #TODO: implement
        for paramDecl in ast.param:
            if paramDecl.name.name in listParam:
                raise Redeclared(Parameter(), paramDecl.name.name)
            typ = self.visit(paramDecl.varType, param)
            listParam[paramDecl.name.name] = VarZcode(typ)
            typeParam.append(typ)   

        #^TH2 khai báo 1 phần trước rồi lần này khai báo có body
        if method:
            ListLHS = self.listFunction[ast.name.name].param
            ListRHS = typeParam
            #TODO: implement kiểm tra 2 dánh sách có giống nhau không -> Redeclared(Function(), ast.name.name) 
            if self.comparListType(ListLHS, ListRHS) is False:
                raise Redeclared(Function(), ast.name.name)
            self.listFunction[ast.name.name].body = True
        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
        
        self.Return = False
        self.function = self.listFunction[ast.name.name] 
        self.visit(ast.body, [listParam] + param)
        if not self.Return:
            if self.listFunction[ast.name.name].typ is None: 
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))
                
 
    def visitId(self, ast, param):
        """
            # TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
                #^ đối với giá trị trả về nếu Id.typ = None thì trả về chính nó luôn Id, nếu cso Id.typ thì trả về typ của nó
                #^ return Id.typ if Id.typ else Id (trả cơ chế reference hay con trỏ)
                #^ https://www.geeksforgeeks.org/references-in-cpp/
            Vd reference:
                def visitId() :
                    param = [{'a' : VarZcode(None)}]
                    id = param[0].get('a')
                    return Id.typ if Id.typ else Id
                
                x = visitId() # lúc này x với VarZcode(None) là như 1
                x.typ = NumberType
                -> có thể hiểu param = [{'a' : VarZcode(None)}] chuyển thành param = [{'a' : VarZcode(NumberType)}]         
        """
        var_zcode = VarZcode()
        for scope in param:
            if ast.name in scope:
                var_zcode = scope[ast.name]
                if var_zcode.typ is None:
                    return var_zcode
                return var_zcode.typ
        raise Undeclared(Identifier(), ast.name)

    def visitCallExpr(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        if method is None:
            raise Undeclared(Function(), ast.name.name)
        
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        listLHS = method.param
        listRHS = []
        for arg in ast.args:
            listRHS.append(self.visit(arg, param))

        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = listLHS[i]
            RHS = listRHS[i]
            if self.LHS_RHS_expr(LHS, RHS, ast):
                return CannotBeInferredZcode()
        
        #TODo: implement nếu method.typ là voidtype -> TypeMismatchInExpression, nếu không thì trả về theo nguyên lí giống ID trên
        if isinstance(method.typ, VoidType):
            raise TypeMismatchInExpression(ast)
        if method.typ is None:
            return method
        return method.typ

    def visitCallStmt(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        if method is None:
            raise Undeclared(Function(), ast.name.name) 
        
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        listLHS = method.param
        listRHS = []
        for arg in ast.args:
            listRHS.append(self.visit(arg, param))
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
            
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
            LHS = listLHS[i]
            RHS = listRHS[i]
            self.LHS_RHS_stmt(LHS, RHS, ast)
    
        #TODO: implement nếu method.typ là None thì gán Voidtype, nếu không thì kiểm tra có phải voidtype hay không nén ra lỗi TypeMismatchInStatement
        if method.typ is None:
            method.typ = VoidType()
        elif not self.comparType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        else:
            return method.typ

    def visitIf(self, ast, param):
        """_typExpr_"""   
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)
        
        self.visit(ast.thenStmt, param)
        
        """_elifStmt_"""   
        for item in ast.elifStmt:
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng 
            LHS = BoolType()
            RHS = self.visit(item[0], param)
            self.LHS_RHS_stmt(LHS, RHS, ast)
            self.visit(item[1], param)           

        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)
        
    def visitFor(self, ast, param):
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """_typID_"""        
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng   
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)    
        
        """_typCondExpr_"""    
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng  
        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)

        """_typUpdExpr_"""            
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, param)
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    
    def visitReturn(self, ast, param):
        self.Return = True
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        self.LHS_RHS_stmt(LHS, RHS, ast)

    def visitAssign(self, ast, param):
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)
            
    def visitBinaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            left = self.visit(ast.left, param)
            if self.LHS_RHS_expr(LHS, left, ast):
                return CannotBeInferredZcode()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            left = self.visit(ast.left, param)
            if self.LHS_RHS_expr(LHS, left, ast):
                return CannotBeInferredZcode()
        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            left = self.visit(ast.left, param)
            LHS = BoolType()
            if self.LHS_RHS_expr(LHS, left, ast):
                return CannotBeInferredZcode()
        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            left = self.visit(ast.left, param)
            if self.LHS_RHS_expr(LHS, left, ast):
                return CannotBeInferredZcode()
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            left = self.visit(ast.left, param)
            if self.LHS_RHS_expr(LHS, left, ast):
                return CannotBeInferredZcode()


        """_right_        
            TƯƠNG TỰ LEFT     
        """        
        left2 = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        #TODO implement
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

    def visitUnaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí giống BinaryOp
            #* giống mấy thằng trong if
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       
        right = self.visit(ast.operand, param)
        op = ast.op
        #TODO implement   
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
        arr = self.visit(ast.arr, param)
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()

        for item in ast.idx:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = self.visit(item, param)
            RHS = NumberType()
            if self.LHS_RHS_expr(LHS, RHS, ast):
                return CannotBeInferredZcode()
            
            
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    def visitArrayLiteral(self, ast, param):
        mainTyp = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                mainTyp = checkTyp
            elif isinstance(checkTyp, CannotBeInferredZcode):
                return CannotBeInferredZcode()
        
        #^ TH1 : mainTyp is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        if mainTyp is None:
            #TODO: implement < 3 dòng 
            return ArrayZcode()
        
        for item in ast.value:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = mainTyp
            RHS = self.visit(item, param)
            if self.LHS_RHS_expr(LHS, RHS, ast):
                return CannotBeInferredZcode()

        
        #^ TH đầu tiên main là BoolType, StringType, NumberType
            #! trả về array có eleType là mainTyp và size là kích thước của ast.value
        #^ TH hai main là mảng
            #! trả về array có eleType là mainTyp.eleType và size là kích thước của [float(len(ast.value))] + mainTyp.size
        #TODO: implement
        if isinstance(mainTyp, (BoolType, StringType, NumberType)):
            return ArrayType(len(ast.value), mainTyp)
        else:
            return ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)            
        
            
    """phần này sẽ là cố định do ngắn quá :(( """
    def visitBlock(self, ast, param):
        paramNew = [{}] + param #! tăng tầm vực
        for item in ast.stmt: 
            self.visit(item,paramNew)   
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()