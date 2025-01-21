# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_decl.
    def visitList_decl(self, ctx:ZCodeParser.List_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_vardecl.
    def visitList_vardecl(self, ctx:ZCodeParser.List_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#imp_var.
    def visitImp_var(self, ctx:ZCodeParser.Imp_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vartype.
    def visitVartype(self, ctx:ZCodeParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyw_var.
    def visitKeyw_var(self, ctx:ZCodeParser.Keyw_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_keyw_var.
    def visitArr_keyw_var(self, ctx:ZCodeParser.Arr_keyw_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dyna_var.
    def visitDyna_var(self, ctx:ZCodeParser.Dyna_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_prameters.
    def visitList_prameters(self, ctx:ZCodeParser.List_prametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_NUMBERLIT.
    def visitList_NUMBERLIT(self, ctx:ZCodeParser.List_NUMBERLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr.
    def visitLogical_expr(self, ctx:ZCodeParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_expr.
    def visitAdding_expr(self, ctx:ZCodeParser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:ZCodeParser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_expr.
    def visitNot_expr(self, ctx:ZCodeParser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexoper_expr.
    def visitIndexoper_expr(self, ctx:ZCodeParser.Indexoper_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#final_expr.
    def visitFinal_expr(self, ctx:ZCodeParser.Final_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_index_operators.
    def visitList_index_operators(self, ctx:ZCodeParser.List_index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_expression.
    def visitList_expression(self, ctx:ZCodeParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_stmt.
    def visitDecl_stmt(self, ctx:ZCodeParser.Decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass_stmt.
    def visitAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_stmt.
    def visitList_stmt(self, ctx:ZCodeParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser