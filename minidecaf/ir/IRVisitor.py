'''
提供接口给每条IRInstruction的accept函数中调用
后实现了IRVisitor的派生类 AsmGenVisitor 重载visit接口
'''

class IRVisitor:

    def visitAnnotation(self, ir):
        pass

    def visitConst(self, ir):
        pass

    def visitRet(self, ir):
        pass

    def visitUnary(self, ir):
        pass
    
    def visitBinary(self, ir):
        pass

    def visitPop(self, ir):
        pass
    
    def visitLoad(self, ir):
        pass

    def visitStore(self, ir):
        pass
    
    def visitFrameAddr(self, ir):
        pass

    def visitGloblAddr(self, ir):
        pass

    def visitLabel(self, ir):
        pass

    def visitBranch(self, ir):
        pass

    def visitCall(self, ir):
        pass

