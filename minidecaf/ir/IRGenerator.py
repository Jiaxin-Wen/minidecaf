from .IRInstruction import *
from ..name.NameManager import GloblVar

class IRFunc:
    '''一个中间码表示的函数'''
    def __init__(self,name, paramSize, instructionList):
        self.name = name #函数名
        self.paramSize = paramSize #函数参数个数
        self.instructionList = instructionList #函数体

    def __str__(self):
        def toStr(instruction):
            if type(instruction) == Label:
                return str(instruction)
            else:
                return f"\t{instruction}"
        return f"{self.name}:\n" + '\n'.join(map(toStr, self.instructionList))

class IRGlobl:
    '''全局变量
    包括value(初始值), size, ident, align
    '''
    def __init__(self, ident, value, size, align=INT_BYTES):
        self.ident = ident
        self.value = value
        self.size = size
        self.align = align
    
    def __str__(self):
        return f"IRGlobl: {self.ident}, value = {self.value}, size = {self.size}, align = {self.align}"

class IRProgram:
    '''分函数和全局变量存储中间码'''
    def __init__(self, funcList, globlList):
        self.funcList = funcList
        self.globlList = globlList
    
    def __str__(self):
        return '\n'.join(map(str, self.funcList))
    

class IRGenerator:
    '''
    在visit的过程中产生中间代码,并转成需要的格式返回
    '''
    def __init__(self):
        self.funcList = [] #list of IRFunc
        self.globlList = []

        self.currentFuncName = '' 
        self.currentFuncParamSize = -1
        self.currentFuncIRList = []
    
    '''
    一个IRFunc的构造从进入某个函数开始,退出该函数结束。
    进入函数标志: visitFunc被调用
    退出函数标志: visitChildren调用结束
    '''
    def enterFunc(self,name, paramSize):
        self.currentFuncName = name
        self.currentFuncParamSize = paramSize
        self.currentFuncIRList = [] #复位
    
    def exitFunc(self):
        self.funcList.append(IRFunc(self.currentFuncName, self.currentFuncParamSize, self.currentFuncIRList))
    
    def defGlobl(self, globlVar:GloblVar):
        irglobl = IRGlobl(ident=globlVar.var.ident, value=globlVar.value,size = globlVar.size)
        self.globlList.append(irglobl)
        
    def append(self, instruction):
        '''装饰器不能利用函数的返回值，这里不能省略掉, 只能每次generator.append
        '''
        if isinstance(instruction, list):
            for i in instruction:
                self.currentFuncIRList.append(i)
        else:
            self.currentFuncIRList.append(instruction)

    #转换为中间码返回
    def getIR(self):
        return IRProgram(self.funcList, self.globlList)
