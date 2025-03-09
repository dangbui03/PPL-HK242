# Bùi Hồ Hải Đăng - 2153289
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

from typing import Tuple

class ASTGeneration(MiniGoVisitor): 
    
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # Visit a parse tree produced by MiniGoParser#decllist.
    def visitDecllist(self, ctx:MiniGoParser.DecllistContext):
        if ctx.decllist():
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        else: return [self.visit(ctx.decl())]


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        if ctx.variable_decl():
            return self.visit(ctx.variable_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())  
        elif ctx.func_decl():
            return self.visit(ctx.func_decl())
        elif ctx.method_decl():
            return self.visit(ctx.method_decl())
        elif ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        else: return self.visit(ctx.interface_decl())


    # Visit a parse tree produced by MiniGoParser#variable_decl.
    def visitVariable_decl(self, ctx:MiniGoParser.Variable_declContext):
        varName = ctx.ID().getText() 
        varType = self.visit(ctx.types()) if ctx.types() else None
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        
        return VarDecl(varName, varType, varInit)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        conName = ctx.ID().getText() 
        conType = self.visit(ctx.types()) if ctx.types() else None
        iniExpr = self.visit(ctx.expr())
        
        return ConstDecl(conName, conType, iniExpr)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        name = ctx.ID().getText() 
        elements = self.visit(ctx.struct_fields()) if ctx.struct_fields() else []
        
        return StructType(name, elements, [])


    # Visit a parse tree produced by MiniGoParser#struct_fields.
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        if ctx.struct_fields():
            return [self.visit(ctx.struct_field())] + self.visit(ctx.struct_fields())
        else: return [self.visit(ctx.struct_field())]


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        name = ctx.ID().getText() 
        type = self.visit(ctx.types())
        
        return (name, type)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        receiver = ctx.ID(0).getText() #Id(ctx.ID(0).getText()) 
        recType = self.visit(ctx.composite_types())
        
        name = ctx.ID(1).getText() #Id(ctx.ID(1).getText())
        params = self.visit(ctx.list_para())
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        body = self.visit(ctx.block_statement())
        
        # funcDecl = FuncDecl(name, params, retType, body)
        
        return MethodDecl(receiver, recType, FuncDecl(name, params, retType, body))


    # # Visit a parse tree produced by MiniGoParser#method_para_list.
    # def visitMethod_para_list(self, ctx:MiniGoParser.Method_para_listContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by MiniGoParser#method_para.
    # def visitMethod_para(self, ctx:MiniGoParser.Method_paraContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        name = ctx.ID().getText() 
        methods = self.visit(ctx.interface_method_list())
        
        return InterfaceType(name, methods)


    # Visit a parse tree produced by MiniGoParser#interface_method_list.
    def visitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        if ctx.interface_method_list():
            return [self.visit(ctx.interface_method())] + self.visit(ctx.interface_method_list())
        else: return [self.visit(ctx.interface_method())]


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name = ctx.ID().getText()
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        params = self.visit(ctx.interface_para_list()) if ctx.interface_para_list() else []
        
        return Prototype(name, params, retType)


    # Visit a parse tree produced by MiniGoParser#interface_para_list.
    # def visitInterface_para_list(self, ctx:MiniGoParser.Interface_para_listContext):
    #     if ctx.getChildCount() > 1:
    #         return [self.visit(ctx.interface_para())] + self.visit(ctx.interface_para_list())
    #     elif ctx.getChildCount() == 1: 
    #         return [self.visit(ctx.interface_para())]
    #     else: return []
    def visitInterface_para_list(self, ctx: MiniGoParser.Interface_para_listContext):
        params = []
        
        # Duyệt qua các tham số
        if ctx.getChildCount() > 1:
            params = [self.visit(ctx.interface_para())] + self.visit(ctx.interface_para_list())
        elif ctx.getChildCount() == 1:
            params = [self.visit(ctx.interface_para())]
        
        # Kiểm tra và thay thế các None thành IntType nếu cần
        for i in range(len(params)):
            if params[i] is None:
                params[i] = IntType()  # Hoặc kiểu dữ liệu mặc định khác nếu cần
        
        # Trả về danh sách tham số đã xử lý
        return params


    # Visit a parse tree produced by MiniGoParser#interface_para.
    def visitInterface_para(self, ctx:MiniGoParser.Interface_paraContext):
        name = ctx.ID().getText() 
        type = self.visit(ctx.types()) if ctx.types() else None
        
        return type #ParamDecl(name, type)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.list_para())
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        body = self.visit(ctx.block_statement())
        
        return FuncDecl(name, params, retType, body)


    # Visit a parse tree produced by MiniGoParser#list_para.
    def visitList_para(self, ctx:MiniGoParser.List_paraContext):
        if ctx.getChildCount() > 1:
            return [self.visit(ctx.para())] + self.visit(ctx.list_para())
        elif ctx.getChildCount() == 1: 
            return [self.visit(ctx.para())]
        else: return []


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        name = ctx.ID().getText()
        type = self.visit(ctx.types())
        
        return ParamDecl(name, type)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return Block(self.visit(ctx.list_statement())) if ctx.list_statement() else Block([])


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        else: return [self.visit(ctx.statement())]


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.declared_statement():
            return self.visit(ctx.declared_statement())
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        lhs = self.visit(ctx.lhs())
        
        rhs = None
        #-=,*=,/=,%=
        if ctx.ass_operator().getText() == '+=': 
            rhs = BinaryOp('+', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '-=':
            rhs = BinaryOp('-', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '*=':
            rhs = BinaryOp('*', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '/=':
            rhs = BinaryOp('/', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '%=':
            rhs = BinaryOp('%', lhs, self.visit(ctx.expr()))
        else: rhs = self.visit(ctx.expr())
        
        return Assign(lhs, rhs)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        # if ctx.LBRACK():  
        #     base = self.visit(ctx.lhs()) 
        #     index = self.visit(ctx.expr())  
        #     return ArrayCell(base, [index]) 
        # elif ctx.DOT():  
        #     base = self.visit(ctx.lhs())
        #     field = ctx.ID().getText()
        #     return FieldAccess(base, field)
        # elif ctx.ID():  
        #     return Id(ctx.ID().getText()) 
        # return None
        
        # if ctx.ID():  
        #     return Id(ctx.ID().getText()) 
        # lhs = self.visit(ctx.lhs())
        # print(f'lhs: {lhs}')
        # if ctx.DOT():  
        #     #self.visit(ctx.lhs())
        #     field = ctx.ID().getText()
        #     return FieldAccess(self.visit(ctx.lhs()), field)
        # if type(lhs) == ArrayCell: #ctx.LBRACK():  
        #     return ArrayCell(lhs.arr, lhs.idx + [self.visit(ctx.expr())]) 
        # return ArrayCell(lhs, [self.visit(ctx.expr())])
    
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText()) 
        elif ctx.getChild(1).getText() == ".":
            base = self.visit(ctx.lhs())
            field = ctx.ID().getText()
            return FieldAccess(base, field)
        elif ctx.getChild(1).getText() == "[":
            base = self.visit(ctx.lhs()) 
            index = self.visit(ctx.expr())  
            return ArrayCell(base, [index]) 

        return None



    # Visit a parse tree produced by MiniGoParser#ass_operator.
    def visitAss_operator(self, ctx:MiniGoParser.Ass_operatorContext):
        return self.visitChildren(ctx)


    def recursive_if(self, list_else_if_statement:List[Tuple[Expr,Block]], else_statement: Block):
        if len(list_else_if_statement) == 0:
            return else_statement
        exp, block = list_else_if_statement[0]
        return If(
            exp,
            block,
            self.recursive_if(list_else_if_statement[1:], else_statement)
        )

    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block_statement()) 
        elseIfStmt = self.visit(ctx.list_else_if_statement()) if ctx.list_else_if_statement() else []  # recursive if
        elseStmt = self.visit(ctx.else_statement()) if ctx.else_statement() else None
        
        return If(expr, thenStmt, self.recursive_if(elseIfStmt, elseStmt))


    # Visit a parse tree produced by MiniGoParser#list_else_if_statement.
    def visitList_else_if_statement(self, ctx:MiniGoParser.List_else_if_statementContext):
        if (ctx.list_else_if_statement()):
            return [self.visit(ctx.else_if_statement())] + self.visit(ctx.list_else_if_statement())
        return [self.visit(ctx.else_if_statement())]


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        expr = self.visit(ctx.expr())
        Stmt = self.visit(ctx.block_statement())
        
        return (expr, Stmt) 


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        Stmt = self.visit(ctx.block_statement())
        
        return Stmt


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        if (ctx.init_for_statement()):
            init = self.visit(ctx.init_for_statement())
            cond = self.visit(ctx.expr())
            upda = self.visit(ctx.update_stament())
            loop = self.visit(ctx.block_statement())
            
            return ForStep(init, cond, upda, loop)
        elif (ctx.value_assign()):
            idx = Id(ctx.ID().getText())
            value = Id(self.visit(ctx.value_assign()))
            arr = self.visit(ctx.expr())
            loop = self.visit(ctx.block_statement()) 
            
            return ForEach(idx, value, arr, loop)
        
        elif (ctx.expr()):
            cond =  self.visit(ctx.expr())
            loop = self.visit(ctx.block_statement())
            
            return ForBasic(cond, loop)
            


    # Visit a parse tree produced by MiniGoParser#init_for_statement.
    def visitInit_for_statement(self, ctx:MiniGoParser.Init_for_statementContext):
        if (ctx.VAR()):
            varName = ctx.ID().getText() 
            varType = self.visit(ctx.types()) if ctx.types() else None
            varInit = self.visit(ctx.expr())
        
            return VarDecl(varName, varType, varInit)
        else:
            lhs = Id(ctx.ID().getText())
            rhs = self.visit(ctx.expr())
            
            return Assign(lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#update_stament.
    def visitUpdate_stament(self, ctx:MiniGoParser.Update_stamentContext):
        lhs = Id(ctx.ID().getText())
        rhs = None
        
        if ctx.ass_operator().getText() == '+=': 
            rhs = BinaryOp('+', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '-=':
            rhs = BinaryOp('-', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '*=':
            rhs = BinaryOp('*', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '/=':
            rhs = BinaryOp('/', lhs, self.visit(ctx.expr()))
        elif ctx.ass_operator().getText() == '%=':
            rhs = BinaryOp('%', lhs, self.visit(ctx.expr()))
        else: rhs = self.visit(ctx.expr())
        
        return Assign(lhs, rhs)


    # Visit a parse tree produced by MiniGoParser#value_assign.
    def visitValue_assign(self, ctx:MiniGoParser.Value_assignContext):
        return ctx.ID().getText()


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        # lhs = self.visit(ctx.lhs())  

        # if isinstance(lhs, FieldAccess):
        #     params = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        #     return MethCall(lhs.receiver, lhs.field, params)
        # elif isinstance(lhs, Id):
        #     method_name = ctx.lhs().ID().getText()  # Extract the method name directly
        #     params = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        #     return FuncCall(method_name, params)
        # else:
        #     params = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        #     return FuncCall(str(lhs), params)
        
        if ctx.lhs():
            lhs = self.visit(ctx.lhs())
            # if isinstance(lhs, FieldAccess):
            params = self.visit(ctx.list_expr()) if ctx.list_expr() else []
            return MethCall(lhs, ctx.ID().getText(), params)
        params = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        return FuncCall(ctx.ID().getText(), params)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        if ctx.list_expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.list_expr())
        else: return [self.visit(ctx.expr())]


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#and_expr.
    def visitAnd_expr(self, ctx:MiniGoParser.And_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#rela_expr.
    def visitRela_expr(self, ctx:MiniGoParser.Rela_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#add_expr.
    def visitAdd_expr(self, ctx:MiniGoParser.Add_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#mul_expr.
    def visitMul_expr(self, ctx:MiniGoParser.Mul_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#unary_expr.
    def visitUnary_expr(self, ctx:MiniGoParser.Unary_exprContext):
        if ctx.getChildCount() > 1:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        # If it's just an ID or a literal, return the corresponding node
        # self_expr = 
        if ctx.exprd():
            return self.visit(ctx.exprd())  # Expression
        elif ctx.func_call():
            return self.visit(ctx.func_call())  # Literal value
        
        self_expr = self.visit(ctx.primary_expr())
        if ctx.DOT():
            if ctx.LPAREN():
                receiver = self.visit(ctx.primary_expr()) #self.visit(ctx.primary_expr()) 
                methName = ctx.ID().getText()
                args = self.visit(ctx.list_expr()) if ctx.list_expr() else [] 
                return MethCall(receiver, methName, args)
            else: return FieldAccess(self.visit(ctx.primary_expr()), ctx.ID().getText())
        
        if type(self_expr) == ArrayCell: #ctx.LBRACK():
            return ArrayCell(self_expr.arr, self_expr.idx + [self.visit(ctx.expr())])
        return ArrayCell(self_expr, [self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#exprd.
    def visitExprd(self, ctx:MiniGoParser.ExprdContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.literals():
            return self.visit(ctx.literals())
        if ctx.expr():
            return self.visit(ctx.expr())


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        fullName = ctx.ID().getText()
        args = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        
        return FuncCall(fullName, args)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        receiver = self.visit(ctx.expr())
        metName = ctx.ID().getText()
        args = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        
        return MethCall(receiver, metName, args)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_types.
    def visitPrimitive_types(self, ctx:MiniGoParser.Primitive_typesContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()


    # Visit a parse tree produced by MiniGoParser#composite_types.
    def visitComposite_types(self, ctx:MiniGoParser.Composite_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#arr_type.
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        dimens = self.visit(ctx.index_operator())
        eleType = self.visit(ctx.types()) if ctx.types() else None
        
        return ArrayType(dimens, eleType)


    # Visit a parse tree produced by MiniGoParser#index_operator.
    def visitIndex_operator(self, ctx:MiniGoParser.Index_operatorContext):
        if ctx.index_operator():
            if ctx.int_lit():
                return [self.visit(ctx.int_lit())] + self.visit(ctx.index_operator())
            else: return [self.visit(ctx.struct_type())] + self.visit(ctx.index_operator())
        else: 
            if ctx.int_lit():
                return [self.visit(ctx.int_lit())]
            else: return [self.visit(ctx.struct_type())]


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.list_field()) if ctx.list_field() else []
        
        return StructLiteral(name, value)


    # Visit a parse tree produced by MiniGoParser#list_field.
    def visitList_field(self, ctx:MiniGoParser.List_fieldContext):
        if ctx.list_field():
            return [self.visit(ctx.field())] + self.visit(ctx.list_field())
        return [self.visit(ctx.field())]


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        field = ctx.ID().getText()
        receiver = self.visit(ctx.expr())
        return (field, receiver)


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        dimens = self.visit(ctx.arr_type().index_operator())
        eleType = self.visit(ctx.arr_type().types()) if ctx.arr_type().types() else None
        value = self.visit(ctx.arr_list())
        
        return ArrayLiteral(dimens, eleType, value)
        # if ctx.LBRACE() and ctx.arr_list():  # Handle nested array
        #     nested_array = self.visit(ctx.arr_list())
        #     return [nested_array]  # Wrap nested array in a list for consistency
        # elif ctx.list_expr():  # Handle a list of values
        #     list_values = self.visit(ctx.list_expr())  # Visit the list_expr
        #     if ctx.COMMA() and ctx.arr_list():  # Handle the optional comma and additional arr_list
        #         additional_list = self.visit(ctx.arr_list())
        #         return list_values + additional_list  # Combine current values with the rest
        #     return list_values  # Return only the current list of values
        # else:
        #     return []


    # Visit a parse tree produced by MiniGoParser#arr_list.
    def visitArr_list(self, ctx:MiniGoParser.Arr_listContext):
        arrlist = [self.visit(ctx.arr_ele())]
        if ctx.arr_list():
            arrlist.extend(self.visit(ctx.arr_list()))
        return arrlist


    # Visit a parse tree produced by MiniGoParser#arr_ele.
    def visitArr_ele(self, ctx:MiniGoParser.Arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext): 
        return IntLiteral(ctx.getChild(0).getText())


    # Visit a parse tree produced by MiniGoParser#float_lit.
    def visitFloat_lit(self, ctx:MiniGoParser.Float_litContext):
        return FloatLiteral(ctx.getChild(0).getText())


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        if ctx.FALSE():
            return BooleanLiteral(False)
        else:
            return BooleanLiteral(True)


    # Visit a parse tree produced by MiniGoParser#str_lit.
    def visitStr_lit(self, ctx:MiniGoParser.Str_litContext):
        result = ctx.STR_LIT().getText()
        # if result.startswith('"') and result.endswith('"'):
        #     result = result[1:-1]
        return StringLiteral(result)


    # Visit a parse tree produced by MiniGoParser#nil_lit.
    def visitNil_lit(self, ctx:MiniGoParser.Nil_litContext):
        return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#newline.
    def visitNewline(self, ctx:MiniGoParser.NewlineContext):
        return self.visitChildren(ctx)
