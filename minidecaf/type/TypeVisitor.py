from ..DecafVisitor import DecafVisitor
from ..DecafParser import DecafParser
from ..name.NameManager import NameInfo
from .TypeManager import *
from .Types import *
from .TypeRules import *
from ..utils import *
from ..ir.IRInstruction import *


def saveType(getType):
    def wrapper(self, ctx):
        ty = getType(self, ctx)
        self.manager.bindNodeType(ctx, ty)
        return ty
    return wrapper

class LvalueManager(DecafVisitor):
    def __init__(self, nameInfo:NameInfo, typeInfo:TypeInfo):
        self.nameInfo = nameInfo
        self.typeInfo = typeInfo
        self.func = None
    
    '''左值分析
    之前我们是在IRGenVisitor的visitCAssign函数中处理了5.5
    现在统一到类型检查中做左值分析，并记录左值．到IRGenVisitor中直接使用

    5.5 : 被声明过的变量是左值 -> visitAtomIdent
              如果e是左值, 那么(e)是左值 -> visitAtomExpr

    11.1: 如果e是类型为T*的表达式，那么*e是类型为T的左值 -> visitCUnary
    可以是一个带有Ident的表达式, 比如a+1

    12.9:
    　被声明过的变量 && 不是数组 是左值 -> visitAtomIdent加判断
        下标运算的结果　如果类型不是数组　则是左值 -> visitPostfixArray

    参考代码里左值分析实现的有些分散
    比如数组12.9的规定，在rule里实现了.
    我统一到左值分析里实现
    '''

    def checkLvalue(self, func, ctx):
        '''result是一个list或是None
        '''
        self.func = func
        result = ctx.accept(self) #即调用对这个ctx的visit函数 先viist了children, 记录了typeInfo, 供LvalueManager使用
        #print('in checkLvalue, func = {}, ctx = {}, ctxText = {}, result = {}'.format(func, type(ctx), ctx.getText(), result))
        if result is None:
            raise DecafException(f"lvalue expected in func: {func}")
        else:
            return result
    
    def visitPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        '''postfix是array
        expr是id
        系数应该是元素的size
        '''
        baseType = self.typeInfo.node2type[ctx.postfix()].baseType
        if not isinstance(baseType, Array): #限制baseType不可以是array
            size = baseType.size
            return [ctx.postfix(), ctx.expr(), Const(size), Binary('*'), Binary('+')]
        
    def visitCUnary(self, ctx:DecafParser.CUnaryContext):
        '''unary只有一种可能是左值
        '''
        if ctx.unaryOp().getText() == '*':
            return [ctx.cast()]
        #else就return none
    
    def visitAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        '''是左值, 直接返回ir指令
        '''
        node = ctx.Ident()
        var = self.nameInfo.node2var[node]
        ty = self.typeInfo.node2type[ctx]
        if not isinstance(ty, Array):#限制不是数组  不对.. 可以是int[1]
            if var.offset is None:
                return [GlobalAddr(var.ident)]
            else: 
                return [FrameAddr(var.offset)]
    
    def visitAtomExpr(self, ctx:DecafParser.AtomExprContext):
        return ctx.expr().accept(self) 

