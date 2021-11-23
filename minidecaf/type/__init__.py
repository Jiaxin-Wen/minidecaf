from .TypeManager import *
from .TypeVisitor import TypeVisitor


def toTypeInfo(nameInfo, tree):
    typeManager = TypeManager()
    TypeVisitor(nameInfo, typeManager).visit(tree)
    return typeManager.getTypeInfo()