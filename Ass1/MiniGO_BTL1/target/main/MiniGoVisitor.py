# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decllist.
    def visitDecllist(self, ctx:MiniGoParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_decl.
    def visitVariable_decl(self, ctx:MiniGoParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_fields.
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
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


    # Visit a parse tree produced by MiniGoParser#func_expr.
    def visitFunc_expr(self, ctx:MiniGoParser.Func_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_operator.
    def visitIndex_operator(self, ctx:MiniGoParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#args.
    def visitArgs(self, ctx:MiniGoParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
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


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_type.
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_dim.
    def visitArr_dim(self, ctx:MiniGoParser.Arr_dimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_list.
    def visitLiteral_list(self, ctx:MiniGoParser.Literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
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


    # Visit a parse tree produced by MiniGoParser#nil_lit.
    def visitNil_lit(self, ctx:MiniGoParser.Nil_litContext):
        return self.visitChildren(ctx)



del MiniGoParser