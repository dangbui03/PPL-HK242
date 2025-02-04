"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
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
        name = Id(ctx.ID().getText()) 
        type = self.visit(ctx.types()) if ctx.types() else None
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        
        return VariablesDecl(name, type, varInit)

    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        name = Id(ctx.ID().getText()) 
        # type = self.get_type(ctx.types().getText()) if ctx.types() else None
        varInit = self.visit(ctx.expr())
        
        return ConstDecl(name, varInit)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        name = Id(ctx.ID().getText()) 
        fields = self.visit(ctx.struct_fields()) if ctx.struct_fields() else []
        
        return StructDecl(name, fields)


    # Visit a parse tree produced by MiniGoParser#struct_fields.
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        if ctx.struct_fields():
            return [self.visit(ctx.struct_field())] + self.visit(ctx.struct_fields())
        else: return [self.visit(ctx.struct_field())]


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        obj = None
        fieldName = Id(ctx.ID().getText())
        
        if ctx.primitive_types():
            obj = self.visit(ctx.primitive_types())
        elif ctx.composite_types():
            obj = self.visit(ctx.composite_types())
        else: obj = self.visit(ctx.arr_type())
        
        return VariablesDecl(fieldName, obj, None)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        name = Id(ctx.ID().getText())
        returnType = self.visit(ctx.types()) if ctx.types() else VoidType()
        methodReceiver = self.visit(ctx.method_para())
        param = self.visit(ctx.list_para()) if ctx.list_para() else []
        stmts = self.visit(ctx.block_statement())
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)

        # Visit a parse tree produced by MiniGoParser#method_para_list.
    def visitMethod_para_list(self, ctx:MiniGoParser.Method_para_listContext):
        if ctx.method_para_list():
            return [self.visit(ctx.method_para())] + self.visit(ctx.method_para_list())
        else: return [self.visit(ctx.method_para())]


    # Visit a parse tree produced by MiniGoParser#method_para.
    def visitMethod_para(self, ctx:MiniGoParser.Method_paraContext):
        name = Id(ctx.ID().getText())
        type = ClassType(self.visit(ctx.composite_types()))
        varInit = None
        
        return VariablesDecl(name, type, varInit)        


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        name = Id(ctx.ID().getText())
        fields = self.visit(ctx.interface_method_list()) if ctx.interface_method_list() else []
        
        return InterfaceDecl(name, fields)


    # Visit a parse tree produced by MiniGoParser#interface_method_list.
    def visitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        if ctx.interface_method_list():
            return [self.visit(ctx.interface_method())] + self.visit(ctx.interface_method_list())
        else: return [self.visit(ctx.interface_method())]


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name = Id(ctx.ID().getText())
        returnType = self.visit(ctx.types()) if ctx.types() else None
        methodReceiver = None
        param = self.visit(ctx.interface_para_list()) if ctx.interface_para_list() else []
        stmts = []
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)


    # Visit a parse tree produced by MiniGoParser#interface_para_list.
    def visitInterface_para_list(self, ctx:MiniGoParser.Interface_para_listContext):
        if ctx.getChildCount() > 1:
            return [self.visit(ctx.interface_para())] + self.visit(ctx.interface_para_list())
        elif ctx.getChildCount() == 1: 
            return [self.visit(ctx.interface_para())]
        else: return []


    # Visit a parse tree produced by MiniGoParser#interface_para.
    def visitInterface_para(self, ctx:MiniGoParser.Interface_paraContext):
        name = Id(ctx.ID().getText())
        type = self.visit(ctx.types()) if ctx.types() else None
        varInit = None
        
        return VariablesDecl(name, type, varInit)       


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        name = Id(ctx.ID().getText())
        returnType = self.visit(ctx.types()) if ctx.types() else None
        methodReceiver = None
        param = self.visit(ctx.list_para()) if ctx.list_para() else []
        stmts = self.visit(ctx.block_statement())
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)


    # Visit a parse tree produced by MiniGoParser#list_para.
    def visitList_para(self, ctx:MiniGoParser.List_paraContext):
        if ctx.getChildCount() > 1:
            return [self.visit(ctx.para())] + self.visit(ctx.list_para())
        elif ctx.getChildCount() == 1: 
            return [self.visit(ctx.para())]
        else: return []


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        name = Id(ctx.ID().getText())
        type = self.visit(ctx.types())
        varInit = None
        
        return VariablesDecl(name, type, varInit)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visit(ctx.list_statement()) if ctx.list_statement() else []


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
        if (ctx.variable_decl()):
            return self.visit(ctx.variable_decl())
        else: return self.visit(ctx.const_decl())


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        lhs = self.visit(ctx.lhs_list())
        exp = self.visit(ctx.expr())
        assign = self.visit(ctx.ass_operator())
        
        return AssignStmt(lhs, assign, exp)


    # Visit a parse tree produced by MiniGoParser#lhs_list.
    def visitLhs_list(self, ctx:MiniGoParser.Lhs_listContext):
        if (ctx.lhs_list()):
            return [self.visit(ctx.lhs())] + self.visit(ctx.lhs_list())
        else: return [self.visit(ctx.lhs())]


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if (ctx.arr_type()):
            return self.visit(ctx.arr_type())
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        else: return self.visit(ctx.getChild(0).getText())


    # Visit a parse tree produced by MiniGoParser#ass_operator.
    def visitAss_operator(self, ctx:MiniGoParser.Ass_operatorContext):
        return self.visit(ctx.getChild(0).getText())


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        expr = self.visit(ctx.expr())
        thenStmt = [self.visit(ctx.block_statement())] if ctx.block_statement() else []
        elifStmt = [self.visit(ctx.list_else_if_statement())] if ctx.list_else_if_statement() else []
        elseStmt = [self.visit(ctx.else_statement())] if ctx.else_statement() else []
        
        return If(expr, thenStmt, elifStmt, elseStmt)


    # Visit a parse tree produced by MiniGoParser#list_else_if_statement.
    def visitList_else_if_statement(self, ctx:MiniGoParser.List_else_if_statementContext):
        if (ctx.list_else_if_statement()):
            return self.visit(ctx.else_if_statement) + self.visit(ctx.list_else_if_statement())
        return self.visit(ctx.else_if_statement)
        


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
        initStmt = None
        if (ctx.value_assign()):
            index = Id(ctx.value_assign().ID().getText())
            value = self.visit(ctx.value_assign())
            array = self.visit(ctx.expr())
            loop = [self.visit(ctx.block_statement())] if ctx.block_statement() else []
            
            return ForArray(index, value, array, loop)
        
        initStmt = self.visit(ctx.init_for_statement())
        expr = self.visit(ctx.expr())
        postStmt = self.visit(ctx.statement())
        loop = [self.visit(ctx.block_statement())] if ctx.block_statement() else []
        
        return For(initStmt, expr, postStmt, loop)


    # Visit a parse tree produced by MiniGoParser#init_for_statement.
    def visitInit_for_statement(self, ctx:MiniGoParser.Init_for_statementContext):
        if (ctx.variable_decl()):
            return self.visit(ctx.variable_decl())
        else: return self.visit(ctx.assign_statement())


    # Visit a parse tree produced by MiniGoParser#value_assign.
    def visitValue_assign(self, ctx:MiniGoParser.Value_assignContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        obj = self.visit(ctx.lhs_list()) if ctx.lhs_list() else None
        method = Id(ctx.ID().getText())
        if ctx.lhs_list().lhs().ID():
            obj = self.visit(ctx.lhs_list())
        param = [self.visit(ctx.list_expr())] if ctx.list_expr() else []
        
        return CallStmt(obj, method, param)


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
        if ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.exprd():
            return self.visit(ctx.exprd())
        elif ctx.expr(): # Handle array indexing
            arr = self.visit(ctx.primary_expr())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr, idx)
        #     base_expr = self.visit(ctx.primary_expr())
        #     index_expr = self.visit(ctx.expr())
        #     return base_expr + index_expr
        elif ctx.ID():
            obj = self.visit(ctx.primary_expr())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.list_expr()) if ctx.list_expr() else []
            if param != []:
                return CallExpr(obj, method, param)
            return FieldAccess(obj, method)
        #     base_expr = self.visit(ctx.primary_expr())
        #     expr = self.visit(ctx.expr()) if ctx.expr() else None
        #     if ctx.LPAREN() and ctx.RPAREN():  
        #         param = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        #         return base_expr + expr + param
        #     return base_expr + expr
        # else: return 1


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
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.list_expr()) if ctx.list_expr() else []
        
        return CallExpr(None, method, param)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        obj = self.visit(ctx.expr())
        method = Id(ctx.ID().getText())
        param = [self.visit(ctx.list_expr())] if ctx.list_expr() else []
        
        return CallExpr(obj, method, param)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        if ctx.primitive_types():
            return self.visit(ctx.primitive_types())
        elif ctx.composite_types():
            return self.visit(ctx.composite_types())
        else: return self.visit(ctx.arr_type())


    # Visit a parse tree produced by MiniGoParser#primitive_types.
    def visitPrimitive_types(self, ctx:MiniGoParser.Primitive_typesContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
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
        type = self.visit(ctx.types()) if ctx.types() else None
        dimensions = self.visit(ctx.index_operator())
        
        return ArrayType(type, dimensions)


    # Visit a parse tree produced by MiniGoParser#index_operator.
    def visitIndex_operator(self, ctx:MiniGoParser.Index_operatorContext):
        if ctx.index_operator():
            return [int(ctx.DEC_LIT().getText())] + self.visit(ctx.index_operator())
        else: return [int(ctx.DEC_LIT().getText())]


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        name = Id(ctx.ID().getText())
        value = self.visit(ctx.list_field()) if ctx.list_field() else []
        
        return StructLiteral(name, value)


    # Visit a parse tree produced by MiniGoParser#list_field.
    def visitList_field(self, ctx: MiniGoParser.List_fieldContext):
        # Handle a single field
        if ctx.list_field():
            return [self.visit(ctx.field())] + self.visit(ctx.list_field())
        return [self.visit(ctx.field())]

    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx: MiniGoParser.FieldContext):
        # Extract the ID and the corresponding expression
        field_id = Id(ctx.ID().getText())
        field_expr = self.visit(ctx.expr())
        return [field_id, field_expr]


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        typ = self.visit(ctx.arr_type().types()) if ctx.arr_type().types() else None
        dimensions = self.visit(ctx.arr_type().index_operator())
        value = self.visit(ctx.arr_list()) if ctx.arr_list() else []
        
        return ArrayLiteral(typ, dimensions, value)


    def visitArr_list(self, ctx: MiniGoParser.Arr_listContext):
        if ctx.LBRACE() and ctx.arr_list():  # Handle nested array
            nested_array = self.visit(ctx.arr_list())
            return [nested_array]  # Wrap nested array in a list for consistency
        elif ctx.list_expr():  # Handle a list of values
            list_values = self.visit(ctx.list_expr())  # Visit the list_expr
            if ctx.COMMA() and ctx.arr_list():  # Handle the optional comma and additional arr_list
                additional_list = self.visit(ctx.arr_list())
                return list_values + additional_list  # Combine current values with the rest
            return list_values  # Return only the current list of values
        else:
            return []


    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return IntLiteral(int(ctx.DEC_LIT().getText()))


    # Visit a parse tree produced by MiniGoParser#float_lit.
    def visitFloat_lit(self, ctx:MiniGoParser.Float_litContext):
        return FloatLiteral(float(ctx.getChild(0).getText()))


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        if ctx.FALSE():
            return BooleanLiteral(False)
        else:
            return BooleanLiteral(True)


    # Visit a parse tree produced by MiniGoParser#str_lit.
    def visitStr_lit(self, ctx:MiniGoParser.Str_litContext):
        return StringLiteral(ctx.STR_LIT().getText())


    # Visit a parse tree produced by MiniGoParser#nil_lit.
    def visitNil_lit(self, ctx:MiniGoParser.Nil_litContext):
        return NilLiteral()

    # Visit a parse tree produced by MiniGoParser#newline.
    def visitNewline(self, ctx:MiniGoParser.NewlineContext):
        return self.visitChildren(ctx)
    