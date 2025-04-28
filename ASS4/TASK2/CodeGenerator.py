from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
from typing import Union, Any


class CodeGenerator(BaseVisitor, Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None # Dùng để lưu kiểu của mảng khi duyệt vào 1 ArrayCell
        self.arrayCellType = None
        self.list_type = {}
        self.struct: StructType = None

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()],
                   VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()],
                   VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()],
                   VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType(
                [FloatType()], VoidType()), CName("io", True)),
            # TODO implement
            Symbol("putBool", MType([BoolType()],
                                    VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()],
                   VoidType()), CName("io", True)),
            Symbol("putString", MType(
                [StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType(
                [StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True))
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType(
            [], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
            # Tạo biến "this" trong phương thức <init>
            self.className), frame.getStartLabel(), frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR(
            "this", ClassType(self.className), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<cinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD(
            "<clinit>", MType([], VoidType()), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        # Process global variable initializations
        # for item in ast.decl:
        #     if isinstance(item, VarDecl) and item.varInit:
                
        #         # Generate code for the initialization expression
        #         rhsCode, rhsType = self.visit(item.varInit, env)
        #         self.emit.printout(rhsCode)
        #         # Store the result in the static field
        #         self.emit.printout(self.emit.emitPUTSTATIC(
        #             f"{self.className}.{item.varName}", rhsType, frame))
        self.visit(Block([
                Assign(Id(item.varName), item.varInit) if isinstance(item, VarDecl) else
                Assign(Id(item.varName), item.value)
                for item in ast.decl if isinstance(item, (VarDecl, ConstDecl))
            ]), env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)),
                                         item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        env = {}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a)
                     if isinstance(x, VarDecl) or isinstance(x, ConstDecl) else a, ast.decl, env)
        reduce(lambda a, x: self.visit(x, a) if isinstance(
            x, FuncDecl) else a, ast.decl, env)
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())
        
        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })
        return env

    # TODO decl ------------------------------
    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:
        self.function = ast
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(
                list(map(lambda x: x.parType, ast.params)), ast.retType)

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                [None], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc, e: self.visit(e, acc), ast.params, env)
        self.visit(ast.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(
            index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        # varInit = ast.varInit
        # varType = ast.varType
        # if not varInit:
        #     if type(varType) is IntType:
        #         varInit = IntLiteral(0)
        #     elif type(varType) is FloatType:
        #         varInit = FloatLiteral(0.0)
        #     # TODO implement
        #     elif type(varType) is StringType:
        #         return StringLiteral("\"\"")
        #     elif type(varType) is BoolType:
        #         return BooleanLiteral("false")
        #     elif type(varType) is ArrayType:
        #         varInit = ArrayLiteral(varType.dimens, varType.dimens, varInit)
        #     ast.varInit = varInit
        
        def create_init(varType: Type, o: dict):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            elif type(varType) is ArrayType:
                # Create a default element for the base type
                baseInit = create_init(varType.eleType, o)
                
                # Create a properly nested structure based on dimensions
                def create_nested_init(dims, baseValue):
                    if not dims:
                        return baseValue
                    # Create a list with 'size' elements, each containing nested initializations
                    size = dims[0].value if isinstance(dims[0], IntLiteral) else 0
                    return [create_nested_init(dims[1:], baseValue) for _ in range(size)]
                
                # Create the nested initialization value
                return create_nested_init(varType.dimens, baseInit)
 
        varInit = ast.varInit  # Giá trị khởi tạo của biến
        varType = ast.varType  # Kiểu của biến

        # Nếu không có giá trị khởi tạo thì tự động gán cho nó 0, 0.0, false, "",..tùy vào kiểu biến
        if not varInit:
            varInit = create_init(varType, o)
            if type(varType) is ArrayType:
                if 'frame' in o:
                    o['frame'].push()
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varInit)
            ast.varInit = varInit

            
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType())
        rhsCode, rhsType = self.visit(varInit, env)
        if not varType:
            varType = rhsType

        if 'frame' not in o:  # global var
            o['env'][0].append(
                Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(
                ast.varName, varType, True, False, None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index)))
            # self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
            self.emit.printout(self.emit.emitVAR(
                index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            # TODO implement))
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode = rhsCode + self.emit.emitI2F(frame)
                # TODO implement
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(
                ast.varName, varType, index,  frame))
        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function), None)
        
        if o.get('stmt'):
            o["stmt"] = False
            # Generate code for each argument and append to output
            params_code = ""
            for arg in ast.args:
                arg_code, arg_type = self.visit(arg, o)
                params_code += arg_code
            
            # Emit the function call after parameters are pushed to stack
            self.emit.printout(params_code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))
            
            return o  # Return o since statements always return void
        
        # For expressions, generate code for parameters and function call
        output = ""
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, o)
            output += arg_code
        
        # Add the function call instruction
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
        
        # Return the generated code and return type since this is an expression
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(
            env['frame'].getStartLabel(), env['frame']))  # TODO implement))

        for item in ast.member:
            if type(item) is FuncCall:
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(
            env['frame'].getEndLabel(), env['frame']))  # TODO implement))
        env['frame'].exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.name, [
            j for i in o['env'] for j in i]), None)
        if o.get('isLeft'):
            if type(sym.value) is Index:
                # TODO implement), sym.mtype
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:
                # Use dot notation for static field access
                return self.emit.emitPUTSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, o['frame']), sym.mtype
        if type(sym.value) is Index:
            # TODO implement),sym.mtype
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:
            # Use dot notation for static field access
            return self.emit.emitGETSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) -> dict:
        # TODO implement),None):
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]), None):
            # return o  # TODO implement
            rhsCode, rhsType = self.visit(ast.rhs, o)
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.lhs.name, rhsType, Index(index)))
            self.emit.printout(self.emit.emitVAR(
                index, ast.lhs.name, rhsType, frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(
                ast.lhs.name, rhsType, index, frame))
            return o
        
        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode = rhsCode + self.emit.emitI2F(o['frame'])
            # TODO implement
        # self.emit.printout(rhsCode)
        # self.emit.printout(lhsCode)

        # Increase stack size by 1, as we'll use the stack to store the value of this variable
        o['frame'].push() 
        if type(ast.lhs) is ArrayCell:
            if 'frame' in o:
                o['frame'].push()
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(self.arrayCell, o['frame'])) 
            ## TODO  )
        # access id
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
        # TODO implement, o['frame']))
        self.emit.printout(self.emit.emitRETURN(
            self.function.retType, o['frame']))
        return o

    # TODO END decl ------------------------------

    # TODO basic expression ------------------------------
    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)
        
        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(
                typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                # TODO implement
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            # TODO implement
            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
        
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(
                typeRight) is IntType else FloatType()  # TODO implement
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                # TODO implement
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            # TODO implement
            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
        
        if op in ['%']:
            # TODO implement
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            # TODO implement
            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), BoolType()
        if op in ['||']:
            # TODO implement
            return codeLeft + codeRight + self.emit.emitOROP(frame), BoolType()
        if op in ['&&']:
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType()

        # string
        if op in ['+'] and type(typeLeft) is StringType:
            # String concatenation should use concat method, not +
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL(
                "java/lang/String/concat", MType([StringType()], StringType()), frame)
            return code, StringType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL(
                "java/lang/String/compareTo", MType([StringType()], IntType()), frame)
            # TODO implement + self.emit.emitREOP(op, IntType(), frame)
            code = code + \
                self.emit.emitPUSHICONST(
                    0, frame) + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()

        # TODO implement
        code, type_return = self.visit(ast.body, o)
        if ast.op == '-':
            return code + self.emit.emitNEGOP(type_return, o['frame']), type_return
        return code, type_return

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        # TODO implement
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        # TODO implement
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        # TODO implement
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()

    # TODO END basic expression ------------------------------

    ## TODO array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO)
        #TODO visit thằng expr của array cell này, nên nhớ arraycell gồm phần expr phía trước và index phía sau.
        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType 
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame']) #TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = retType # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx): ], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame']) #TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = retType # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        return codeGen, retType
        #TODO trả vè mã nãy giờ tạo để thằng nào gọi thằng đó in và type -> tuple[str, Type]:

    def visitArrayLiteral(self, ast:ArrayLiteral , o: dict) -> tuple[str, Type]:

        # def nested2recursive(dat: Union[Literal, list]|Any, o: dict) -> tuple[str, Type]:
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            #dat có thể là 1 Literal hoặc là 1 list chứa các Literal khác, nên mình sẽ kiểm tra xem dat có phải là list hay không.

            #Nếu là Literal thôi thì chỉ cần visit tới là xong, không cần đệ quy nữa, tham số o là 0
            if not isinstance(dat,list): 
                return self.visit(dat, o)  # Changed from 0 to o to avoid NoneType error

            #Nếu dat là 1 list thì đoạn code dưới sẽ giải quyết
            #chuẩn bị ngữ cảnh
            frame = o['frame'] # lấy frame từ o
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame) #sinh mã đẩy số lượng phần tử của mảng vào stack
            
            # # Handle empty list case
            # if len(dat) == 0:
            #     # Create an empty array with Object type
            #     codeGen += self.emit.emitANEWARRAY(VoidType(), frame)
            #     return codeGen, ArrayType([0], VoidType())

            #Trường hợp danh sách không lồng nhau(vì phần tử đầu tiên không phải là list)
            if not isinstance(dat[0],list):
                _, type_element_array = self.visit(dat[0], o)  # gọi hàm visit cho phần tử đầu tiên để lấy kiểu của nó
                codeGen += self.emit.emitNEWARRAY(type_element_array, frame)  # Create array with element type

                # Lặp qua từng phần tử trong danh sách:
                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(frame)  # Duplicate array reference on stack
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)  # Push index onto stack
                    item_code, _ = self.visit(item, o)  # Process the element value
                    codeGen += item_code  # Add code for element
                    codeGen += self.emit.emitASTORE(type_element_array, frame)  # Store element in array
                return codeGen, ArrayType([len(dat)], type_element_array)  # Return array type with dimension

            # trường hợp mảng 2 chiều 
            _, type_element_array = nested2recursive(dat[0], o)
            codeGen += self.emit.emitANEWARRAY(type_element_array, frame)  # Create array with nested type

            # Lặp qua từng phần tử trong danh sách:
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(frame)  # Duplicate array reference
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)  # Push index
                item_code, _ = nested2recursive(item, o)  # Process nested item
                codeGen += item_code  # Add code for nested item
                codeGen += self.emit.emitASTORE(type_element_array, frame)  # Store in array
            return codeGen, ArrayType([len(dat)] + type_element_array.dimens, type_element_array.eleType)  # Return array type with dimension

        if type(ast.value) is ArrayType:
            # Nếu là mảng 1 chiều thì mình sẽ gọi hàm visit cho nó, nếu là mảng 2 chiều thì mình sẽ gọi hàm đệ quy cho nó.
            # Nếu là mảng 3 chiều thì mình sẽ gọi hàm đệ quy cho nó, và cứ như vậy cho đến khi nào không còn mảng nữa thì thôi.
            return self.visit(ast.value, o)
        #Gọi hàm đệ quy trong đó tham số truyền vào là ast.value, o
        return nested2recursive(ast.value, o)

    def visitConstDecl(self, ast:ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def visitArrayType(self, ast:ArrayType, o):
        codeGen = ""
        # TODO : Lặp qua dimens để thêm code vào codeGen, dùng visit và lưu ý rằng visit sẽ trả về cặp mã và kiểu của nó.
        # Cuối cùng đủ tham số thì dùng emitMULTIANEWARRAY để tạo mảng mới.
        dimensions = []
        for dim in ast.dimens:
            dim_code, dim_type = self.visit(dim, o)
            codeGen += dim_code
            dimensions.append(dim)

        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast
    
    # def visitIf(self, ast: If, o: dict) -> dict:
    #     frame = o['frame']
    #     label_exit = frame.getNewLabel()
    #     label_end_if = ## TODO
    #     condCode, _ = self.visit(ast.expr, o)
    #     self.emit.printout(condCode)
    #     self.emit.printout(## TODO)
    #     self.visit(ast.thenStmt, o)
    #     self.emit.printout(## TODO)
    #     self.emit.printout(## TODO)

    #     if ast.elseStmt is not None:
    #         ## TODO
    #     self.emit.printout(## TODO)
    #     return o
    

    # def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
    #     frame = o['frame']
    #     frame.enterLoop()
    #     lable_new = ## TODO
    #     lable_Break = frame.getBreakLabel() 
    #     lable_Cont = ## TODO
    #     self.emit.printout(## TODO)
    #     self.emit.printout(self.visit(ast.cond, o)[0])
    #     self.emit.printout(## TODO)
    #     self.visit(## TODO)
    #     self.emit.printout(## TODO)
    #     self.emit.printout(## TODO)
    #     self.emit.printout(## TODO)
    #     frame.exitLoop()
    #     return o
    
    # def visitForStep(self, ast: ForStep, o: dict) -> dict:
    #     ## TODO

    # def visitForEach(self, ast, o: dict) -> dict:
    #     # thẩy bỏ qua (đặt thầy thầy có nói)
    #     return o

    # def visitContinue(self, ast, o: dict) -> dict:
    #     self.emit.printout(## TODO)
    #     return o

    # def visitBreak(self, ast, o: dict) -> dict:
    #     self.emit.printout(## TODO)
    #     return o