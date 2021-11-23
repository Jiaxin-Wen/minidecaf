from ..utils import INT_BYTES
from ..DecafException import DecafException
from copy import deepcopy
from ..DecafParser import DecafParser

class Variable:
    '''
    变量
    '''
    cnt = {} # ident -> cnt
    def __init__(self, ident, size, offset):
        '''
        ident: 变量名
        size: size
        offset: 到栈帧起始位置(fp)的offset
        id: 后缀(用来区分同名变量, 便于debug, 不会直接用到)
        '''
        self.ident = ident
        self.size = size
        self.offset = offset
        self.id = self.getId()
    
    def getId(self):
        if self.ident in Variable.cnt:
            Variable.cnt[self.ident] += 1
        else:
            Variable.cnt[self.ident] = 0
        return Variable.cnt[self.ident]
    
    def __str__(self):
        return f"variable: {self.ident}({self.id})"
    
    '''
    注意: 需要重载以正常使用dict
    '''
    def __eq__(self, other):
        return self.ident == other.ident and self.id == other.id
    
    def __hash__(self):
        #print('enter hash, ident = {}, id = {}, hash = {}'.format(self.ident, self.id, hash((self.ident, self.id))))
        return hash((self.ident, self.id))    

class Func:
    '''
    维护一个函数内的变量
    '''
    def __init__(self, ident, defined,):
        self.ident = ident #函数名
        self.defined = defined #函数是否已有定义
        self.node2var = {} #AST的一个节点 -> Variable
        self.node2blocksize = {}
        '''参数也会以函数作用域内变量的形式, 记录在node2var中
        '''
        
    def addVariable(self, node, var):
        '''添加一个函数作用域内的<node, var> pair
        '''
        self.node2var[node] = var
    
    def __str__(self):
        s = f"function:{self.ident} \n"
        for var in self.node2var.values():
            s += f"\tvariable = {var.ident}({var.id}), frameaddr = {var.offset}\n"
        s += '='*50 + '\n'
        return s

class GloblVar:
    '''全局变量
    '''
    def __init__(self, var, value):
        self.var = var
        self.value = value #初始值
        self.size = var.size #大小

    def __str__(self):
        return f"globl variable: {self.var}, initial value = {self.value}, size = {self.size}"
    
class NameInfo:
    '''
    管理所有functions 
    最后统一作为名称解析的结果返回
    '''
    def __init__(self):
        self.funcDict = {}  # 函数名 -> Func
        self.globlDict = {} # 全局变量名 -> GloblVar
        self.node2var = {}

    def finish(self):
        for func in self.funcDict.values():
            # print(func)
            self.node2var.update(func.node2var)
        # for node, var in self.node2var.items():
        #     print(f"node = {node}, var = {var}")
    
    def __str__(self):
        def f(fn):
            func, funcNameInfo = fn
            indentedFuncNameInfo = "\t" + str(funcNameInfo).replace("\n", "\n\t")
            return f"NameInfo for {func}:\n{indentedFuncNameInfo}"
        res = "\n--------\n\n".join(map(f, self.funcDict.items()))
        res += "\n--------\n\nGlobInfos:\n\t"
        res += "\n\t".join(map(str, self.globlDict.values()))
        return res

class ScopeNameList:
    '''
    由于"重复声明"只会在子作用域中出现，如果出现和父作用域同名变量，则视为覆盖而不是重复
    因此要同时维护两个list of dict，其中一个只维护当前作用域新加入的变量，进行语义检查
    '''
    def __init__(self):
        '''初始化的作用域是全局
        '''
        self.inheritList = [{}] #继承自父作用域的dict
        self.newList = [{}] #本作用域的dict

    def push(self):
        '''进入一个新的作用域
        '''
        #print("准备进入一个新的作用域, 上个作用域的dict = ", self.inheritList[-1])
        self.inheritList.append(deepcopy(self.inheritList[-1]))
        self.newList.append({})    

    def pop(self):
        '''离开当前作用域, pop一次
        '''
        self.inheritList.pop()
        self.newList.pop()
    
    def __getitem__(self, ident):
        return self.inheritList[-1][ident]

    def __setitem__(self, ident, variable):
        self.inheritList[-1][ident] = self.newList[-1][ident] = variable
    
    def checkRedefinition(self, ident):
        return ident in self.newList[-1]
    
    def __contains__(self, ident):
        return ident in self.inheritList[-1]

