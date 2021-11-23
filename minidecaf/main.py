"""实例：真·main"""


from antlr4 import *
from .DecafLexer import DecafLexer
from .DecafParser import DecafParser
from .ir import toIR
from .asm import toAsm
from .name import toNameInfo
from .type import toTypeInfo
import sys



def toFile(path,asm):
    with open(path,'w') as file:
            file.write(asm)

def toStdout(asm):
        print(asm)

def main(argv):
    input_path = argv[1]
    input = FileStream(input_path)
    lexer = DecafLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = DecafParser(tokens)
    parser._errHandler = BailErrorStrategy()
    tree = parser.prog()
    nameInfo = toNameInfo(tree)
    # print("name = ")
    # print(nameInfo)
    # print("="*50)
    typeInfo = toTypeInfo(nameInfo, tree)
    ir = toIR(nameInfo, typeInfo, tree)
    asm = toAsm(ir)
    # print(tree.toStringTree(recog=parser))
    # print('='*100)
    # for node, var in nameInfo.items():
    #     print(f"node = {node}, offset = {var.offset}")
    # print('='*50)

    # print('ir = ')
    # print(ir)
    # print('='*50)
    # print('asm = ')
    print(asm)
    # if len(argv) >= 3:
    #     toFile(output_path,asm)
    # else:
    #     toStdout(asm)


    return 0
    


if __name__ == "__main__":
        main()