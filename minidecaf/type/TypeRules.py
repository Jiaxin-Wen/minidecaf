from ..DecafException import DecafException
from .Types import *

def TypeCheck(rule):
    def wrapper(*tys):
        checkResult = rule(*tys)
        #print(f"{rule.__name__}, checkresult = {checkResult}")
        if checkResult is None:
            raise DecafException(f"Type Error: {rule.__name__}")
        elif type(checkResult) is str:  #rule返回了错误信息
            raise DecafException(f"Type Error: {checkResult}")
        else:
            return checkResult #Type
    return wrapper

def combineRule(*rules):
    @TypeCheck
    def wrapper(*tys):
        errorList = []
        for rule in rules:
            try:
                result =  rule(*tys)
                # print('rule : {} success, tyList = {}'.format(rule, *tys))
                # print('='*50)
                return result
            except DecafException as e:
                #print("rule : {} failed, message = {}".format(rule, e.message))
                errorList.append(e.message)
        #print('*'*50)
        return '\n'.join(errorList)
    return wrapper

@TypeCheck
def intRule(ty):
    '''循环用到的condition
    根据实验指导书, 条件表达式类型必须是 int，没有操作结果。
    '''
    if not isinstance(ty, Int):
        return f"wrong condition type : {ty}, int type expected"
    else:
        return Void()

@TypeCheck
def assignRule(tyL, tyR):
    '''赋值, 左右类型需要相同
    '''
    # print("tyL = {}, tyR = {}, flag = {}".format(tyL, tyR, tyL==tyR))
    if tyL != tyR:
        return f"cannot assign type {tyL} to type {tyR}"
    # elif isinstance(tyL, Array): #统一到LvalueManager中实现
    #     return f"cannot assign array"
    else:
        return tyL #赋值表达式类型

'''一元运算规则
'''
@TypeCheck
def intUnaryRule(ty):
    ''' ! / 
    '''
    if isinstance(ty, Int):
        return ty
    else:
        return f"unary op for int , but got {ty}"

#取地址
@TypeCheck
def addrOfRule(ty):
    if not isinstance(ty, Array):
        return Ptr(ty)
    else:
        return "cannot take address of array type"
#解引用

@TypeCheck
def derefRule(ty):
    #规则: 必须是指针类型
    if isinstance(ty, Ptr):
        return ty.baseType #返回解引用后的类型
    else:
        return f"dereference expect ptr, but got {ty}"

'''二元运算规则
'''
@TypeCheck
def intBinaryRule(tyL, tyR):
    if isinstance(tyL, Int) and isinstance(tyR, Int):
        return tyL
    else:
        return f"binary op for int , but got {tyL} and {tyR}"


@TypeCheck
def equalRule(tyL, tyR):
    if tyL == tyR and (isinstance(tyL, Int) or isinstance(tyL, Ptr)):
        return Int()
    else:
        return f"cannot equal type {tyL} with type {tyR}"

@TypeCheck
def relationRule(tyL, tyR):
    if isinstance(tyL, Int) and tyL == tyR: #只能比较int和int
        return Int()
    else:
        return f"cannot compare type {tyL} with type {tyR}"

#为了详细显示报错信息, 还是区分这些rule吧...
@TypeCheck
def returnRule(returnType, exprType):
    if returnType != exprType:
        return f"return {returnType} expected, but got {exprType}"
    else:
        return Void()


'''
三元表达式
'''
@TypeCheck
def condRule(cond, then, el):
    if isinstance(cond, Int) and then == el:
        return then


'''
指针相关
'''
@TypeCheck
def ptrArithRule(tyL, tyR):
    '''允许Int和Ptr做加减法法
    '''
    if isinstance(tyL, Int) and isinstance(tyR, Ptr):
        return tyR
    elif isinstance(tyL, Ptr) and isinstance(tyR, Int):
        return tyL
    else:
        return f"ptr arith, ptr and int expected, but got {tyL} and {tyR}"

@TypeCheck
def ptrMinusRule(tyL, tyR):
    '''允许Ptr和Ptr做减法
    '''
    if tyL == tyR and isinstance(tyL, Ptr):
        return Int()
    else:
        return f"same type ptr expected, but got {tyL}, {tyR}"

'''数组
'''
@TypeCheck
def arrayRule(arrayTy, indexTy):
    '''array必须是指针或数组
    index必须是int
    '''
    if not (isinstance(arrayTy,Array) or isinstance(arrayTy, Ptr)):
        return f"array type should be array or ptr , but got {arrayTy}"
    elif not isinstance(indexTy, Int):
        return f"index type should be Int,  but got {indexTy}"
    else:
        return arrayTy.baseType #按下标访问,返回数组元素的类型
