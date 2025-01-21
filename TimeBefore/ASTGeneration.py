from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        if ctx.decllist():
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        return [self.visit(ctx.decl())]


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.func_decl():
            return self.visit(ctx.func_decl())
        return self.visit(ctx.variable_decl())


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.para_decl())
        body = None
        if ctx.block_statement():
            body = self.visit(ctx.block_statement())
        elif ctx.return_statement():
            body = self.visit(ctx.return_statement())
        
        return FuncDecl(name, param, body)


    # Visit a parse tree produced by ZCodeParser#para_decl.
    def visitPara_decl(self, ctx:ZCodeParser.Para_declContext):
        return self.visit(ctx.para_list())


    # Visit a parse tree produced by ZCodeParser#para_list.
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        return self.visit(ctx.para_prime()) if ctx.para_prime() else []


    # Visit a parse tree produced by ZCodeParser#para_prime.
    def visitPara_prime(self, ctx:ZCodeParser.Para_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.para_prime())


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        name = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.array_type().ID().getText())
        varType = self.visit(ctx.data_type()) if ctx.data_type() else self.visit(ctx.array_type())   
        
        return VarDecl(name, varType, None, None)


    # Visit a parse tree produced by ZCodeParser#variable_decl.
    def visitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        if ctx.var():
            return self.visit(ctx.var())
        elif ctx.var_implicit():
            return self.visit(ctx.var_implicit())
        elif ctx.dyn_implicit():
            return self.visit(ctx.dyn_implicit())


    # Visit a parse tree produced by ZCodeParser#var.
    def visitVar(self, ctx:ZCodeParser.VarContext):
        name = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.array_type().ID().getText())
        varType = self.visit(ctx.data_type()) if ctx.data_type() else self.visit(ctx.array_type())
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        
        return VarDecl(name, varType, None, varInit)


    # Visit a parse tree produced by ZCodeParser#var_implicit.
    def visitVar_implicit(self, ctx:ZCodeParser.Var_implicitContext):
        name = Id(ctx.ID().getText())
        modifier = ctx.vartype().getText()
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        
        return VarDecl(name, None, modifier, varInit)


    # Visit a parse tree produced by ZCodeParser#dyn_implicit.
    def visitDyn_implicit(self, ctx:ZCodeParser.Dyn_implicitContext):
        name = Id(ctx.ID().getText())
        modifier = ctx.dyntype().getText()
        varInit = self.visit(ctx.expr()) if ctx.expr() else None

        return VarDecl(name, None, modifier, varInit)

    # Visit a parse tree produced by ZCodeParser#statementlist.
    def visitStatementlist(self, ctx:ZCodeParser.StatementlistContext):
        if ctx.statementlist():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementlist())
        return []


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#decl_statement.
    def visitDecl_statement(self, ctx:ZCodeParser.Decl_statementContext):
        return self.visit(ctx.variable_decl())


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statementlist()))


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.expr())
        
        return Assign(lhs, exp)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.index_operator():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operator()))
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.statement()) if ctx.statement() else self.visit(ctx.block_statement())
        elifStmt = self.visit(ctx.elif_statement()) if ctx.elif_statement() else []
        elseStmt = self.visit(ctx.else_statement()) 

        return If(expr, thenStmt, elifStmt, elseStmt)
        
    # Visit a parse tree produced by ZCodeParser#else_statement.
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        stmt = None
        if ctx.block_statement():
            stmt = self.visit(ctx.block_statement())
        elif ctx.statement():
            stmt = self.visit(ctx.statement())
            
        if ctx.elseword():
            return stmt
        else:
            return None
        
    # Visit a parse tree produced by ZCodeParser#elif_statement.
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        stmt = None
        if ctx.block_statement():
            stmt = self.visit(ctx.block_statement())
        elif ctx.statement():
            stmt = self.visit(ctx.statement())
        
        if ctx.elif_statement():
            return [(self.visit(ctx.expr()), stmt)] + self.visit(ctx.elif_statement())  
        else:
            return []


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        name = Id(ctx.ID().getText())
        condExpr = self.visit(ctx.expr()[0])
        updExpr = self.visit(ctx.expr()[1])
        body = self.visit(ctx.statement()) if ctx.statement() else self.visit(ctx.block_statement())
        
        return For(name, condExpr, updExpr, body)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None   
        return Return(expr)


    # Visit a parse tree produced by ZCodeParser#funcCall_statement.
    def visitFuncCall_statement(self, ctx:ZCodeParser.FuncCall_statementContext):
        name = Id(ctx.ID().getText())
        args = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        
        return CallStmt(name, args)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#relation_expr.
    def visitRelation_expr(self, ctx:ZCodeParser.Relation_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#andOr_expr.
    def visitAndOr_expr(self, ctx:ZCodeParser.AndOr_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#add_expr.
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#mul_expr.
    def visitMul_expr(self, ctx:ZCodeParser.Mul_exprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#not_expr.
    def visitNot_expr(self, ctx:ZCodeParser.Not_exprContext):
        if ctx.getChildCount() > 1:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#sub_expr.
    def visitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        if ctx.getChildCount() > 1:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else: 
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#element_expr.
    def visitElement_expr(self, ctx:ZCodeParser.Element_exprContext):
        if ctx.array_element():
            return self.visit(ctx.array_element())
        return self.visit(ctx.func_expr())


    # Visit a parse tree produced by ZCodeParser#func_expr.
    def visitFunc_expr(self, ctx:ZCodeParser.Func_exprContext):
        if ctx.funcCall():
            return self.visit(ctx.funcCall())
        return self.visit(ctx.exprd())


    # Visit a parse tree produced by ZCodeParser#exprd.
    def visitExprd(self, ctx:ZCodeParser.ExprdContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.data_value():
            return self.visit(ctx.data_value())
        else: 
            return Id(ctx.ID().getText())


    # Visit a parse tree produced by ZCodeParser#funcCall.
    def visitFuncCall(self, ctx:ZCodeParser.FuncCallContext):
        name = Id(ctx.ID().getText())
        args = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        
        return CallExpr(name, args)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        if ctx.index_operator():
            return self.visit(ctx.expr_list()) + self.visit(ctx.index_operator())
        return self.visit(ctx.expr_list())


    # Visit a parse tree produced by ZCodeParser#array_element.
    def visitArray_element(self, ctx:ZCodeParser.Array_elementContext):
        arr = self.visit(ctx.func_expr())
        idx = self.visit(ctx.index_operator())
        return ArrayCell(arr, idx)


    # Visit a parse tree produced by ZCodeParser#data_value.
    def visitData_value(self, ctx:ZCodeParser.Data_valueContext):
        if ctx.numberliteral():
            return self.visit(ctx.numberliteral())
        elif ctx.boolliteral():
            return self.visit(ctx.boolliteral())
        elif ctx.strliteral():
            return self.visit(ctx.strliteral())
        return self.visit(ctx.array_value())


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return ArrayLiteral(self.visit(ctx.arr_list()))


    # Visit a parse tree produced by ZCodeParser#arr_list.
    def visitArr_list(self, ctx:ZCodeParser.Arr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.data_value())]
        return [self.visit(ctx.data_value())] + self.visit(ctx.arr_list())


    # Visit a parse tree produced by ZCodeParser#data_type.
    def visitData_type(self, ctx:ZCodeParser.Data_typeContext):
        if ctx.numtype():
            return NumberType()
        elif ctx.booltype():
            return BoolType()
        elif ctx.stringtype():
            return StringType()


        # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        size = self.visit(ctx.numlist())
        varType = self.visit(ctx.data_type())
        
        return ArrayType(size, varType)
    
    
        # Visit a parse tree produced by ZCodeParser#numlist.
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUM_LIT().getText())]
        return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.numlist())
    
    
    # Visit a parse tree produced by ZCodeParser#numberliteral.
    def visitNumberliteral(self, ctx:ZCodeParser.NumberliteralContext):
        return NumberLiteral(float(ctx.NUM_LIT().getText()))


    # Visit a parse tree produced by ZCodeParser#boolliteral.
    def visitBoolliteral(self, ctx:ZCodeParser.BoolliteralContext):
        if ctx.FALSE():
            return BooleanLiteral(False)
        else:
            return BooleanLiteral(True)
        


    # Visit a parse tree produced by ZCodeParser#strliteral.
    def visitStrliteral(self, ctx:ZCodeParser.StrliteralContext):
        return StringLiteral(ctx.STR_LIT().getText())
    
    # Visit a parse tree produced by ZCodeParser#newline.
    def visitNewline(self, ctx:ZCodeParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numtype.
    def visitNumtype(self, ctx:ZCodeParser.NumtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#booltype.
    def visitBooltype(self, ctx:ZCodeParser.BooltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringtype.
    def visitStringtype(self, ctx:ZCodeParser.StringtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnn.
    def visitReturnn(self, ctx:ZCodeParser.ReturnnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vartype.
    def visitVartype(self, ctx:ZCodeParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dyntype.
    def visitDyntype(self, ctx:ZCodeParser.DyntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forword.
    def visitForword(self, ctx:ZCodeParser.ForwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#unitlword.
    def visitUnitlword(self, ctx:ZCodeParser.UnitlwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#byword.
    def visitByword(self, ctx:ZCodeParser.BywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakword.
    def visitBreakword(self, ctx:ZCodeParser.BreakwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continueword.
    def visitContinueword(self, ctx:ZCodeParser.ContinuewordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifword.
    def visitIfword(self, ctx:ZCodeParser.IfwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseword.
    def visitElseword(self, ctx:ZCodeParser.ElsewordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifword.
    def visitElifword(self, ctx:ZCodeParser.ElifwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#beginn.
    def visitBeginn(self, ctx:ZCodeParser.BeginnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#endd.
    def visitEndd(self, ctx:ZCodeParser.EnddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#notword.
    def visitNotword(self, ctx:ZCodeParser.NotwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#andword.
    def visitAndword(self, ctx:ZCodeParser.AndwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#orword.
    def visitOrword(self, ctx:ZCodeParser.OrwordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#addd.
    def visitAddd(self, ctx:ZCodeParser.AdddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subb.
    def visitSubb(self, ctx:ZCodeParser.SubbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mull.
    def visitMull(self, ctx:ZCodeParser.MullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#divv.
    def visitDivv(self, ctx:ZCodeParser.DivvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#modd.
    def visitModd(self, ctx:ZCodeParser.ModdContext):
        return self.visitChildren(ctx)
