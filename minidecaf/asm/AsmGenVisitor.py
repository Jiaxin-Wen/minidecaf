from .AsmGenerator import AsmGenerator
from .AsmCode import *
from ..ir import *
from ..utils import *

def ir2asm(toStr):
    #参考dzy助教代码,采用装饰器
    def func(*args,**kwargs):
        '''
        (1) IR指令对象 -> risc-v指令字符串 
        (2) risc-v指令字符串-> risc-v指令对象
        '''
        codeStrList = toStr(*args,**kwargs) #第一阶段
        return [AsmInstruction(i) if not isinstance(i, AsmCode) else i for i in codeStrList] #第二阶段
        #注意这里要判断一下是否已经是AsmInstruction的对象,否则一些指令由于某些原因(比如simple_pop的调用)会被构造两次,导致格式错误
    return func


@ir2asm
def _push(v): #即toStr
    if type(v) == int: #是立即数
        codeStrList = [ 
            f"addi sp,sp,-{INT_BYTES}", #开栈帧
            f"li t1,{v}", #先存到寄存器里
            "sw t1,0(sp)"#再存到栈上
        ]
    else: #是寄存器
        codeStrList = [ 
            f"addi sp,sp,-{INT_BYTES}", #开栈帧
            f"sw {v},0(sp)"
        ]
    return codeStrList

#批量push
def push(*items):
    return flatten(map(_push, items))

@ir2asm
def ret(func):
    codeStrList = [ 
        f"beqz x0,{func}_exit" #返回值已压栈，直接跳到func_exit执行
        # "lw a0,0(sp)", #从栈中取出返回值
        # "addi sp,sp,4" #清除栈帧
    ]
    return codeStrList

@ir2asm
def label(text):
    codeStrList = [
        AsmLabel(text)
    ]
    return codeStrList

@ir2asm
def _pop(reg):
    codeStrList = [
        f"lw {reg},0(sp)" 
    ] if reg else []
    codeStrList += [
        f'addi sp,sp,{INT_BYTES}'
    ]
    return codeStrList

#仿照助教的设计,将pop的命名留给实现批量pop的方法, 供其他函数调用
def pop(*regs):#每次pop都返回一个list,要从二维降到一维
    return flatten(map(_pop, regs))

@ir2asm
def unary(op):
    op = {'-':'neg', '~': 'not', '!': 'seqz'}[op]
    codeStrList = pop("t1") + [f"{op} t1, t1"] + push("t1")
    return codeStrList

@ir2asm
def binary(op):
    '''
    先pop两次 取出两个操作数 完成计算 再将结果压栈
    '''
    if op in binaryCalOps: # + - * / %
        return pop("t2", "t1") + [f"{binaryOpAsmDict[op]} t1, t1, t2"] + push("t1")
    elif op in binaryEqOps: # == !=
        return pop("t2", "t1") + ["sub t1, t1, t2", f"{binaryOpAsmDict[op]} t1, t1"] + push("t1")
    elif op in binaryRelOps: #<  >
        return pop("t2", "t1") + [f"{binaryOpAsmDict[op]} t1, t1, t2"] + push("t1")
    elif op == "&&":
        return pop("t2") + unary("!") + push("t2") + unary("!") + binary("||") + unary("!")
    elif op == "||":
        return pop("t2", "t1") + ["or t1, t1, t2", "snez t1, t1"] + push("t1")
    elif op == "<=":
        return binary(">") + unary("!")
    elif op == ">=":
        return binary("<") + unary("!")

@ir2asm
def load():
    '''加载变量的值:
    把栈顶的值作为地址(变量的地址)，加载该地址的值, 压栈
    '''
    return pop("t1") + [f"lw t1, 0(t1)"] + push("t1")

@ir2asm
def store():
    '''变量赋值:
    弹出栈顶作为地址(变量的地址)，读取新栈顶作为值，将值写入地址开始的int
    '''
    return pop("t2", "t1") + [f"sw t1,0(t2)"] + push("t1")

@ir2asm
def frameAddr(offset):
    '''将变量在栈中的地址压栈:
    依次将fp和offset压栈，执行一次加法即可
    '''
    return push("fp", offset) + binary("+")

@ir2asm
def globlAddr(ident):
    return [f"la t1, {ident}"] + push("t1")

@ir2asm
def branch(op, label):
    '''
    参考python实现:
    作为一个binary进行实现
    以branch2binary中的一项"br":(2, "beq")为例
    j label 等价于 beq 0, 0, label
    所以先push两个0, 再pop出来
    '''
    branch2binary = {"br":(2, "beq"),"beqz":(1, "beq"), "bnez":(1, "bne")}
    if op in branch2binary:
        num, op = branch2binary[op]
        return push(*[0]*num) + branch(op, label)
    return pop("t2", "t1") + [f"{op} t1,t2, {label}"]

