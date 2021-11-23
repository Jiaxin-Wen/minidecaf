from .AsmGenerator import AsmGenerator
from .AsmGenVisitor import AsmGenVisitor
from .AsmCode import *


def toAsm(ir):
    asmGenerator = AsmGenerator()
    AsmGenVisitor(asmGenerator).visit(ir)
    return asmGenerator.getAsm()