# Generated from minidecaf/Decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete generic visitor for a parse tree produced by DecafParser.

class DecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafParser#prog.
    def visitProg(self, ctx:DecafParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#progFunc.
    def visitProgFunc(self, ctx:DecafParser.ProgFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#progDeclaration.
    def visitProgDeclaration(self, ctx:DecafParser.ProgDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#funcDefinition.
    def visitFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parameterList.
    def visitParameterList(self, ctx:DecafParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ptrType.
    def visitPtrType(self, ctx:DecafParser.PtrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#intType.
    def visitIntType(self, ctx:DecafParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#blockItemStat.
    def visitBlockItemStat(self, ctx:DecafParser.BlockItemStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#blockItemDecl.
    def visitBlockItemDecl(self, ctx:DecafParser.BlockItemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#returnStat.
    def visitReturnStat(self, ctx:DecafParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#exprStat.
    def visitExprStat(self, ctx:DecafParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ifStat.
    def visitIfStat(self, ctx:DecafParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#blockStat.
    def visitBlockStat(self, ctx:DecafParser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#forDeclStat.
    def visitForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#forStat.
    def visitForStat(self, ctx:DecafParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#whileStat.
    def visitWhileStat(self, ctx:DecafParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#doWhileStat.
    def visitDoWhileStat(self, ctx:DecafParser.DoWhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#breakStat.
    def visitBreakStat(self, ctx:DecafParser.BreakStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#continueStat.
    def visitContinueStat(self, ctx:DecafParser.ContinueStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#emptyStat.
    def visitEmptyStat(self, ctx:DecafParser.EmptyStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#declaration.
    def visitDeclaration(self, ctx:DecafParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx:DecafParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tAssign.
    def visitTAssign(self, ctx:DecafParser.TAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cAssign.
    def visitCAssign(self, ctx:DecafParser.CAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tConditional.
    def visitTConditional(self, ctx:DecafParser.TConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cConditional.
    def visitCConditional(self, ctx:DecafParser.CConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tLogicOr.
    def visitTLogicOr(self, ctx:DecafParser.TLogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cLogicOr.
    def visitCLogicOr(self, ctx:DecafParser.CLogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cLogicAnd.
    def visitCLogicAnd(self, ctx:DecafParser.CLogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tLogicAnd.
    def visitTLogicAnd(self, ctx:DecafParser.TLogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cEqual.
    def visitCEqual(self, ctx:DecafParser.CEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tEqual.
    def visitTEqual(self, ctx:DecafParser.TEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tRelation.
    def visitTRelation(self, ctx:DecafParser.TRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cRelation.
    def visitCRelation(self, ctx:DecafParser.CRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cAdd.
    def visitCAdd(self, ctx:DecafParser.CAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tAdd.
    def visitTAdd(self, ctx:DecafParser.TAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tMul.
    def visitTMul(self, ctx:DecafParser.TMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cMul.
    def visitCMul(self, ctx:DecafParser.CMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tCast.
    def visitTCast(self, ctx:DecafParser.TCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cCast.
    def visitCCast(self, ctx:DecafParser.CCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tUnary.
    def visitTUnary(self, ctx:DecafParser.TUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cUnary.
    def visitCUnary(self, ctx:DecafParser.CUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#postfixArray.
    def visitPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#postfixCall.
    def visitPostfixCall(self, ctx:DecafParser.PostfixCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#tPostfix.
    def visitTPostfix(self, ctx:DecafParser.TPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#argList.
    def visitArgList(self, ctx:DecafParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#atomInteger.
    def visitAtomInteger(self, ctx:DecafParser.AtomIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#atomExpr.
    def visitAtomExpr(self, ctx:DecafParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#atomIdent.
    def visitAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#unaryOp.
    def visitUnaryOp(self, ctx:DecafParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#addOp.
    def visitAddOp(self, ctx:DecafParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#mulOp.
    def visitMulOp(self, ctx:DecafParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#relationOp.
    def visitRelationOp(self, ctx:DecafParser.RelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#equalOp.
    def visitEqualOp(self, ctx:DecafParser.EqualOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#andOp.
    def visitAndOp(self, ctx:DecafParser.AndOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#orOp.
    def visitOrOp(self, ctx:DecafParser.OrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#assignOP.
    def visitAssignOP(self, ctx:DecafParser.AssignOPContext):
        return self.visitChildren(ctx)



del DecafParser