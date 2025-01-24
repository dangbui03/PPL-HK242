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
        declared = [self.visit(decl) for decl in ctx.decl()]
        return self.visit(declared)


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
        type = self.get_type(ctx.types().getText()) if ctx.types() else None
        varInit = self.visit(ctx.list_expr()) if ctx.list_expr() else None
        
        return VariablesDecl(name, type, varInit)

    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        name = Id(ctx.ID().getText()) 
        # type = self.get_type(ctx.types().getText()) if ctx.types() else None
        varInit = self.visit(ctx.list_expr()) # if ctx.list_expr() else None
        
        return ConstDecl(name, varInit)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        name = Id(ctx.ID().getText()) 
        fields = [self.visit(field) for field in ctx.struct_fields()] if ctx.struct_fields() else []
        
        return StructDecl(name, fields)


    # Visit a parse tree produced by MiniGoParser#struct_fields.
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        if ctx.struct_fields():
            return self.visit(ctx.struct_field()) + self.visit(ctx.struct_fields())
        else: return self.visit(ctx.struct_field())


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        obj = None
        fieldName = Id(ctx.ID().getText())
        
        if ctx.primitive_types():
            obj = self.get_type(ctx.primitive_types().getText())
        elif ctx.composite_types():
            obj = self.get_type(ctx.composite_types())
        else: obj = self.get_type(ctx.arr_type())
        
        return FieldAccess(obj, fieldName)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        name = Id(ctx.ID().getText())
        returnType = self.get_type(ctx.types().getText()) if ctx.types() else None
        methodReceiver = self.visit(ctx.method_para())
        param = [self.visit(para) for para in ctx.list_para()] if ctx.list_para() else []
        stmts = [self.visit(stmt) for stmt in ctx.block_statement()] if ctx.block_statement() else []
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)


    # Visit a parse tree produced by MiniGoParser#method_para.
    def visitMethod_para(self, ctx:MiniGoParser.Method_paraContext):
        name = Id(ctx.ID().getText())
        type = self.get_type(ctx.types().getText())
        varInit = None
        
        return VariablesDecl(name, type, varInit)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        name = Id(ctx.ID().getText())
        fields = [self.visit(field) for field in ctx.interface_method_list()] if ctx.interface_method_list() else []
        
        return InterfaceDecl(name, fields)


    # Visit a parse tree produced by MiniGoParser#interface_method_list.
    def visitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        if ctx.interface_method_list():
            return self.visit(ctx.interface_method()) + self.visit(ctx.interface_method_list())
        else: return self.visit(ctx.interface_method())


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name = Id(ctx.ID().getText())
        returnType = self.get_type(ctx.types().getText()) if ctx.types() else None
        methodReceiver = None
        param = [self.visit(para) for para in ctx.interface_para_list()] if ctx.interface_para_list() else []
        stmts = []
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)


    # Visit a parse tree produced by MiniGoParser#interface_para_list.
    def visitInterface_para_list(self, ctx:MiniGoParser.Interface_para_listContext):
        if ctx.interface_para_list():
            return self.visit(ctx.interface_para()) + self.visit(ctx.interface_para_list())
        else: return self.visit(ctx.interface_para())


    # Visit a parse tree produced by MiniGoParser#interface_para.
    def visitInterface_para(self, ctx:MiniGoParser.Interface_paraContext):
        if (ctx.ID()):
            name = Id(ctx.ID().getText())
            type = self.get_type(ctx.types().getText()) if ctx.types() else None
            varInit = None
            
            return VariablesDecl(name, type, varInit)       
        else: return VariablesDecl(None, None, None)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        name = Id(ctx.ID().getText())
        returnType = self.get_type(ctx.types().getText()) if ctx.types() else None
        methodReceiver = None
        param = [self.visit(para) for para in ctx.list_para()] if ctx.list_para() else []
        stmts = [self.visit(stmt) for stmt in ctx.block_statement()] if ctx.block_statement() else []
        
        return FunctionDecl(name, returnType, methodReceiver, param, stmts)


    # Visit a parse tree produced by MiniGoParser#list_para.
    def visitList_para(self, ctx:MiniGoParser.List_paraContext):
        if ctx.list_para():
            return self.visit(ctx.para()) + self.visit(ctx.list_para())
        else: return self.visit(ctx.para())


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        if (ctx.ID()):
            name = Id(ctx.ID().getText())
            type = self.get_type(ctx.types().getText()) if ctx.types() else None
            varInit = None
            
            return VariablesDecl(name, type, varInit)
        else: return VariablesDecl(None, None, None)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visit(ctx.list_statement()) if ctx.list_statement() else None


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return self.visit(ctx.statement()) + self.visit(ctx.list_statement())
        else: return self.visit(ctx.statement())


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
        rhs = self.visit(ctx.list_expr())
        assign = 


    # Visit a parse tree produced by MiniGoParser#lhs_list.
    def visitLhs_list(self, ctx:MiniGoParser.Lhs_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ass_operator.
    def visitAss_operator(self, ctx:MiniGoParser.Ass_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_else_if_statement.
    def visitList_else_if_statement(self, ctx:MiniGoParser.List_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for_statement.
    def visitInit_for_statement(self, ctx:MiniGoParser.Init_for_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value_assign.
    def visitValue_assign(self, ctx:MiniGoParser.Value_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#and_expr.
    def visitAnd_expr(self, ctx:MiniGoParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rela_expr.
    def visitRela_expr(self, ctx:MiniGoParser.Rela_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_expr.
    def visitAdd_expr(self, ctx:MiniGoParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_expr.
    def visitMul_expr(self, ctx:MiniGoParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_expr.
    def visitUnary_expr(self, ctx:MiniGoParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprd.
    def visitExprd(self, ctx:MiniGoParser.ExprdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_types.
    def visitPrimitive_types(self, ctx:MiniGoParser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#composite_types.
    def visitComposite_types(self, ctx:MiniGoParser.Composite_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_type.
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_operator.
    def visitIndex_operator(self, ctx:MiniGoParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field.
    def visitList_field(self, ctx:MiniGoParser.List_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_list.
    def visitArr_list(self, ctx:MiniGoParser.Arr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#float_lit.
    def visitFloat_lit(self, ctx:MiniGoParser.Float_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#str_lit.
    def visitStr_lit(self, ctx:MiniGoParser.Str_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#newline.
    def visitNewline(self, ctx:MiniGoParser.NewlineContext):
        return self.visitChildren(ctx)