
from ..DecafVisitor import DecafVisitor
from ..DecafParser import DecafParser
from .IRInstruction import *
from .IRGenerator import IRGenerator
from ..name.NameManager import NameInfo
from ..type.TypeManager import TypeInfo
from ..type.Types import *
from ..DecafException import DecafException

'''
每个节点有一个accept函数
accept函数有一个参数　即visitor
accept函数内部是一个对visitor的函数的调用
也就是说　可以通过实现visitor的函数　来定义accept的行为
'''

class LabelManager:
    '''
    用于label不能重复，需要一个Manager来管理label, 自动添加id
    '''
    def __init__(self):
        self.labelCnt = {}
        self.continueLabelList = []
        self.breakLabelList = []
    
    def generateLabel(self, label):
        if label in self.labelCnt:
            self.labelCnt[label] += 1
        else:
            self.labelCnt[label] = 0 #编号从0开始
        return f'{label}_{self.labelCnt[label]}'
    
    def enterLoop(self, continueLabel, breakLabel):
        self.continueLabelList.append(continueLabel)
        self.breakLabelList.append(breakLabel)
    
    def exitLoop(self):
        self.continueLabelList.pop()
        self.breakLabelList.pop()
    
    def getCurBreakLabel(self):
        '''返回当前所在循环语句的breakLabel
        '''
        if not len(self.breakLabelList):
            raise DecafException("break statement not in a loop")
        return self.breakLabelList[-1]
    
    def getCurContinueLabel(self):
        '''返回当前所在循环语句的beginLoopLabel
        '''
        if not len(self.continueLabelList):
            raise DecafException("continue statement not in a loop")
        return self.continueLabelList[-1]