@ir2asm
def call(ident, paramSize):
    '''
    caller压栈参数已经通过frameaddr和load指令完成了(因为在visitAtomIdent时也包括了函数形参)
    call指令之后要pop掉栈上之前压入的参数
    '''
    return [f"call {ident}"] + pop(*[None]*paramSize) + push("a0") #返回值存在栈顶

class AsmGenVisitor(IRVisitor):
    '''
    重载IRVisitor的接口
    遍历调用IR的accpet, 更新AsmGenerator的列表
    '''
    def __init__(self, generator:AsmGenerator):
        self.generator = generator
        self.irProgram = None
        self.curFunc = ''
    
    #重载IRVisitor的接口
    def visitConst(self, ir):
        self.generator.append(AsmAnnotation("const"))
        self.generator.append(push(ir.value))
    
    def visitRet(self, ir):
        self.generator.append(AsmAnnotation("return"))
        self.generator.append(ret(self.curFunc))
    
    def visitUnary(self, ir):
        self.generator.append(unary(ir.op))
    
    def visitBinary(self, ir):
        self.generator.append(binary(ir.op))
    
    def visitLoad(self, ir):
        self.generator.append(AsmAnnotation("load"))
        self.generator.append(load())

    def visitStore(self, ir):
        self.generator.append(AsmAnnotation("store"))
        self.generator.append(store())

    def visitFrameAddr(self, ir):
        self.generator.append(AsmAnnotation("frameaddr"))
        self.generator.append(frameAddr(ir.offset))
    
    def visitGloblAddr(self, ir):
        self.generator.append(AsmAnnotation("globladdr"))
        self.generator.append(globlAddr(ir.globl))

    def visitPop(self, ir):
        self.generator.append(AsmAnnotation("pop"))
        self.generator.append(pop(None))
    
    def visitLabel(self, ir):
        self.generator.append(label(ir.label))

    def visitBranch(self, ir):
        self.generator.append(AsmAnnotation("branch"))
        self.generator.append(branch(ir.op, ir.label))
    
    def visitCall(self, ir):
        ident = ir.ident
        paramSize = ir.paramSize
        self.generator.append(call(ident, paramSize))
        #call也需要paramSize, 将之前压栈的参数(即在栈帧之上的参数)弹出

    def setPrologue(self, irFunc:IRFunc):
        self.generator.append([
            AsmAnnotation("PROLOGUE"),
            AsmSection(".text"),
            AsmSection(f".globl {irFunc.name}"), 
            AsmLabel(irFunc.name)]+
            push("ra", "fp")+[  # 保存ra, fp
            AsmInstruction("mv fp, sp")])
        '''
        由于名称解析阶段的offset都是以进入作用域之后的fp为基础
        但ir生成阶段压栈的参数都在栈帧上方
        所以这里需要把参数的值copy到相应的offset的位置上
        copy即取出,再压栈
        '''
        for i in range(irFunc.paramSize):
            oriOffset = INT_BYTES * (i + 2) #+2是callee保存的ra, fp
            self.generator.append([
                AsmInstruction(f"lw t1, {oriOffset}(fp)")] + #原本参数相对于fp的offset, load到t1中
                push("t1")) #压栈

    def setEpilogue(self, irFunc: IRFunc):
        self.generator.append([
            AsmAnnotation("PROLOGUE")]+
            push(0)+[ #给一个默认的返回值
            AsmLabel(f"{irFunc.name}_exit"),
            AsmInstruction("lw a0, 0(sp)"), #从栈上加载返回值
            AsmInstruction("mv sp, fp")]+ 
            pop("fp", "ra")+[ #恢复
            AsmInstruction("jr ra")]
        )
    
    def visitFunc(self, irFunc:IRFunc): 
        self.setPrologue(irFunc)
        self.curFunc = irFunc.name
        #函数体
        self.generator.append(AsmAnnotation("FUNC BODY"))
        for ir in irFunc.instructionList:
            ir.accept(self) #调用accept, 间接调用重载的visitXXX, 生成指令对应的asm
        self.setEpilogue(irFunc)

    def visitGlobl(self, irGlobl: IRGlobl):
        ident = irGlobl.ident
        value = irGlobl.value
        size = irGlobl.size
        align = irGlobl.align
        if irGlobl.value is None: #未初始化, 在.bss
            self.generator.append(AsmSection(f".comm {ident},{size},{align}"))
        else: #已初始化, 在.data
            self.generator.append([
                AsmSection(".data"),
                AsmSection(f".globl {ident}"),
                AsmSection(f".align {align}"),
                AsmSection(f".size {ident},{size}"),
                AsmLabel(ident),
                AsmSection(f".word {value}")
            ])

    def visit(self, irProgram:IRProgram):
        '''
        如何根据ir指令　确定应该visit哪个asm visitor的函数? -> accept + visitor
        '''
        self.irProgram = irProgram
        #先定义全局变量
        for globl in irProgram.globlList:
            self.visitGlobl(globl)
        for func in irProgram.funcList:
            self.visitFunc(func)
        # for ir in irList:
        #     ir.accept(self) #根据type, 更新generator的情况

