from ..utils import *

class IRInstruction:
    def __repr__(self):
        return self.__str__() #重载

class Const(IRInstruction):
    '''压栈一个int'''
    def __init__(self, value):
        MAX_INT = 2**31 - 1 #类型检查
        MIN_INT = -2**32
        assert MIN_INT <= value <= MAX_INT
        self.value = value  

    def accept(self,visitor):
        visitor.visitConst(self)      

    def __str__(self):
        return "const  {}".format(self.value)


class Ret(IRInstruction):
    '''return'''

    def accept(self, visitor):
        visitor.visitRet(self)

    def __str__(self):
        return "ret"

class Unary(IRInstruction):
    def __init__(self, op):
        assert op in unaryOps
        self.op = op
    
    def accept(self, visitor):
        visitor.visitUnary(self)

    def __str__(self):
        return unaryOpDict[self.op]

class Binary(IRInstruction):
    def __init__(self, op):
        assert op in binaryOps
        self.op = op
    
    def accept(self, visitor):
        visitor.visitBinary(self)
    
    def __str__(self):
        return binaryOpDict[self.op]

class Pop(IRInstruction):
    def accept(self, visitor):
        visitor.visitPop(self)
    
    def __str__(self):
        return "pop"

class Load(IRInstruction):
    '''
    把栈顶的值作为地址(变量的地址)，加载该地址的值, 压栈
    用于加载变量的值
    '''
    def accept(self, visitor):
        visitor.visitLoad(self)

    def __str__(self):
        return "load"

class Store(IRInstruction):
    '''
    弹出栈顶作为地址(变量的地址)，读取新栈顶作为值，将值写入地址开始的int
    用于实现赋值
    '''
    def accept(self, visitor):
        visitor.visitStore(self)
    
    def __str__(self):
        return "store"

class FrameAddr(IRInstruction):
    '''
    把fp+offset(即变量在栈中的地址) 压栈
    辅助实现load, store指令
    '''
    def __init__(self, offset):
        self.offset = offset
    
    def accept(self, visitor):
        visitor.visitFrameAddr(self)

    def __str__(self):
        return f"frameaddr {self.offset}"

class GlobalAddr(IRInstruction):
    '''
    全局变量
    '''
    def __init__(self, globl):
        self.globl = globl
    
    def accept(self, visitor):
        visitor.visitGloblAddr(self)

    def __str__(self):
        return f"globl {self.globl}"
    
class Label(IRInstruction):
    '''定义一个label 用于地址跳转
    '''
    def __init__(self, label):
        self.label = label
    
    def accept(self, visitor):
        visitor.visitLabel(self)
    
    def __str__(self):
        return self.label+':'

class Branch(IRInstruction):
    '''有条件/无条件跳转
    '''
    def __init__(self, op, label):
        assert op in branchOps
        self. op = op
        self.label = label
    
    def accept(self, visitor):
        visitor.visitBranch(self)
    
    def __str__(self):
        return f'{self.op} {self.label}'

class Call(IRInstruction):
    '''函数调用: 参数压栈, 跳转
    '''
    def __init__(self, ident, paramSize):
        '''
        这里的func只是一个函数名str
        '''
        self.ident = ident
        self.paramSize = paramSize
    
    def accept(self, visitor):
        visitor.visitCall(self)

    def __str__(self):
        return f"call {self.ident}  (paramSize = {self.paramSize})"
        