class IRGenVisitor(DecafVisitor):
    def __init__(self, generator:IRGenerator, nameInfo: NameInfo, typeInfo: TypeInfo):
        self.generator = generator
        self.nameInfo = nameInfo #名称解析的结果
        self.typeInfo = typeInfo # 类型检查的结果
        self.labelManager = LabelManager()

        self.curFuncIdent = ''
    '''
    这里是重载
    accept是定义好的
    我们只需要重载visitor,就可以改变accept的行为
    context可以视为一个语法树里的一个node
    '''
    def node2var(self, node):
        '''返回node映射到的variable
        '''
        # print(f"in node2var, node = {node}, id = {id(node)}")
        return self.nameInfo.node2var[node]
    
    def node2type(self, node):
        '''返回node映射到的type
        '''
        return self.typeInfo.node2type[node]
    
    def visitLvalue(self, node):
        result = self.typeInfo.lvalueDict[node]
        for i in result:
            if isinstance(i, IRInstruction):
                self.generator.append(i)
            else: #是一个AST的node
                i.accept(self)

    def ident2func(self, ident):
        '''返回ident映射到的func
        '''
        return self.nameInfo.funcDict[ident]
    
    def binaryFactory(self, ctx, op):
        '''实现二元操作
        '''
        self.visitChildren(ctx) #先把左右操作数压栈
        self.generator.append(Binary(op.getText()))    

    def visitProgDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        '''全局变量声明
        '''
        pass

    def visitFuncDefinition(self, ctx:DecafParser.FuncDefinitionContext):
        #print(f'visit func definition : {ctx.ty()} {ctx.Ident()}')
        ident = ctx.Ident().getText()
        paramSize = len(self.typeInfo.funcDict[ident].paramTypeList)
        self.curFuncIdent = ident
        self.generator.enterFunc(ident, paramSize)
        ctx.block().accept(self)
        self.generator.exitFunc()
    
    def visitFuncDeclaration(self, ctx:DecafParser.FuncDeclarationContext):
        '''
        在名称解析阶段直接跳过了函数声明时的变量记录
        为了避免visitDeclaration报错，这里也跳过
        '''
        #print(f"visit func declaration : {ctx.ty()} {ctx.Ident()}")
        pass
    
    def visitPostfixCall(self, ctx:DecafParser.PostfixCallContext):
        '''函数调用
        调用call
        '''
        argExprList = ctx.argList().expr()
        '''
        逆序压栈
        因为offset是顺序增长的
        也就是说第一个参数应该最后被压栈
        '''
        for argExpr in reversed(argExprList):
            argExpr.accept(self)
        ident = ctx.Ident().getText()
        #可以这里直接引入paramSize
        paramSize = len(self.typeInfo.funcDict[ident].paramTypeList)
        # print(f'ident = {ident}, paramSize = {paramSize}')
        self.generator.append(Call(ident, paramSize))
    
    def visitPostfixArray(self, ctx:DecafParser.PostfixArrayContext):
        node = ctx.postfix()
        baseType = self.node2type(node).baseType
        size = baseType.size
        
        ctx.postfix().accept(self)
        ctx.expr().accept(self)
        self.generator.append([Const(size), Binary('*')]) #实际偏移量
        self.generator.append(Binary("+")) #计算
        ty = self.node2type(ctx)
        if not isinstance(ty, Array):
            self.generator.append(Load())
        #print("数组调用, ctx = {}, ty = {}, baseType = {}, baseTypeSize = {},  flag = {}".format(ctx.getText(), ty, baseType, size, isinstance(ty, Array)))
    
    def visitBlock(self, ctx: DecafParser.BlockContext):
        '''作用域
        离开时要pop干净
        '''
        self.visitChildren(ctx)
        self.generator.append([Pop()]*self.ident2func(self.curFuncIdent).node2blocksize[ctx])

    def visitReturnStat(self, ctx:DecafParser.ReturnStatContext):
        self.visitChildren(ctx)  #注意顺序,要先visitChildren 
        self.generator.append(Ret())
    
    def visitExprStat(self, ctx:DecafParser.ExprStatContext):
        self.visitChildren(ctx)
        self.generator.append(Pop()) 
    
    def visitIfStat(self, ctx:DecafParser.IfStatContext):
        ctx.expr().accept(self) #条件表达式的结果压栈
        endLabel = self.labelManager.generateLabel("END_LABEL") #label不能重复, 自动加id区分
        elseLabel = self.labelManager.generateLabel("ELSE_LABEL")
        if ctx.elseBranch: #有else分支
            self.generator.append(Branch("beqz", elseLabel)) #不成立，则执行else分支
            ctx.thenBranch.accept(self)#条件成立，执行then
            self.generator.append(Branch("br", endLabel)) #执行then后结束
            self.generator.append(Label(elseLabel)) #定义else入口地址
            ctx.elseBranch.accept(self) # else分支的ir
            self.generator.append(Label(endLabel)) #结束地址
        else:
            self.generator.append(Branch("beqz", endLabel)) #不成立, 直接进入end
            ctx.thenBranch.accept(self)#成立, 生成then分支的ir
            self.generator.append(Label(endLabel)) #结束地址
    
    '''
    循环语句
    将循环语句统一定义为Loop(pre, cond, body, post)
    pre: 初始化(可能有定义)
    cond: 循环判断
    body: 主体
    post: 每次循环结束后执行的操作(只有for语句是有post的)

    按如下思路生成循环语句的IR
    1. pre 的 IR
    2. label BEGINLOOP_LABEL：开始下一轮迭代
    3. cond 的 IR
    4. beqz BREAK_LABEL：条件不满足就终止循环
    5. body 的 IR
    6. label CONTINUE_LABEL：continue 跳到这
    7. post 的 IR
    8. br BEGINLOOP_LABEL：本轮迭代完成
    9. label BREAK_LABEL：条件不满足，或者 break 语句都会跳到这儿
    '''
    def loopFactory(self, label, pre, cond, body, post):
        beginLoopLabel = self.labelManager.generateLabel("BEGINLOOP_LABEL")
        continueLabel = self.labelManager.generateLabel("CONTINUE_LABEL") if post else beginLoopLabel
        breakLabel = self.labelManager.generateLabel("BREAK_LABEL")
        self.labelManager.enterLoop(continueLabel=continueLabel, breakLabel=breakLabel)
        #pre的IR
        if pre:
            pre.accept(self)
            if isinstance(pre, DecafParser.ExprContext):
                self.generator.append(Pop())
        #label BEGINLOOP_LABEL
        self.generator.append(Label(beginLoopLabel))
        #cond的IR
        if cond:
            cond.accept(self)
        else: #未声明 默认判定成功 压栈一个真值
            self.generator.append(Const(1))
        #beqz BREAK_LABEL
        self.generator.append(Branch("beqz", breakLabel))
        #body的IR
        body.accept(self)
        #post的IR
        if post:
            #label CONTINUE_LABEL
            self.generator.append(Label(continueLabel))
            post.accept(self)
            if isinstance(post, DecafParser.ExprContext):
                self.generator.append(Pop())
        #br BEGINLOOP_LABEL
        self.generator.append(Branch("br", beginLoopLabel))
        #label BREAK_LABEL
        self.generator.append(Label(breakLabel))       
        self.labelManager.exitLoop()  

    def visitForDeclStat(self, ctx:DecafParser.ForDeclStatContext):
        self.loopFactory("for", ctx.pre, ctx.cond, ctx.stat(), ctx.post)
        self.generator.append([Pop()]*self.ident2func(self.curFuncIdent).node2blocksize[ctx])
        #有定义的for循环提供了一层新的作用域，离开时pop掉

    def visitForStat(self, ctx:DecafParser.ForStatContext):
        self.loopFactory("for", pre=ctx.pre, cond=ctx.cond, body=ctx.stat(), post=ctx.post)

    def visitWhileStat(self, ctx:DecafParser.WhileStatContext):
        self.loopFactory("while", pre=None, cond=ctx.expr(), body=ctx.stat(), post=None)

    def visitDoWhileStat(self, ctx:DecafParser.DoWhileStatContext):
        #先执行一次body, 所以pre==body
        self.loopFactory("doWhile", pre=ctx.stat(), cond=ctx.expr(), body=ctx.stat(), post=None)
    
    def visitBreakStat(self, ctx:DecafParser.BreakStatContext):
        '''br到当前所在循环的breakLabel
        '''
        curBreakLabel = self.labelManager.getCurBreakLabel()
        self.generator.append(Branch("br", curBreakLabel))

    def visitContinueStat(self, ctx:DecafParser.ContinueStatContext):
        '''br到当前所在循环的beginLoopLabel
        '''
        curContinueLabel = self.labelManager.getCurContinueLabel()
        self.generator.append(Branch("br", curContinueLabel))

    # def _computeAddr(self, lvalue:Unary):
    #     '''计算assign语句左操作数的地址
    #     '''
    #     if isinstance(lvalue, DecafParser.TUnaryContext):
    #         return self._computeAddr(lvalue.postfix())
    #     if isinstance(lvalue, DecafParser.PostfixContext):
    #         return self._computeAddr(lvalue.atom())
    #     if isinstance(lvalue, DecafParser.AtomIdentContext):
    #         var = self.node2var(lvalue.Ident())
    #         if var.offset != None: #是普通变量 需要!=None而不是!=0
    #             return self.generator.append(FrameAddr(var.offset)) #把地址压栈
    #         else: #是全局变量
    #             return self.generator.append(GlobalAddr(var.ident))
    #     elif isinstance(lvalue, DecafParser.AtomExprContext):
    #         return self._computeAddr(lvalue.expr())
    #     raise  DecafException(f"{lvalue.getText()} is not a lvalue")

    #赋值语句
    def visitCAssign(self, ctx:DecafParser.CAssignContext):
        ctx.expr().accept(self)#继续计算右操作数, 压栈
        self.visitLvalue(ctx.unary())
        # self._computeAddr(ctx.unary())
        # var = self.node2var(ctx.Ident())
        # self.generator.append(FrameAddr(var.offset)) #把左操作数　即被赋值的变量的地址 压栈, 然后接一个store指令
        self.generator.append(Store()) #通过store指令，更新变量的值

    #声明
    def visitDeclaration(self, ctx:DecafParser.DeclarationContext):
        #print("declaration : ", ctx.Ident())
        var = self.node2var(ctx.Ident()) #根据名称解析的结果，找到这个变量
        if ctx.expr() is not None: #如果有初始化, 就继续visit, 到下游创建FrameAddr, 
            ctx.expr().accept(self)
        else: #初始化为0, 直接压栈
            self.generator.append([Const(0)]*(var.size // INT_BYTES))
    
    def visitCConditional(self, ctx: DecafParser.CConditionalContext):
        ctx.logicOr().accept(self)
        #相当于一个if else语句 
        endLabel = self.labelManager.generateLabel("END_LABEL")
        elseLabel = self.labelManager.generateLabel("ELSE_LABEL")
        self.generator.append(Branch("beqz", elseLabel)) #不成立，则:后的表达式
        ctx.expr().accept(self)#条件成立，执行:前的表达式
        self.generator.append(Branch("br", endLabel)) #执行then后结束
        self.generator.append(Label(elseLabel)) #定义else入口地址
        ctx.conditional().accept(self) # else分支的ir
        self.generator.append(Label(endLabel)) #结束地址

    def visitCUnary(self, ctx:DecafParser.CUnaryContext):
        op = ctx.unaryOp().getText()
        '''引入取地址和解引用后, 需要做特判
        根据实验指导书:
        对于取地址 &，生成其操作数左值的地址作为其值。
        解引用 * 的 IR 就是子表达式的 IR 接上一个 load。
        '''
        if op == '&':#将它的addr压栈,  不load
            self.visitLvalue(ctx.cast())
        elif op == '*':
            self.visitChildren(ctx)
            self.generator.append(Load())
        else:
            self.visitChildren(ctx) #先压栈操作数
            self.generator.append(Unary(op))
    
    def visitCAdd(self, ctx:DecafParser.CAddContext):
        op = ctx.addOp().getText()
        nodeL = ctx.add()
        nodeR = ctx.mul()
        tyL = self.node2type(nodeL)
        tyR = self.node2type(nodeR)
        #针对指针的加减法做特殊处理
        if isinstance(tyL, Ptr):#左操作数为指针
            nodeL.accept(self) #左右操作数压栈
            nodeR.accept(self)
            if isinstance(tyR, Ptr): #右操作数也为指针
                self.generator.append(Binary(op))
                self.generator.append([Const(INT_BYTES), Binary('/')]) 
            else:
                self.generator.append([Const(INT_BYTES), Binary("*")]) 
                self.generator.append(Binary(op))
        else: #左操作数为int
            if isinstance(tyR, Ptr):#右操作数为指针
                nodeL.accept(self)
                self.generator.append([Const(INT_BYTES), Binary("*")])
                nodeR.accept(self)
                self.generator.append(Binary(op))
            else:
                self.visitChildren(ctx)
                self.generator.append(Binary(op))
        #self.binaryFactory(ctx, ctx.addOp())
    
    def visitCMul(self, ctx:DecafParser.CMulContext):
        self.binaryFactory(ctx, ctx.mulOp())
    
    def visitCRelation(self, ctx:DecafParser.CRelationContext):
        self.binaryFactory(ctx, ctx.relationOp())
    
    def visitCEqual(self, ctx:DecafParser.CEqualContext):
        self.binaryFactory(ctx, ctx.equalOp())
    
    def visitCLogicOr(self, ctx:DecafParser.CLogicOrContext):
        self.binaryFactory(ctx, ctx.orOp())
    
    def visitCLogicAnd(self, ctx:DecafParser.CLogicAndContext):
        self.binaryFactory(ctx, ctx.andOp())

    def visitAtomInteger(self, ctx:DecafParser.AtomIntegerContext):
        v = int(ctx.Integer().getText())
        self.generator.append(Const(v))

    def visitAtomIdent(self, ctx: DecafParser.AtomIdentContext):
        var = self.node2var(ctx.Ident())
        ty = self.node2type(ctx)
        '''
        通过offset是否为None,　区别是全局变量还是普通变量
        '''
        if var.offset != None: #是普通变量 需要!=None而不是!=0
            self.generator.append(FrameAddr(var.offset)) #把地址压栈
        else: #是全局变量
            self.generator.append(GlobalAddr(var.ident))
        
        if not isinstance(ty, Array):
            self.generator.append(Load())#用load指令把这个变量的值压栈

    def visitProg(self, ctx:DecafParser.ProgContext):
        '''定义全局变量
        '''
        for globl in self.nameInfo.globlDict.values():
            self.generator.defGlobl(globl)
        self.visitChildren(ctx)
