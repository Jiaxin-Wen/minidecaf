INT_BYTES = 4
MAX_INT = 1<<31-1

#一元
unaryOps = ['-', '!', '~', '&', '*']
unaryOpStrs = ["neg", 'lnot', "not", "addrof", "deref"]
unaryOpDict = {op: s for (op, s) in zip(unaryOps, unaryOpStrs)}

#二元
binaryCalOps = ['+','-','*','/','%']
binaryEqOps = ['==', '!=']
binaryRelOps = ['<','>']
binaryRaeOps = ['<=', '>=']
binaryLogicOps = ['&&', '||']
binaryOps = binaryCalOps + binaryEqOps + binaryRelOps + binaryRaeOps + binaryLogicOps
binaryOps = ['+', '-', '*', '/', '%', "==", "!=", "<", ">", "<=", ">=", "&&", "||"]
'''
一个版本给ir
一个版本给riscv
'''
binaryOpStrs = ["add", "sub", "mul", "div", "rem", "equal", "nequal", "lt", "gt", "le", "ge", "logicAnd", "logicOr"]
binaryOpAsmStrs = ["add", "sub", "mul", "div", "rem", "seqz", "snez", "slt", "sgt", "le", "ge", "land", "lor"]
binaryOpDict = {op: s for (op, s) in zip(binaryOps, binaryOpStrs)}
binaryOpAsmDict = {op:s for (op,s) in zip(binaryOps, binaryOpAsmStrs)}

branchOps = ["br", "beqz", "bnez", "beq", "bne"]

def flatten(ori_list):
    result = []
    for i in ori_list:
        result += i
    return result