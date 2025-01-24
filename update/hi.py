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
    #copy function target/main/MiniGoVisitor.py
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        decls = [self.visit(decl) for decl in ctx.declared()]
        return Program(decls)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        if ctx.variables_declared():
            return self.visit(ctx.variables_declared())
        elif ctx.constants_declared():
            return self.visit(ctx.constants_declared())
        elif ctx.function_declared():
            return self.visit(ctx.function_declared())
        elif ctx.method_declared():
            return self.visit(ctx.method_declared())
        elif ctx.struct_declared():
            return self.visit(ctx.struct_declared())
        else: return self.visit(ctx.interface_declared())
        


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        var_name = Id(ctx.ID(0).getText())
        var_type = None
        var_value = None
        
        if ctx.TYPE_LIT():
            type_text = ctx.TYPE_LIT().getText()
            var_type = self.get_type(type_text)
        
        if ctx.ASSIGN():
            var_value = self.visit(ctx.list_expression())
        
        return VariablesDecl(var_name, var_type, var_value)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        const_name = Id(ctx.ID(0).getText())
        # const_type = None
        const_value = None
        
        # if ctx.TYPE_LIT():
        #     type_text = ctx.TYPE_LIT().getText()
        #     var_type = self.get_type(type_text)
        
        if ctx.ASSIGN():
            var_value = self.visit(ctx.list_expression())
        
        return ConstDecl(Id(ctx.ID().getText()), var_value)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        func_name = ctx.ID().getText()
        return_type = None
        
        func_list_para = []
        if ctx.function_declared():
            func_list_para = self.visit(ctx.list_func())
        
        if ctx.TYPE_LIT():
            type_text = ctx.TYPE_LIT().getText()
            return_type = self.get_type(type_text)
        
        return FunctionDecl(func_name, return_type, var_value)


    # Visit a parse tree produced by MiniGoParser#list_func.
    def visitList_func(self, ctx:MiniGoParser.List_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method.
    def visitList_method(self, ctx:MiniGoParser.List_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_body.
    def visitStruct_body(self, ctx:MiniGoParser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_body.
    def visitInterface_body(self, ctx:MiniGoParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_element.
    def visitInterface_element(self, ctx:MiniGoParser.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_parameters.
    def visitList_parameters(self, ctx:MiniGoParser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_temp.
    def visitList_para_temp(self, ctx:MiniGoParser.List_para_tempContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_lhs.
    def visitList_lhs(self, ctx:MiniGoParser.List_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elif.
    def visitList_elif(self, ctx:MiniGoParser.List_elifContext):
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


    # Visit a parse tree produced by MiniGoParser#for_init.
    def visitFor_init(self, ctx:MiniGoParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update_expr.
    def visitUpdate_expr(self, ctx:MiniGoParser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.BOOLEAN_LIT():
            return BooleanLiteral(ctx.BOOLEAN_LIT().getText() == 'true')
        elif ctx.NIL():
            return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_elements.
    def visitArray_elements(self, ctx:MiniGoParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nested_array.
    def visitNested_array(self, ctx:MiniGoParser.Nested_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements.
    def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return [self.visit(expr) for expr in ctx.expression()]


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:  # Binary operators
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return BinaryOp(op, left, right)
        elif ctx.getChildCount() == 2:  # Unary operators
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expression(0))
            return UnaryOp(op, body)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expression.
    def visitPrimary_expression(self, ctx:MiniGoParser.Primary_expressionContext):
        return self.visitChildren(ctx)
    
    def get_type(self, type_text: str):
        type_map = {
            'int': IntType(),
            'float': FloatType(),
            'string': StringType(),
            'boolean': BooleanType()
        }
        return type_map.get(type_text, None)