class NameManager:
    '''
    在遍历过程中维护nameinfo, 得到最终的结果: 一个node->Variable的dict
    '''
    def __init__(self):
        self.nameInfo = NameInfo()
        self.scopeNameList = ScopeNameList()
        self.frameOffsetList = [] #全部栈帧的offset
        self.curFrameOffset = 0 #当前栈帧的offset
        self.curFunc = None

    # def defParamList(self, funcIdent, paramList):
    #     '''记录函数参数
    #     '''
    #     result = []
    #     for param in paramList:
    #         ident = param.Ident()
    #         var = self.scopeNameList[ident]
    #         result.append(var)
    #     funcParam = FuncParam(result)

    def declFunc(self, ident):
        '''
        声明新函数
        '''
        #重新声明是允许的
        # if ident in self.nameInfo.funcDict: #语义检查
        #     raise DecafException(f"redeclaration function : {ident}")
        if ident in self.nameInfo.globlDict: #检查是否与全局变量冲突
            raise DecafException(f"function ident : {ident} has been declared as global variable")
    
        if ident not in self.nameInfo.funcDict:
            '''
            解决testcases/step9/later_decl.c
            '''
            newFunc = Func(ident, defined=False)
            # newParam = FuncParam(param)
            self.nameInfo.funcDict[ident] = newFunc #建立新的ident->func映射
            # self.nameInfo.paramDict[ident] = param
            # self.curFunc = newFunc

    def defFunc(self, ident):
        '''
        定义新函数
        '''
        if ident in self.nameInfo.funcDict:
            if self.nameInfo.funcDict[ident].defined: #语义检查：函数是否有重定义 
                raise DecafException(f"redefinition function : {ident}")
            #else:
                #已有声明, 但未定义
                #个数检查应该放到类型检查里了   
        newFunc = Func(ident, defined=True)
        # newParam = FuncParam(param)
        self.nameInfo.funcDict[ident] = newFunc #建立新的ident->func映射
        # self.nameInfo.paramDict[ident] = param
        self.curFunc = newFunc
    
    def defGloblVariable(self, var, ident, value):
        '''定义全局变量
        '''
        # declaration = ctx.globlDeclaration()
        # expr = declaration.expr()
        # value = None
        # if expr is not None:
        #     try:
        #         # print("value = ", expr.getText())
        #         value = int(expr.getText())
        #     except:
        #         raise DecafException("globl variable initial value must be Integer")
        # ident = declaration.atom().getText()
        # size = INT_BYTES
        # var = Variable(ident=ident, size=size, offset=None)

        if ident in self.nameInfo.funcDict:
            raise DecafException(f"global variable ident : {ident} has been declared as function")

        '''引入数组后再修改size
        offset初始化为None
        '''
        globlVar = GloblVar(var=var, value=value)
        if ident in self.nameInfo.globlDict:
            if self.nameInfo.globlDict[ident].value != None and value !=None:
                #都有初始值设置
                #注意这里必须通过!=None而不是!=0, 0也可以是正确的初值
                raise DecafException(f"redefinition of globl variable : {value}")
            elif value: #本次有初始值, 则说明原值一定没有初始值
                self.nameInfo.globlDict[ident].value = value 
        else: #首次visit
            '''
            与其他的声明语句不同的是
            没有把变量绑定到函数里, 只是
            1. 记录到作用域里，进行语义检查
            2. 记录到nameInfo的globs里 
            '''
            self.nameInfo.globlDict[ident] = globlVar #记录
            self.scopeNameList[ident] = var
            
    def defVariable(self, node, ident, size=1):
        '''
        定义新变量
        '''
        if self.scopeNameList.checkRedefinition(ident): #语义检查：变量是否有重定义
            raise DecafException(f"redefinition variable: {ident}")

        self.curFrameOffset += size
        variable = Variable(ident, size*INT_BYTES, -self.curFrameOffset*INT_BYTES)
        self.scopeNameList[ident] = variable
        self.curFunc.addVariable(node, variable) #到func中建立映射

    def useVariable(self, node):
        '''
        变量并不一定是在当前这个作用域中声明的
        因此应该在全部里面找
        '''
        # print("enter use variable ")
        # print(f"curFunc = {self.curFunc}")
        ident = node.getText()
        if ident not in self.scopeNameList:
            raise DecafException(f"undeclared variable: {ident}")
        variable = self.scopeNameList[ident]
        self.curFunc.addVariable(node, variable) #到func中建立映射
        # print("bind variable")
        # print(f"curFunc = {self.curFunc}")

    def enterScope(self, ctx):
        '''
        进入一个新的作用域
        '''
        self.scopeNameList.push() #新作用域的dict
        self.frameOffsetList.append(self.curFrameOffset) #保存上一个作用域的offset
        
    def exitScope(self, ctx):
        '''
        离开一个作用域
        '''
        self.curFunc.node2blocksize[ctx] = self.curFrameOffset - self.frameOffsetList[-1] #作差
        self.curFrameOffset = self.frameOffsetList.pop() #弹栈，恢复到上一个作用域的offset
        self.scopeNameList.pop()

    def getNameInfo(self):
        '''返回结果
        '''
        self.nameInfo.finish()
        return self.nameInfo
    