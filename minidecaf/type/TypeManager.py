from ..DecafParser import DecafParser
from ..DecafException import DecafException
class Func:
    def __init__(self, returnType, paramTypeList):
        self.returnType = returnType # step9 暂时就用一个str
        self.paramTypeList = paramTypeList # 函数参数列表
    
    def __eq__(self, other):
        '''比较两个同名函数是否冲突
        '''
        flag1 = self.returnType == other.returnType
        flag2 = self.paramTypeList == other.paramTypeList
        return flag1 and flag2

class TypeInfo:
    def __init__(self):
        self.funcDict = {} # funcIdent -> Func
        self.node2type = {} # node -> Type
        self.lvalueDict = {} # node -> ir | ctx
        

class TypeManager:
    def __init__(self):
        self.typeInfo = TypeInfo()
        self.curFunc = ''
    
    def getCurFuncTy(self):
        '''返回当前函数的返回类型'''
        return self.typeInfo.funcDict[self.curFunc].returnType

    def enterFunc(self, ident, returnType, paramTypeList):
        '''
        处理一个函数(定义或是声明)
        将函数记录到TypeInfo的funcDict里
        '''
        func = Func(returnType, paramTypeList)
        if ident in self.typeInfo.funcDict: #如果已经出现过同名函数
            '''
            名称解析阶段只会检测出同名的函数
            但不会检测出同名,但返回值或参数不同的同名函数 
            这类报错由类型检查阶段来做 
            '''
            if func != self.typeInfo.funcDict[ident]:
                raise DecafException(f"conflict type info of func : {ident}")
        else:
            self.typeInfo.funcDict[ident] = func
        self.curFunc = ident #确认无误后更新curFunc

    # def callFunc(self, ident, argTypeList):
    #     '''函数调用前的类型检查: 检查参数是否匹配
    #     '''
    #     print(' argList = ', argTypeList)
    #     print(' myList = ', self.typeInfo.funcDict[ident].paramTypeList)
    #     if argTypeList != self.typeInfo.funcDict[ident].paramTypeList:
    #         raise DecafException(f"wrong parameter types when call function : {ident}")
    
    def callFunc(self, ident, paramTypeList):
        '''函数调用前的类型检查: 检查参数类型是否匹配
        '''
        # print('call type list = ', paramTypeList)
        # print('declare type list = ', self.typeInfo.funcDict[ident].paramTypeList)
        if paramTypeList != self.typeInfo.funcDict[ident].paramTypeList:
            raise DecafException(f"wrong args when call function : {ident}")
        
        return self.typeInfo.funcDict[ident].returnType
    
    def bindNodeType(self, ctx, ty):
        self.typeInfo.node2type[ctx] = ty
    
    def bindLvalue(self, ctx, loc):
        self.typeInfo.lvalueDict[ctx] = loc
    
    def getTypeInfo(self):
        return self.typeInfo



    

