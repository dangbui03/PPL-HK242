# 2153289 - Bùi Hồ Hải Đăng

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
from typing import List, Tuple, Dict, Type


class CodeGenerator(BaseVisitor, Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None  # Dùng để lưu kiểu của mảng khi duyệt vào 1 ArrayCell
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

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        # Kiểm tra xem hai kiểu có tương thích hay không.
        # Gợi ý:
        # 1. Xử lý trường hợp RHS_type là StructType có tên rỗng (thường là nil literal).
        if type(RHS_type) == StructType and RHS_type.name == "":
            #  nil có thể gán cho InterfaceType, StructType hoặc Id.
            return isinstance(LSH_type, (InterfaceType, StructType, Id))

        # Resolve Id types thành kiểu thực tế từ self.list_type.
        LSH_type = self.lookup(LSH_type.name, self.list_type.values(
        ), lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type.values(
        ), lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type

        #  Kiểm tra các trường hợp dựa trên danh sách các cặp kiểu cho phép.
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            # Xử lý kiểm tra tương thích giữa InterfaceType và StructType.
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                #  Kiểm tra xem StructType có implement tất cả các phương thức của InterfaceType không.
                return all(
                    any(
                        # So sánh tên, kiểu trả về và kiểu tham số của phương thức.
                        struct_methods.fun.name == inteface_method.name and
                        self.checkType(struct_methods.fun.retType, inteface_method.retType) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.checkType(
                                struct_methods.fun.params[i].parType, inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LSH_type.methods
                )
            # Kiểm tra tương thích giữa hai InterfaceType hoặc hai StructType.
            if isinstance(LSH_type, (InterfaceType, StructType)) and isinstance(RHS_type, (InterfaceType, StructType)):
                # Hai kiểu này tương thích nếu chúng có cùng tên.
                return LSH_type.name == RHS_type.name

        #  Kiểm tra tương thích giữa hai ArrayType.
        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            # Hai kiểu mảng tương thích nếu số chiều bằng nhau, kích thước các chiều tương ứng bằng nhau và kiểu phần tử tương thích.
            return (len(LSH_type.dimens) == len(RHS_type.dimens)
                    and all(
                        l.value == r.value for l, r in zip(LSH_type.dimens, RHS_type.dimens)
            )
                and self.checkType(LSH_type.eleType, RHS_type.eleType, [list_type_permission[0]] if len(list_type_permission) != 0 else []))

        #  Kiểm tra tương thích giữa các kiểu cơ bản (IntType, FloatType, StringType, BoolType).
        # Gợi ý: Hai kiểu cơ bản tương thích nếu chúng cùng loại.
        return type(LSH_type) == type(RHS_type)

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType(
            [], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(
            # Tạo biến "this" trong phương thức <init>
            self.className), frame.getStartLabel(), frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR(
            "this", Id(self.className), 0, frame))
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
            Assign(Id(item.conName), item.iniExpr) if isinstance(
                item, ConstDecl) else item
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

    def arrayLitchange(self, size, typ):
        # size: [3,2,1]
        # typ: NumberType...
        if (len(size) == 1):
            if type(typ) is IntType:
                return ArrayLiteral([IntType(0) for _ in range(size)])
            if type(typ) is StringType:
                return ArrayLiteral([StringLiteral("") for _ in range(size)])
            if type(typ) is BoolType:
                return ArrayLiteral([BooleanLiteral(True) for _ in range(size)])
        else:
            # Extract integer value from the first dimension
            dim_value = size[0].value if hasattr(
                size[0], 'value') else int(size[0])
            return [self.arrayLitchange(size[1:], typ) for _ in range(dim_value)]

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        # varInit = ast.varInit
        # varType = ast.varType
        # if not varInit:
        #     if type(varType) is IntType:
        #         varInit = IntLiteral(0)
        #     elif type(varType) is FloatType:
        #         varInit = FloatLiteral(0.0)
        # 
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

                    if (isinstance(dims[0], Id)):
                        return ArrayType(varType.dimens, varType.eleType)
                    # Create a list with 'size' elements, each containing nested initializations
                    size = dims[0].value if isinstance(
                        dims[0], IntLiteral) else 1
                    return [create_nested_init(dims[1:], baseValue) for _ in range(size)]

                # Create the nested initialization value
                return create_nested_init(varType.dimens, baseInit)
                # return ArrayType(varType.dimens, varType.eleType)  # Return the type itself for array initialization
            elif isinstance(varType, (StructType, Id)):
            # For struct types, return nil literal
                return NilLiteral()

        varInit = ast.varInit  # Giá trị khởi tạo của biến
        varType = ast.varType  # Kiểu của biến

        # Nếu không có giá trị khởi tạo thì tự động gán cho nó 0, 0.0, false, "",..tùy vào kiểu biến
        if not varInit:
            varInit = create_init(varType, o)
            if type(varType) is ArrayType and not isinstance(varInit, ArrayType):
                if 'frame' in o:
                    o['frame'].push()
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varInit)
            ast.varInit = varInit

        env = o.copy()
        env['frame'] = Frame("<template_hd>", VoidType())
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

            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode = rhsCode + self.emit.emitI2F(frame)

            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(
                ast.varName, varType, index,  frame))
        return o

    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object")) # khởi tạo đầu file mô tả tên

        # .implements name
        for item in self.list_type.values(): # Lặp qua các type đc khai báo(interface/struct)
            # Lệnh if - tìm interface mà struct này đang implement(ast là struct mà mình visit), hàm checkType sẽ check 1 struct implement đc interface
            if isinstance(item, InterfaceType) and self.checkType(item, ast, [(InterfaceType, StructType)]): 
                self.emit.printout(f".implements {item.name}") # Sinh ra đoạn .implement ___ như ở ví dụ bên trên.

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0], item[1], False, False, False)) # danh sách các thuộc tính cần khởi tạo
        
        # khởi tạo Method contructor có giá trị parram (khác với constructor rỗng nha)
        self.visit(MethodDecl(None, ast.name, FuncDecl("<init>", [ParamDecl(item[0], None, item[1]) for item in ast.elements], VoidType(),
                                                   
                            Block([Assign(FieldAccess(Id("this"), item[0]), Id(item[0])) for item in ast.elements]))), o) 

        # khởi tạo Method contructor rỗng
        self.visit(MethodDecl(None, ast.name, FuncDecl("<init>", [], VoidType(), Block([])), o))

        # duyệt qua method
        for item in ast.methods: self.visit(item, o)
        self.emit.printout(self.emit.emitEPILOG()) # kết thúc khai báo của struct
    
    def visitMethodDecl(self, ast: MethodDecl, o):
        # Store reference to current function being processed
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType([x.parType for x in ast.fun.params], ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        
        # Create method with appropriate access modifiers
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)
        
        # Add "this" reference to the frame
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), "this", Id(ast.receiver), 
            frame.getStartLabel(), frame.getEndLabel(), frame)
        )
        
        # Start the method body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # For constructors, call superclass constructor
        if ast.fun.name == "<init>":
            self.emit.printout(self.emit.emitREADVAR("this", Id(ast.receiver), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # Create a new scope for method body to contain parameters
        # Find which global variables are accessible to this method
        if self.astTree and hasattr(self.astTree, 'decl'):
            # Find global variables declared before this struct
            struct_position = -1
            for i, item in enumerate(self.astTree.decl):
                if isinstance(item, MethodDecl) and item.struct_name == self.struct.name:
                    struct_position = i
                    break
            
            # Get global variables declared before this struct
            global_vars = []
            if struct_position >= 0:
                for i in range(struct_position):
                    if isinstance(self.astTree.decl[i], (VarDecl, ConstDecl)):
                        # Add to accessible globals
                        global_vars.append(o['env'][0][i])
            
            # Create new environment with only accessible globals
            env['env'] = [[]] + [global_vars] + env['env'][1:]
        else:
            # If we can't determine position, just use a new empty scope
            env['env'] = [[]] + env['env']
        
        # Add parameters to method scope
        for param in ast.fun.params:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                idx, param.parName, param.parType, 
                frame.getStartLabel(), frame.getEndLabel(), frame
            ))
            env['env'][0].append(Symbol(param.parName, param.parType, Index(idx)))
        
        # Process method body
        self.visit(ast.fun.body, env)
        
        # End the method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        return o

    def visitInterfaceType(self, ast: InterfaceType, o):
        # type Course interface {study();}

        # .source Course.java
        # .class public interface Course
        # .super java.lang.Object

        # .method public abstract study()V
        # .end method

        #Giống struct type thôi nhưng đơn giản hơn
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            # Sinh mã cho các prototype, nhớ này là abstract method
            mtype = MType([x for x in item.params], item.retType)
            self.emit.printout(f".method public abstract {item.name}{self.emit.emitMETHODTYPE(mtype)}")
            self.emit.printout(".end method")
            
        self.emit.printout(self.emit.emitEPILOG())

    def visitFieldAccess(self, ast: FieldAccess, o: dict) -> tuple[str, Type]:
        # Get the code and type of the receiver
        code, typ = self.visit(ast.receiver, o)
        
        # If typ is an Id, look up the actual type in self.list_type
        if isinstance(typ, Id):
            structType = self.lookup(typ.name, self.list_type.values(), lambda x: x.name)
            if structType:
                typ = structType
        
        # Find the field type in the struct
        fieldType = None
        if isinstance(typ, StructType):
            for element in typ.elements:
                if element[0] == ast.field:
                    fieldType = element[1]
                    break
        
        # For interface type, we might need to look for method signatures
        elif isinstance(typ, InterfaceType):
            for method in typ.methods:
                if method.name == ast.field:
                    fieldType = method.retType
                    break
        
        # Handle case when o['isLeft'] is True (assignment to a field)
        if o.get('isLeft'):
            return code, fieldType
        
        # Generate code to get the field value
        return code + self.emit.emitGETFIELD(f"{typ.name}/{ast.field}", fieldType, o['frame']), fieldType

    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
    
        # 1. Tạo mã cho receiver (đối tượng mà phương thức được gọi).
        code, typ = self.visit(ast.receiver, o)

        # 2. Lấy thông tin kiểu đầy đủ của receiver từ self.list_type.
        # 'typ' có thể chỉ là một Id (tên kiểu), cần lookup để lấy StructType hoặc InterfaceType.
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        # 3. Kiểm tra xem lời gọi phương thức này có phải là một statement hay một expression
        is_stmt = o.pop("stmt", False)

        # 4. Tạo mã cho các đối số của phương thức.
        param_types = []
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, o)
            code += arg_code
            param_types.append(arg_type)

        returnType = None
        # 5. Xử lý trường hợp receiver là một StructType (gọi phương thức thông thường).
        if isinstance(typ, StructType):
            # Tìm kiếm phương thức trong danh sách các phương thức của struct dựa trên tên.
            method = next((m for m in typ.methods if m.fun.name == ast.method), None)
            
            # Tạo MType (Method Type) cho lời gọi phương thức.
            # Lấy kiểu của các tham số và kiểu trả về từ FuncDecl của phương thức.
            mtype = MType([p.parType for p in method.fun.params], method.fun.retType)
            returnType = method.fun.retType
            # Tạo mã bytecode để gọi phương thức ảo (invokevirtual).
            # invokevirtual được sử dụng cho các phương thức instance.
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.method}", mtype, o['frame'])
            
        # 6. Xử lý trường hợp receiver là một InterfaceType (gọi phương thức interface).
        elif isinstance(typ, InterfaceType):
            # Tìm kiếm phương thức trong danh sách các phương thức của interface dựa trên tên.
            method = next((m for m in typ.methods if m.name == ast.method), None)
            
            # Tạo MType cho lời gọi phương thức interface.
            mtype = MType([p for p in method.params], method.retType)
            returnType = method.retType
            # Tạo mã bytecode để gọi phương thức interface (invokeinterface).
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.method}", mtype, o['frame'])
        
        # 7. Nếu lời gọi phương thức là một statement, in mã ra mà không trả về giá trị.
        if is_stmt:
            self.emit.printout(code)
            return o

        # 8. Nếu lời gọi phương thức là một expression, trả về mã và kiểu trả về của phương thức.
        return code, returnType

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        if frame is None:
            frame = Frame("<static>", VoidType())
        
        # Create a new instance of the struct
        code = self.emit.emitNEW(ast.name, frame)
        code += self.emit.emitDUP(frame)
        
        # Create named parameters if they exist
        param_types = []
        param_codes = ""
        
        # Find the struct type to get element types
        struct_type = self.lookup(ast.name, self.list_type.values(), lambda x: x.name)
        if struct_type:
            # Handle named initialization if elements have names
            if all(isinstance(elem, tuple) and len(elem) == 2 for elem in ast.elements):
                # Map by name
                name_to_elem = {name: value for name, value in ast.elements}
                for elem_name, elem_type in struct_type.elements:
                    if elem_name in name_to_elem:
                        code_part, type_part = self.visit(name_to_elem[elem_name], o)
                        param_codes += code_part
                        param_types.append(type_part)
            # Handle positional initialization
            else:
                for elem in ast.elements:
                    code_part, type_part = self.visit(elem, o)
                    param_codes += code_part
                    param_types.append(type_part)
        
        code += param_codes
        
        # Call the constructor
        mtype = MType(param_types, VoidType()) if param_types else MType([], VoidType())
        code += self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", mtype)
        
        return code, Id(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o: dict) -> tuple[str, Type]:
        # Gợi ý:
        # 1. Sử dụng self.emit.emitPUSHNULL để đẩy giá trị null lên stack.
        code = self.emit.emitPUSHNULL(o['frame'])
        # Trả về mã và kiểu của 'nil'.
        # Gợi ý:
        # 1. Kiểu của 'nil' thường là một kiểu tham chiếu đặc biệt hoặc có thể được biểu diễn bằng một Id rỗng.
        return code, Id("")

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = next(filter(lambda x: x.name ==
                   ast.funName, self.list_function), None)

        if o.get('stmt'):
            o["stmt"] = False
            # Generate code for each argument and append to output
            params_code = ""
            for arg in ast.args:
                arg_code, arg_type = self.visit(arg, o)
                params_code += arg_code

            # Emit the function call after parameters are pushed to stack
            self.emit.printout(params_code)
            self.emit.printout(self.emit.emitINVOKESTATIC(
                f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))

            return o  # Return o since statements always return void

        # For expressions, generate code for parameters and function call
        output = ""
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, o)
            output += arg_code

        # Add the function call instruction
        output += self.emit.emitINVOKESTATIC(
            f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])

        # Return the generated code and return type since this is an expression
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(
            env['frame'].getStartLabel(), env['frame']))  

        for item in ast.member:
            if isinstance(item, FuncCall) or isinstance(item, MethCall):
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(
            env['frame'].getEndLabel(), env['frame'])) 
        env['frame'].exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.name, [
            j for i in o['env'] for j in i]), None)
        
        if sym is None and self.struct:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this", Id(self.struct.name), 0, o['frame']), Id(self.struct.name)
            return self.emit.emitREADVAR("this", Id(self.struct.name), 0, o['frame']), Id(self.struct.name)
        if o.get('isLeft'):
            if type(sym.value) is Index:

                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:
                # Use dot notation for static field access
                return self.emit.emitPUTSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, o['frame']), sym.mtype
        if type(sym.value) is Index:

            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:
            # Use dot notation for static field access
            return self.emit.emitGETSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) -> dict:

        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]), None):
            # return o 
            # rhsCode, rhsType = self.visit(ast.rhs, o)
            # frame = o['frame']
            # index = frame.getNewIndex()
            # o['env'][0].append(Symbol(ast.lhs.name, rhsType, Index(index)))
            # self.emit.printout(self.emit.emitVAR(
            #     index, ast.lhs.name, rhsType, frame.getStartLabel(), frame.getEndLabel(), frame))
            # self.emit.printout(rhsCode)
            # self.emit.printout(self.emit.emitWRITEVAR(
            #     ast.lhs.name, rhsType, index, frame))
            # return o
            return self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)

        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False
        
        if type(ast.lhs) is FieldAccess:
            # For field access, we need: get the receiver, then set the field
            o['isLeft'] = False  # We're just accessing the object, not setting it directly
            receiverCode, receiverType = self.visit(ast.lhs.receiver, o)
            
            # Resolve Id type
            if isinstance(receiverType, Id):
                receiverType = self.lookup(receiverType.name, self.list_type.values(), lambda x: x.name)
            
            # Find field type
            fieldType = None
            if isinstance(receiverType, StructType) and hasattr(receiverType, 'elements'):
                for elem_name, elem_type in receiverType.elements:
                    if elem_name == ast.lhs.field:
                        fieldType = elem_type
                        break
            
            # Default to the right-hand side type if field type not found
            if fieldType is None:
                fieldType = rhsType
            
            # Push receiver reference and RHS value onto the stack
            self.emit.printout(receiverCode)
            self.emit.printout(rhsCode)
            
            # Convert types if needed
            if isinstance(fieldType, FloatType) and isinstance(rhsType, IntType):
                self.emit.printout(self.emit.emitI2F(o['frame']))
            
            # Store value in field
            self.emit.printout(self.emit.emitPUTFIELD(
                f"{receiverType.name}/{ast.lhs.field}", fieldType, o['frame']))

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode = rhsCode + self.emit.emitI2F(o['frame'])
            
        o['frame'].push()
        if type(ast.lhs) is ArrayCell:
            if 'frame' in o:
                o['frame'].push()
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(
                self.arrayCell, o['frame']))
            # TODO  )
        # access id
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
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
   
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)

            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn

        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(
                typeRight) is IntType else FloatType() 
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)

                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)

            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn

        if op in ['%']:
           
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()

        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:

            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), BoolType()
        if op in ['||']:
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
            code = code + \
                self.emit.emitPUSHICONST(
                    0, frame) + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()

        code, type_return = self.visit(ast.body, o)
        if ast.op == '-':
            return code + self.emit.emitNEGOP(type_return, o['frame']), type_return
        return code, type_return

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()

    # TODO END basic expression ------------------------------

    # TODO array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO)

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get('isLeft'):
                
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                
                self.arrayCell = retType
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
            if not o.get('isLeft'):
                
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                
                self.arrayCell = retType
        return codeGen, retType

    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:

        # def nested2recursive(dat: Union[Literal, list]|Any, o: dict) -> tuple[str, Type]:
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            # dat có thể là 1 Literal hoặc là 1 list chứa các Literal khác, nên mình sẽ kiểm tra xem dat có phải là list hay không.
            #     frame = o['frame']
            #     codeGen = self.emit.emitPUSHCONST(0, IntType(), frame)
            #     codeGen += self.emit.emitANEWARRAY(VoidType(), frame)
            #     return codeGen, ArrayType([0], VoidType())
            # Nếu là Literal thôi thì chỉ cần visit tới là xong, không cần đệ quy nữa, tham số o là 0
            if not isinstance(dat, list):
                # Changed from 0 to o to avoid NoneType error
                return self.visit(dat, o)

            # Nếu dat là 1 list thì đoạn code dưới sẽ giải quyết
            # chuẩn bị ngữ cảnh
            frame = o['frame']  # lấy frame từ o
            # sinh mã đẩy số lượng phần tử của mảng vào stack
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)

            # # Handle empty list case
            # if len(dat) == 0:
            #     # Create an empty array with Object type
            #     codeGen += self.emit.emitANEWARRAY(VoidType(), frame)
            #     return codeGen, ArrayType([0], VoidType())

            # Trường hợp danh sách không lồng nhau(vì phần tử đầu tiên không phải là list)
            if not isinstance(dat[0], list):
                # gọi hàm visit cho phần tử đầu tiên để lấy kiểu của nó
                _, type_element_array = self.visit(dat[0], o)
                # Create array with element type
                codeGen += self.emit.emitNEWARRAY(type_element_array, frame)

                # Lặp qua từng phần tử trong danh sách:
                for idx, item in enumerate(dat):
                    # Duplicate array reference on stack
                    codeGen += self.emit.emitDUP(frame)
                    # Push index onto stack
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                    # Process the element value
                    item_code, _ = self.visit(item, o)
                    codeGen += item_code  # Add code for element
                    # Store element in array
                    codeGen += self.emit.emitASTORE(type_element_array, frame)
                # Return array type with dimension
                return codeGen, ArrayType([len(dat)], type_element_array)

            # trường hợp mảng 2 chiều
            _, type_element_array = nested2recursive(dat[0], o)
            # Create array with nested type
            codeGen += self.emit.emitANEWARRAY(type_element_array, frame)

            # Lặp qua từng phần tử trong danh sách:
            for idx, item in enumerate(dat):
                # Duplicate array reference
                codeGen += self.emit.emitDUP(frame)
                # Push index
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                item_code, _ = nested2recursive(item, o)  # Process nested item
                codeGen += item_code  # Add code for nested item
                # Store in array
                codeGen += self.emit.emitASTORE(type_element_array, frame)
            # Return array type with dimension
            return codeGen, ArrayType([len(dat)] + type_element_array.dimens, type_element_array.eleType)

        if type(ast.value) is ArrayType:
            # Nếu là mảng 1 chiều thì mình sẽ gọi hàm visit cho nó, nếu là mảng 2 chiều thì mình sẽ gọi hàm đệ quy cho nó.
            # Nếu là mảng 3 chiều thì mình sẽ gọi hàm đệ quy cho nó, và cứ như vậy cho đến khi nào không còn mảng nữa thì thôi.
            return self.visit(ast.value, o)
        # Gọi hàm đệ quy trong đó tham số truyền vào là ast.value, o
        return nested2recursive(ast.value, o)

    def visitConstDecl(self, ast: ConstDecl, o: dict) -> dict:

        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast: ArrayType, o):
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

    def visitIf(self, ast: If, o: dict) -> dict:
        frame = o['frame']
        label_exit = frame.getNewLabel()
        label_end_if = frame.getNewLabel()  # TODO
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))  # TODO)
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(label_exit, frame))  # TODO)
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))  # TODO)

        if ast.elseStmt is not None:
            # TODO
            self.visit(ast.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(label_exit, frame))  # TODO)
        return o

    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()
        lable_new = frame.getNewLabel()  # TODO
        lable_Break = frame.getBreakLabel()
        lable_Cont = frame.getContinueLabel()  # TODO
        self.emit.printout(self.emit.emitLABEL(lable_new, frame))  # TODO)
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(lable_Break, frame))  # TODO)
        self.visit(ast.loop, o)  # TODO)
        self.emit.printout(self.emit.emitLABEL(lable_Break, frame))  # TODO)
        self.emit.printout(self.emit.emitLABEL(lable_new, frame))  # TODO)
        self.emit.printout(self.emit.emitLABEL(lable_Cont, frame))  # TODO)
        frame.exitLoop()
        return o

    def visitForStep(self, ast: ForStep, o: dict) -> dict:
        frame = o['frame']

        # ──────────────────────────────────────────────────────────────
        # 1. Create a *new* symbol scope for the whole loop
        # ──────────────────────────────────────────────────────────────
        loop_env = o.copy()
        loop_env['env'] = [[]] + loop_env['env']

        # ──────────────────────────────────────────────────────────────
        # 2. Emit the initialisation *outside* the loop context
        #    (this gives the loop‑local variable its own slot)
        # ──────────────────────────────────────────────────────────────
        self.visit(ast.init, loop_env)

        # ──────────────────────────────────────────────────────────────
        # 3. Now enter the real “loop context” (break/continue labels)
        # ──────────────────────────────────────────────────────────────
        frame.enterLoop()
        label_start = frame.getNewLabel()      # top‑of‑loop
        label_break = frame.getBreakLabel()    # for “break”
        label_continue = frame.getContinueLabel()  # for “continue”

        # ──────────────────────────────────────────────────────────────
        # 4.   start:
        # ──────────────────────────────────────────────────────────────
        self.emit.printout(self.emit.emitLABEL(label_start, frame))

        #    condition
        cond_code, _ = self.visit(ast.cond, loop_env)
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(label_break, frame))

        #    body
        self.visit(ast.loop, loop_env)

        # ──────────────────────────────────────────────────────────────
        # 5.   continue:          ←  target of every “continue”
        # ──────────────────────────────────────────────────────────────
        self.emit.printout(self.emit.emitLABEL(label_continue, frame))

        #    update
        self.visit(ast.upda, loop_env)

        #    goto start
        self.emit.printout(self.emit.emitGOTO(label_start, frame))

        # ──────────────────────────────────────────────────────────────
        # 6.   break:
        # ──────────────────────────────────────────────────────────────
        self.emit.printout(self.emit.emitLABEL(label_break, frame))

        frame.exitLoop()
        return o

    def visitForEach(self, ast: ForEach, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()

        # Get array reference
        arrCode, arrType = self.visit(ast.arr, o)
        self.emit.printout(arrCode)

        # Assuming the array is of type ArrayType and we know its element type
        eleType = arrType.eleType

        # Create a temporary local variable for the array
        tempArr = frame.getNewIndex()
        self.emit.printout(self.emit.emitWRITEVAR(
            "$arr", arrType, tempArr, frame))

        # Create index variable and initialize it to 0
        idxIndex = frame.getIndex(ast.idx.name)
        self.emit.printout(self.emit.emitPUSHICONST(0, frame))
        self.emit.printout(self.emit.emitWRITEVAR(
            ast.idx.name, IntType(), idxIndex, frame))

        # Get array length (assuming array.length operation is supported)
        self.emit.printout(self.emit.emitREADVAR(
            "$arr", arrType, tempArr, frame))
        self.emit.printout(self.emit.emitARRAYLEN(frame))

        # Store array length in a temporary variable
        tempLen = frame.getNewIndex()
        self.emit.printout(self.emit.emitWRITEVAR(
            "$len", IntType(), tempLen, frame))

        # Labels for loop
        label_start = frame.getNewLabel()
        label_break = frame.getBreakLabel()
        label_cont = frame.getContinueLabel()

        # Start of loop
        self.emit.printout(self.emit.emitLABEL(label_start, frame))

        # Check if index < array length
        self.emit.printout(self.emit.emitREADVAR(
            ast.idx.name, IntType(), idxIndex, frame))
        self.emit.printout(self.emit.emitREADVAR(
            "$len", IntType(), tempLen, frame))
        self.emit.printout(self.emit.emitREOP("<", IntType(), frame))

        # If condition is false (index >= length), break out of loop
        self.emit.printout(self.emit.emitIFFALSE(label_break, frame))

        # Get array element at current index
        self.emit.printout(self.emit.emitREADVAR(
            "$arr", arrType, tempArr, frame))
        self.emit.printout(self.emit.emitREADVAR(
            ast.idx.name, IntType(), idxIndex, frame))
        self.emit.printout(self.emit.emitALOAD(eleType, frame))

        # Store element value in the loop variable
        valueIndex = frame.getIndex(ast.value.name)
        self.emit.printout(self.emit.emitWRITEVAR(
            ast.value.name, eleType, valueIndex, frame))

        # Execute loop body
        self.visit(ast.loop, o)

        # Continue label
        self.emit.printout(self.emit.emitLABEL(label_cont, frame))

        # Increment index
        self.emit.printout(self.emit.emitREADVAR(
            ast.idx.name, IntType(), idxIndex, frame))
        self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP("+", IntType(), frame))
        self.emit.printout(self.emit.emitWRITEVAR(
            ast.idx.name, IntType(), idxIndex, frame))

        # Jump back to start of loop
        self.emit.printout(self.emit.emitGOTO(label_start, frame))

        # Break label
        self.emit.printout(self.emit.emitLABEL(label_break, frame))

        frame.exitLoop()
        return o

    def visitContinue(self, ast, o: dict) -> dict:
        # Jump to the continue label of the current loop
        self.emit.printout(self.emit.emitGOTO(
            o['frame'].getContinueLabel(), o['frame']))
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        # Jump to the break label of the current loop
        self.emit.printout(self.emit.emitGOTO(
            o['frame'].getBreakLabel(), o['frame']))
        return o
