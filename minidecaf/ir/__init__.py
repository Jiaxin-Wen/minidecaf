from .IRGenerator import *
from .IRGenVisitor import IRGenVisitor
from .IRVisitor import IRVisitor


def toIR(nameInfo, typeInfo, tree):
    irGenerator = IRGenerator()
    IRGenVisitor(irGenerator, nameInfo, typeInfo).visit(tree)
    return irGenerator.getIR()