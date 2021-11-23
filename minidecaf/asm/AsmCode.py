class AsmCode:
    def __init__(self,s):
        self.s = s

class AsmLabel(AsmCode):
    #func:
    def __str__(self):
        return f"{self.s}:" #比"\t{}:".format()更好的写法

class AsmInstruction(AsmCode):
    def __str__(self):
        return f"\t{self.s}"

class AsmSection(AsmCode):
    def __str__(self):
        return f"\t{self.s}"

class  AsmAnnotation(AsmCode):
    def __str__(self):
        return f"\t\t\t\t#{self.s}"
