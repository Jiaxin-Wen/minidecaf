from ..utils import INT_BYTES

class Type:
    def __repr__(self):
        return self.__str__()


class Void(Type):
    def __init__(self):
        self.size = INT_BYTES

    def __eq__(self, other):
        return isinstance(other, Void)

    def __str__(self):
        return "void"


class Int(Type):
    def __init__(self):
        self.size = INT_BYTES

    def __eq__(self, other):
        # print('other type = ', type(other))
        # print("Int __eq__: flag = {}".format(isinstance(other, Int)))
        return isinstance(other, Int)

    def __str__(self):
        return 'int'


class Ptr(Type):
    def __init__(self, baseType):
        self.baseType = baseType
        self.size = INT_BYTES

    def __eq__(self, other):
        return isinstance(other, Ptr) and self.baseType == other.baseType

    def __str__(self):
        return f"{self.baseType}*"

class Array(Type):
    def __init__(self, baseType, len): 
        self.baseType = baseType
        self.len = len
        self.size = baseType.size * len
    
    def __str__(self):
        return f"{self.baseType}[{self.len}]"
    
    def __eq__(self, other):
        return isinstance(other, Array) and other.baseType == self.baseType and other.len == self.len
    
    @staticmethod
    def inflatten(base, dimenSizeList):
        '''构造多维数组
        '''
        for dimenSize in reversed(dimenSizeList): #逆序嵌套
            base = Array(base, dimenSize) #新增一层嵌套
        return base