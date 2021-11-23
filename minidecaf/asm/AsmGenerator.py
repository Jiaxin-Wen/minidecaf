from .AsmCode import *

class AsmGenerator:
    '''
    生成risc-v代码
    '''
    def __init__(self):
        self.asmList = []
    
    def append(self, code):
        if isinstance(code,list):
            self.asmList += code
        else:
            self.asmList.append(code)
    
    def getAsm(self):
        return"\n".join(map(str, self.asmList))


