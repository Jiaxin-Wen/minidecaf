# Generated from minidecaf/Decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#prog.
    def enterProg(self, ctx:DecafParser.ProgContext):
        pass

    # Exit a parse tree produced by DecafParser#prog.
    def exitProg(self, ctx:DecafParser.ProgContext):
        pass


    # Enter a parse tree produced by DecafParser#progFunc.
    def enterProgFunc(self, ctx:DecafParser.ProgFuncContext):
        pass

    # Exit a parse tree produced by DecafParser#progFunc.
    def exitProgFunc(self, ctx:DecafParser.ProgFuncContext):
        pass


    # Enter a parse tree produced by DecafParser#progDeclaration.
    def enterProgDeclaration(self, ctx:DecafParser.ProgDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#progDeclaration.
    def exitProgDeclaration(self, ctx:DecafParser.ProgDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#funcDefinition.
    def enterFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        pass

    # Exit a parse tree produced by DecafParser#funcDefinition.
    def exitFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        pass


    # Enter a parse tree produced by DecafParser#funcDeclaration.
    def enterFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#funcDeclaration.
    def exitFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#parameterList.
    def enterParameterList(self, ctx:DecafParser.ParameterListContext):
        pass

    # Exit a parse tree produced by DecafParser#parameterList.
    def exitParameterList(self, ctx:DecafParser.ParameterListContext):
        pass


    # Enter a parse tree produced by DecafParser#ptrType.
    def enterPtrType(self, ctx:DecafParser.PtrTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#ptrType.
    def exitPtrType(self, ctx:DecafParser.PtrTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#intType.
    def enterIntType(self, ctx:DecafParser.IntTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#intType.
    def exitIntType(self, ctx:DecafParser.IntTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#blockItemStat.
    def enterBlockItemStat(self, ctx:DecafParser.BlockItemStatContext):
        pass

    # Exit a parse tree produced by DecafParser#blockItemStat.
    def exitBlockItemStat(self, ctx:DecafParser.BlockItemStatContext):
        pass


    # Enter a parse tree produced by DecafParser#blockItemDecl.
    def enterBlockItemDecl(self, ctx:DecafParser.BlockItemDeclContext):
        pass

    # Exit a parse tree produced by DecafParser#blockItemDecl.
    def exitBlockItemDecl(self, ctx:DecafParser.BlockItemDeclContext):
        pass


    # Enter a parse tree produced by DecafParser#returnStat.
    def enterReturnStat(self, ctx:DecafParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by DecafParser#returnStat.
    def exitReturnStat(self, ctx:DecafParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by DecafParser#exprStat.
    def enterExprStat(self, ctx:DecafParser.ExprStatContext):
        pass

    # Exit a parse tree produced by DecafParser#exprStat.
    def exitExprStat(self, ctx:DecafParser.ExprStatContext):
        pass


    # Enter a parse tree produced by DecafParser#ifStat.
    def enterIfStat(self, ctx:DecafParser.IfStatContext):
        pass

    # Exit a parse tree produced by DecafParser#ifStat.
    def exitIfStat(self, ctx:DecafParser.IfStatContext):
        pass


    # Enter a parse tree produced by DecafParser#blockStat.
    def enterBlockStat(self, ctx:DecafParser.BlockStatContext):
        pass

    # Exit a parse tree produced by DecafParser#blockStat.
    def exitBlockStat(self, ctx:DecafParser.BlockStatContext):
        pass


    # Enter a parse tree produced by DecafParser#forDeclStat.
    def enterForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        pass

    # Exit a parse tree produced by DecafParser#forDeclStat.
    def exitForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        pass


    # Enter a parse tree produced by DecafParser#forStat.
    def enterForStat(self, ctx:DecafParser.ForStatContext):
        pass

    # Exit a parse tree produced by DecafParser#forStat.
    def exitForStat(self, ctx:DecafParser.ForStatContext):
        pass


    # Enter a parse tree produced by DecafParser#whileStat.
    def enterWhileStat(self, ctx:DecafParser.WhileStatContext):
        pass

    # Exit a parse tree produced by DecafParser#whileStat.
    def exitWhileStat(self, ctx:DecafParser.WhileStatContext):
        pass


    # Enter a parse tree produced by DecafParser#doWhileStat.
    def enterDoWhileStat(self, ctx:DecafParser.DoWhileStatContext):
        pass

    # Exit a parse tree produced by DecafParser#doWhileStat.
    def exitDoWhileStat(self, ctx:DecafParser.DoWhileStatContext):
        pass


    # Enter a parse tree produced by DecafParser#breakStat.
    def enterBreakStat(self, ctx:DecafParser.BreakStatContext):
        pass

    # Exit a parse tree produced by DecafParser#breakStat.
    def exitBreakStat(self, ctx:DecafParser.BreakStatContext):
        pass


    # Enter a parse tree produced by DecafParser#continueStat.
    def enterContinueStat(self, ctx:DecafParser.ContinueStatContext):
        pass

    # Exit a parse tree produced by DecafParser#continueStat.
    def exitContinueStat(self, ctx:DecafParser.ContinueStatContext):
        pass


    # Enter a parse tree produced by DecafParser#emptyStat.
    def enterEmptyStat(self, ctx:DecafParser.EmptyStatContext):
        pass

    # Exit a parse tree produced by DecafParser#emptyStat.
    def exitEmptyStat(self, ctx:DecafParser.EmptyStatContext):
        pass


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#expr.
    def enterExpr(self, ctx:DecafParser.ExprContext):
        pass

    # Exit a parse tree produced by DecafParser#expr.
    def exitExpr(self, ctx:DecafParser.ExprContext):
        pass


    # Enter a parse tree produced by DecafParser#tAssign.
    def enterTAssign(self, ctx:DecafParser.TAssignContext):
        pass

    # Exit a parse tree produced by DecafParser#tAssign.
    def exitTAssign(self, ctx:DecafParser.TAssignContext):
        pass


    # Enter a parse tree produced by DecafParser#cAssign.
    def enterCAssign(self, ctx:DecafParser.CAssignContext):
        pass

    # Exit a parse tree produced by DecafParser#cAssign.
    def exitCAssign(self, ctx:DecafParser.CAssignContext):
        pass


    # Enter a parse tree produced by DecafParser#tConditional.
    def enterTConditional(self, ctx:DecafParser.TConditionalContext):
        pass

    # Exit a parse tree produced by DecafParser#tConditional.
    def exitTConditional(self, ctx:DecafParser.TConditionalContext):
        pass


    # Enter a parse tree produced by DecafParser#cConditional.
    def enterCConditional(self, ctx:DecafParser.CConditionalContext):
        pass

    # Exit a parse tree produced by DecafParser#cConditional.
    def exitCConditional(self, ctx:DecafParser.CConditionalContext):
        pass


    # Enter a parse tree produced by DecafParser#tLogicOr.
    def enterTLogicOr(self, ctx:DecafParser.TLogicOrContext):
        pass

    # Exit a parse tree produced by DecafParser#tLogicOr.
    def exitTLogicOr(self, ctx:DecafParser.TLogicOrContext):
        pass


    # Enter a parse tree produced by DecafParser#cLogicOr.
    def enterCLogicOr(self, ctx:DecafParser.CLogicOrContext):
        pass

    # Exit a parse tree produced by DecafParser#cLogicOr.
    def exitCLogicOr(self, ctx:DecafParser.CLogicOrContext):
        pass


    # Enter a parse tree produced by DecafParser#cLogicAnd.
    def enterCLogicAnd(self, ctx:DecafParser.CLogicAndContext):
        pass

    # Exit a parse tree produced by DecafParser#cLogicAnd.
    def exitCLogicAnd(self, ctx:DecafParser.CLogicAndContext):
        pass


    # Enter a parse tree produced by DecafParser#tLogicAnd.
    def enterTLogicAnd(self, ctx:DecafParser.TLogicAndContext):
        pass

    # Exit a parse tree produced by DecafParser#tLogicAnd.
    def exitTLogicAnd(self, ctx:DecafParser.TLogicAndContext):
        pass


    # Enter a parse tree produced by DecafParser#cEqual.
    def enterCEqual(self, ctx:DecafParser.CEqualContext):
        pass

    # Exit a parse tree produced by DecafParser#cEqual.
    def exitCEqual(self, ctx:DecafParser.CEqualContext):
        pass


    # Enter a parse tree produced by DecafParser#tEqual.
    def enterTEqual(self, ctx:DecafParser.TEqualContext):
        pass

    # Exit a parse tree produced by DecafParser#tEqual.
    def exitTEqual(self, ctx:DecafParser.TEqualContext):
        pass


    # Enter a parse tree produced by DecafParser#tRelation.
    def enterTRelation(self, ctx:DecafParser.TRelationContext):
        pass

    # Exit a parse tree produced by DecafParser#tRelation.
    def exitTRelation(self, ctx:DecafParser.TRelationContext):
        pass


    # Enter a parse tree produced by DecafParser#cRelation.
    def enterCRelation(self, ctx:DecafParser.CRelationContext):
        pass

    # Exit a parse tree produced by DecafParser#cRelation.
    def exitCRelation(self, ctx:DecafParser.CRelationContext):
        pass


    # Enter a parse tree produced by DecafParser#cAdd.
    def enterCAdd(self, ctx:DecafParser.CAddContext):
        pass

    # Exit a parse tree produced by DecafParser#cAdd.
    def exitCAdd(self, ctx:DecafParser.CAddContext):
        pass


    # Enter a parse tree produced by DecafParser#tAdd.
    def enterTAdd(self, ctx:DecafParser.TAddContext):
        pass

    # Exit a parse tree produced by DecafParser#tAdd.
    def exitTAdd(self, ctx:DecafParser.TAddContext):
        pass


    # Enter a parse tree produced by DecafParser#tMul.
    def enterTMul(self, ctx:DecafParser.TMulContext):
        pass

    # Exit a parse tree produced by DecafParser#tMul.
    def exitTMul(self, ctx:DecafParser.TMulContext):
        pass


    # Enter a parse tree produced by DecafParser#cMul.
    def enterCMul(self, ctx:DecafParser.CMulContext):
        pass

    # Exit a parse tree produced by DecafParser#cMul.
    def exitCMul(self, ctx:DecafParser.CMulContext):
        pass


    # Enter a parse tree produced by DecafParser#tCast.
    def enterTCast(self, ctx:DecafParser.TCastContext):
        pass

    # Exit a parse tree produced by DecafParser#tCast.
    def exitTCast(self, ctx:DecafParser.TCastContext):
        pass


    # Enter a parse tree produced by DecafParser#cCast.
    def enterCCast(self, ctx:DecafParser.CCastContext):
        pass

    # Exit a parse tree produced by DecafParser#cCast.
    def exitCCast(self, ctx:DecafParser.CCastContext):
        pass


    # Enter a parse tree produced by DecafParser#tUnary.
    def enterTUnary(self, ctx:DecafParser.TUnaryContext):
        pass

    # Exit a parse tree produced by DecafParser#tUnary.
    def exitTUnary(self, ctx:DecafParser.TUnaryContext):
        pass


    # Enter a parse tree produced by DecafParser#cUnary.
    def enterCUnary(self, ctx:DecafParser.CUnaryContext):
        pass

    # Exit a parse tree produced by DecafParser#cUnary.
    def exitCUnary(self, ctx:DecafParser.CUnaryContext):
        pass


    # Enter a parse tree produced by DecafParser#postfixArray.
    def enterPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        pass

    # Exit a parse tree produced by DecafParser#postfixArray.
    def exitPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        pass


    # Enter a parse tree produced by DecafParser#postfixCall.
    def enterPostfixCall(self, ctx:DecafParser.PostfixCallContext):
        pass

    # Exit a parse tree produced by DecafParser#postfixCall.
    def exitPostfixCall(self, ctx:DecafParser.PostfixCallContext):
        pass


    # Enter a parse tree produced by DecafParser#tPostfix.
    def enterTPostfix(self, ctx:DecafParser.TPostfixContext):
        pass

    # Exit a parse tree produced by DecafParser#tPostfix.
    def exitTPostfix(self, ctx:DecafParser.TPostfixContext):
        pass


    # Enter a parse tree produced by DecafParser#argList.
    def enterArgList(self, ctx:DecafParser.ArgListContext):
        pass

    # Exit a parse tree produced by DecafParser#argList.
    def exitArgList(self, ctx:DecafParser.ArgListContext):
        pass


    # Enter a parse tree produced by DecafParser#atomInteger.
    def enterAtomInteger(self, ctx:DecafParser.AtomIntegerContext):
        pass

    # Exit a parse tree produced by DecafParser#atomInteger.
    def exitAtomInteger(self, ctx:DecafParser.AtomIntegerContext):
        pass


    # Enter a parse tree produced by DecafParser#atomExpr.
    def enterAtomExpr(self, ctx:DecafParser.AtomExprContext):
        pass

    # Exit a parse tree produced by DecafParser#atomExpr.
    def exitAtomExpr(self, ctx:DecafParser.AtomExprContext):
        pass


    # Enter a parse tree produced by DecafParser#atomIdent.
    def enterAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        pass

    # Exit a parse tree produced by DecafParser#atomIdent.
    def exitAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        pass


    # Enter a parse tree produced by DecafParser#unaryOp.
    def enterUnaryOp(self, ctx:DecafParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by DecafParser#unaryOp.
    def exitUnaryOp(self, ctx:DecafParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by DecafParser#addOp.
    def enterAddOp(self, ctx:DecafParser.AddOpContext):
        pass

    # Exit a parse tree produced by DecafParser#addOp.
    def exitAddOp(self, ctx:DecafParser.AddOpContext):
        pass


    # Enter a parse tree produced by DecafParser#mulOp.
    def enterMulOp(self, ctx:DecafParser.MulOpContext):
        pass

    # Exit a parse tree produced by DecafParser#mulOp.
    def exitMulOp(self, ctx:DecafParser.MulOpContext):
        pass


    # Enter a parse tree produced by DecafParser#relationOp.
    def enterRelationOp(self, ctx:DecafParser.RelationOpContext):
        pass

    # Exit a parse tree produced by DecafParser#relationOp.
    def exitRelationOp(self, ctx:DecafParser.RelationOpContext):
        pass


    # Enter a parse tree produced by DecafParser#equalOp.
    def enterEqualOp(self, ctx:DecafParser.EqualOpContext):
        pass

    # Exit a parse tree produced by DecafParser#equalOp.
    def exitEqualOp(self, ctx:DecafParser.EqualOpContext):
        pass


    # Enter a parse tree produced by DecafParser#andOp.
    def enterAndOp(self, ctx:DecafParser.AndOpContext):
        pass

    # Exit a parse tree produced by DecafParser#andOp.
    def exitAndOp(self, ctx:DecafParser.AndOpContext):
        pass


    # Enter a parse tree produced by DecafParser#orOp.
    def enterOrOp(self, ctx:DecafParser.OrOpContext):
        pass

    # Exit a parse tree produced by DecafParser#orOp.
    def exitOrOp(self, ctx:DecafParser.OrOpContext):
        pass


    # Enter a parse tree produced by DecafParser#assignOP.
    def enterAssignOP(self, ctx:DecafParser.AssignOPContext):
        pass

    # Exit a parse tree produced by DecafParser#assignOP.
    def exitAssignOP(self, ctx:DecafParser.AssignOPContext):
        pass



del DecafParser