class TypeVisitor(DecafVisitor):
    '''类型检查
    我们还是可以使用一个 AST Visitor 实现类型检查，在其中
    
    对于每个操作结点，先对所有子结点类型检查，完成后子结点的 type 就是源操作数的类型。 
    然后对照这个操作的类型规则，如果源操作数类型不对那么报错，否则计算该结点的 type。
    
    碰到变量声明（包括形参），遍历声明类型子节点，然后设置其变量数据结构的类型。 
    如果有初始值，对它执行类型检查，如果它的类型和声明的类型不匹配则报错。
    '''
    '''
    类型检查阶段
    1. 建立了node -> type的映射
    2. 解析了函数的信息(主要是参数个数，用于后续的asm生成)

    在decl阶段确定
    '''
    def __init__(self, nameInfo:NameInfo, typeManager:TypeManager):
        self.nameInfo = nameInfo
        '''
        node -> var -> type
        不过为什么不能直接node -> type呢..
        '''
        self.manager = typeManager
        self.lvalueManager= LvalueManager(nameInfo, self.manager.typeInfo)
        self.var2type = {} # 记录Variable ->  Type 辅助node -> Type的记录

    def node2var(self, node):
        return self.nameInfo.node2var[node]
    
    def ident2globl(self, ident):
        return self.nameInfo.globlDict[ident]

    def checkLvalue(self, ctx):
        result = self.lvalueManager.checkLvalue(self.manager.curFunc, ctx)
        self.manager.bindLvalue(ctx, result)
    
    def getDeclType(self, ctx:DecafParser.DeclarationContext):
        '''引入数组后, 需要判断一下实际的类型
        '''
        ty = ctx.ty().accept(self)
        dimenSizeList = [int(dimenSize.getText()) for dimenSize in ctx.Integer()]
        if dimenSizeList == []: #普通变量
            return ty
        else:
            return Array.inflatten(ty, dimenSizeList)


    def visitChildren(self, ctx):
        ty = DecafVisitor.visitChildren(self, ctx)
        #print("ctx = {} : {}, visitChilren ty = {}".format(type(ctx), ctx.getText(), ty))
        self.manager.bindNodeType(ctx, ty)
        return ty #返回类型

    '''int / ptr / ident 作为叶节点　需要返回Type
    '''
    def visitPtrType(self, ctx:DecafParser.PtrTypeContext):
        baseType = ctx.ty().accept(self)
        return Ptr(baseType)
    
    def visitIntType(self, ctx:DecafParser.IntTypeContext):
        return Int()
    
    def visitDeclaration(self, ctx:DecafParser.DeclarationContext):
        node = ctx.Ident()
        var = self.node2var(node=node)
        ty = self.getDeclType(ctx)
        self.var2type[var] = ty #记录 到visitAtomIdent中使用
        #要检查赋值语句的类型
        if ctx.expr() != None:
            exprTy = ctx.expr().accept(self)
            assignRule(ty, exprTy)#检查赋值的类型
    
    @saveType
    def visitAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        '''记录node->type
        通过node->var->type
        '''
        # print('='*50)
        # print('enter visitAtomIdent')
        node = ctx.Ident()
        var = self.node2var(node)
        # print('in visitAtomIdent, var = {}, id = {}'.format(var, id(var)))
        # print('self.var2type = ')
        # for i, ty in self.var2type.items():
        #     print("var = {}, id = {}, ty = {}".format(i, id(i), ty))
        # print('='*50)
        return self.var2type[var] #返回类型，留给装饰器保存
    
    @saveType
    def visitAtomInteger(self, ctx:DecafParser.AtomIntegerContext):
        return Int()

    @saveType
    def visitAtomExpr(self, ctx:DecafParser.AtomExprContext):
        '''取消这层嵌套, 返回给上层'''
        return ctx.expr().accept(self)

    @saveType
    def visitCCast(self, ctx:DecafParser.CCastContext):
        '''强制类型转换, 返回转换后的类型 
        根据实验指导书, 这里不做其他规定
        '''
        ctx.cast().accept(self)
        return ctx.ty().accept(self)


    '''一元运算
    '''
    def checkUnary(self, unaryOp, ty):
        '''根据op确定具体的一元运算
        并检查ty
        '''
        if unaryOp in ['-', '!', '~']:
            return intUnaryRule(ty)
        elif unaryOp == '&': #取地址
            return addrOfRule(ty)
        elif unaryOp == '*': #解引用
            return derefRule(ty)
    
    @saveType
    def visitCUnary(self, ctx:DecafParser.CUnaryContext):
        ty = self.checkUnary(ctx.unaryOp().getText(), ctx.cast().accept(self))
        op = ctx.unaryOp().getText()
        if op == '&':  #取地址操作要求是左值
            self.checkLvalue(ctx.cast())
        #print("visit CUnary , op = {}, ty = {}".format(op, ty))
        return ty

    '''二元运算
    '''
    def checkBinary(self, binaryOp, tyL, tyR):
        if binaryOp == '+': 
            return combineRule(intBinaryRule, ptrArithRule)(tyL, tyR)
        elif binaryOp == '-': #与加法不同，允许指针减指针
            return combineRule(intBinaryRule, ptrArithRule, ptrMinusRule)(tyL, tyR)
        elif binaryOp in binaryLogicOps + binaryCalOps: #二元运算
            return intBinaryRule(tyL, tyR)
        elif binaryOp in binaryEqOps: # 判等
            return equalRule(tyL, tyR)
        elif binaryOp in binaryRelOps + binaryRaeOps: #比较
            return relationRule(tyL, tyR)
        elif binaryOp == '=': #赋值
            return assignRule(tyL, tyR)

    @saveType
    def visitCAdd(self, ctx:DecafParser.CAddContext):
        op = ctx.addOp().getText()
        tyL = ctx.add().accept(self)
        tyR = ctx.mul().accept(self)
        return self.checkBinary(op, tyL, tyR)
    
    @saveType
    def visitCMul(self, ctx:DecafParser.CMulContext):
        op = ctx.mulOp().getText()
        tyL = ctx.mul().accept(self)
        tyR = ctx.cast().accept(self)
        return self.checkBinary(op, tyL, tyR)
    
    @saveType
    def visitCRelation(self, ctx:DecafParser.CRelationContext):
        op = ctx.relationOp().getText()
        tyL = ctx.relation().accept(self)
        tyR = ctx.add().accept(self)
        return self.checkBinary(op, tyL, tyR)
    
    @saveType
    def visitCEqual(self, ctx:DecafParser.CEqualContext):
        # print('visitCEqual')
        op = ctx.equalOp().getText()
        # print('op = ', op)
        tyL = ctx.equal().accept(self)
        # print('='*50)
        # print("tyL = ", tyL)
        tyR = ctx.relation().accept(self)
        # print('='*50)
        # print('tyR = ', tyR)
        # print('='*100)
        return self.checkBinary(op, tyL, tyR)
    
    @saveType
    def visitCLogicAnd(self, ctx:DecafParser.CLogicAndContext):
        op = ctx.andOp().getText()
        tyL = ctx.logicAnd().accept(self)
        tyR = ctx.equal().accept(self)
        return self.checkBinary(op, tyL, tyR)
    
    @saveType
    def visitCLogicOr(self, ctx:DecafParser.CLogicOrContext):
        op = ctx.orOp().getText()
        tyL = ctx.logicOr().accept(self)
        tyR = ctx.logicAnd().accept(self)
        return self.checkBinary(op, tyL, tyR)

    '''三元表达式
    '''
    @saveType
    def visitCConditional(self, ctx:DecafParser.CConditionalContext):
        cond = ctx.logicOr().accept(self)
        then = ctx.expr().accept(self)
        el = ctx.conditional().accept(self)
        return condRule(cond, then, el)
    
    #赋值
    @saveType
    def visitCAssign(self, ctx:DecafParser.CAssignContext):
        op = ctx.assignOP().getText()
        tyL = ctx.unary().accept(self)
        tyR = ctx.expr().accept(self)
        res =  self.checkBinary(op, tyL, tyR) #先检查了类型
        self.checkLvalue(ctx.unary()) #再检查是否是左值  
        #类型检查已经帮左值排除掉一些了
        return res

    '''函数 
    '''
    def paramTypeListFactory(self, ctx:DecafParser.ParameterListContext):
        '''
        返回参数类型列表
        '''
        paramTypeList = []
        for declaration in ctx.declaration():
            if declaration.expr() is not None: #参数不可以初始化
                raise DecafException("got initialized function parameter")
            ty = self.getDeclType(declaration)
            if isinstance(ty, Array):
                raise DecafException("func parameter cannot be array")
            paramTypeList.append(ty)
        return paramTypeList

    def visitFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        ident = ctx.Ident().getText()
        returnType = ctx.ty().accept(self)
        paramTypeList = self.paramTypeListFactory(ctx.parameterList())
        
        self.manager.enterFunc(ident, returnType, paramTypeList)

    def visitFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        ident = ctx.Ident().getText()
        returnType = ctx.ty().accept(self)
        paramTypeList = self.paramTypeListFactory(ctx.parameterList())
        
        self.manager.enterFunc(ident, returnType, paramTypeList)
        self.visitChildren(ctx)
    
    def visitPostfixCall(self, ctx:DecafParser.PostfixCallContext):
        '''检查函数调用的参数类型是否匹配'''
        paramTypeList = list(map(lambda x: x.accept(self), ctx.argList().expr()))
        ident = ctx.Ident().getText()
        #return返回值的类型
        return self.manager.callFunc(ident,paramTypeList)
    
    #数组调用
    @saveType
    def visitPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        arrayTy = ctx.postfix().accept(self)
        indexTy = ctx.expr().accept(self)
        return arrayRule(arrayTy, indexTy)
    
    #全局变量
    def visitProgDeclaration(self, ctx:DecafParser.ProgDeclarationContext):
        ctx = ctx.declaration()
        ident = ctx.Ident().getText() #
        globl = self.ident2globl(ident)
        var = globl.var
        ty = self.getDeclType(ctx)
        self.var2type[var] = ty
        if ctx.expr() is not None: #类似assign, 检查赋值语句的做右操作数类型
            # print('expr = {}'.format(ctx.expr().getText()))
            exprType = ctx.expr().accept(self)
            # print("ty = {}, exprTy = {}".format(ty, exprType))
            assignRule(ty, exprType)

    def visitReturnStat(self, ctx:DecafParser.ReturnStatContext):
        '''检查函数的返回值是否和返回类型匹配'''
        returnType = self.manager.getCurFuncTy()
        ty = ctx.expr().accept(self)
        returnRule(returnType, ty)
    
    #if
    def visitIfStat(self, ctx:DecafParser.IfStatContext):
        self.visitChildren(ctx)
        intRule(ctx.expr().accept(self))

    '''循环
    检查条件判断表达式类型是否是int
    '''
    def visitForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        self.visitChildren(ctx)
        if ctx.cond is not None: #检查for循环的cond, 注意可能为None
            intRule(ctx.cond.accept(self))
    
    def visitForStat(self, ctx:DecafParser.ForStatContext):
        self.visitChildren(ctx)
        if ctx.cond is not None: #同理
            intRule(ctx.cond.accept(self))
    
    def visitWhileStat(self, ctx:DecafParser.WhileStatContext):
        self.visitChildren(ctx) 
        intRule(ctx.expr().accept(self)) # while循环的cond即expr
    
    def visitDoWhileStat(self, ctx:DecafParser.DoWhileStatContext):
        self.visitChildren(ctx)
        intRule(ctx.expr().accept(self))
          