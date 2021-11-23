from ..DecafVisitor import DecafVisitor
from ..DecafParser import DecafParser
from ..DecafException import DecafException
from .NameManager import *
from ..utils import MAX_INT


class NameVisitor(DecafVisitor):
    '''
    遍历AST,更新NameManager
    遍历过程中，在做名称解析的同时，同时也做错误检查

    名称解析阶段并不直接保存变量的值
    只记录变量的addr
    '''
    def __init__(self, nameManager: NameManager):
        self.nameManager = nameManager

    
    # def visitParameterList(self, ctx:DecafParser.ParameterListContext):
    #     '''函数参数
    #     '''
    #     self.visitChildren(ctx)  #先把变量记录了
    #     #self.nameManager.defParamList(ctx.declaration())
    #     # for declaration in ctx.declaration():
    #     #     ident = declaration.Ident()
    #     #     variable = self.nameManager.

    def getVariableSize(self, ctx:DecafParser.DeclarationContext):
        #引入数组后, 计算变量的size
        size = 1
        for dimen in ctx.Integer():
            dimenSize = int(dimen.getText())
            if dimenSize == 0 or dimenSize >= MAX_INT: #每一维长度只能是正整数常数
                raise DecafException("array dimen size range is (0, 1<<31-1), got {}".format(dimenSize))
            size *= dimenSize
        return size

    #函数声明
    def visitFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        ident = ctx.Ident().getText()
        self.nameManager.declFunc(ident)
        #这里直接不visit paramList了
        #感觉也是有道理的, 这里其实是一个新增的作用域, 需要的记录的就是类型，用于之后匹配．变量名无所谓

    #函数定义
    def visitFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        '''
        一个新的作用域
        '''
        ident = ctx.Ident().getText()
        self.nameManager.defFunc(ident) #定义函数
        self.nameManager.enterScope(ctx.block()) #进入作用域
        ctx.parameterList().accept(self) #函数参数通过vistDecalaration记录
        self.visitChildren(ctx.block())
        self.nameManager.exitScope(ctx.block()) #离开作用域
    
    def visitProgDeclaration(self, ctx:DecafParser.ProgDeclarationContext):
        '''全局变量
        '''
        declaration = ctx.declaration()
        expr = declaration.expr()
        value = None
        if expr is not None:
            try:
                value = int(expr.getText())
            except:
                raise DecafException("globl variable initial value must be Integer")
        ident = declaration.Ident().getText()
        size = self.getVariableSize(declaration)*INT_BYTES
        #print('globl variable : {}, size = {}'.format(ident, size) )
        var = Variable(ident=ident, size=size, offset=None)
        self.nameManager.defGloblVariable(var=var, ident=ident, value=value)

    def visitBlock(self, ctx: DecafParser.BlockContext):
        '''
        block也是一个新的作用域, 包含于func的作用域 
        一方面, 这会在函数引入参数之后会体现出来
        另一方面, block也作为一个statement, 定义一个新的作用域
        '''
        self.nameManager.enterScope(ctx)
        self.visitChildren(ctx)
        self.nameManager.exitScope(ctx)

    def visitDeclaration(self, ctx:DecafParser.DeclarationContext):
        if ctx.expr(): #有初始化
            ctx.expr().accept(self)
        ident = ctx.Ident().getText()
        size = self.getVariableSize(ctx)
        #print('declaration {}, node = {}'.format(ident, ctx.Ident()))
        #在manager的函数里检查是否有重定义, 都用nameManager维护
        self.nameManager.defVariable(ctx.Ident(), ident, size)
    
    def visitForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        '''for循环内可以定义变量
        作为一个新的作用域
        '''
        self.nameManager.enterScope(ctx)
        self.visitChildren(ctx)
        self.nameManager.exitScope(ctx)

    def visitAtomIdent(self, ctx:DecafParser.AtomIdentContext):
        '''
        补充当前作用域用到的(但不是在当前作用域声明的)，需要保存到栈帧中的变量
        '''
        self.nameManager.useVariable(ctx.Ident())
        
