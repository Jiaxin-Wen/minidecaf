from .NameManager import *
from .NameVisitor import NameVisitor

def toNameInfo(tree):
    nameManager = NameManager()
    NameVisitor(nameManager).visit(tree)
    return nameManager.getNameInfo()