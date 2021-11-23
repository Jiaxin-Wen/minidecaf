## 编原step3报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

#### (1) 更新g4文件

考虑到运算的优先级特性

把优先级较低的写在靠近树根节点的地方, 优先级较高的写在靠近树叶节点的地方, 这样在visit过程中就自动按照优先级完成了计算.

```
add
    : mul # tAdd
    | add addOp mul # cAdd
    ;

mul
    : unary # tMul
    | mul mulOp unary # cMul
    ;
```

#### (2) ir指令类添加

添加`Binary`类

#### (3) IRGenVisitor中新增的重载

```python
    def visitCAdd(self, ctx:DecafParser.CAddContext)
    def visitCMul(self, ctx:DecafParser.CMulContext):
```

同样, 先visitChildren, 将左右两个操作数压栈, 再将op压栈

#### (4) AsmGenVisitor中新增的重载

```python
    def visitBinary(self, ir):
        self.generator.append(binary(ir.op))
```

其中binary返回的汇编指令列表根据不同的二元操作符进行区分

> step3和step4我是一起做的, 这里就直接展示step4完成后的函数吧

```python
@ir2asm
def binary(op):
    '''
    先pop两次 取出两个操作数 完成计算 再将结果压栈
    '''
    if op in binaryCalOps: # + - * / %
        return pop("t2", "t1") + [f"{binaryOpAsmDict[op]} t1, t1, t2"] + push("t1")
    elif op in binaryEqOps: # == !=
        return pop("t2", "t1") + ["sub t1, t1, t2", f"{binaryOpAsmDict[op]} t1, t1"] + push("t1")
    elif op in binaryRelOps: #<  >
        return pop("t2", "t1") + [f"{binaryOpAsmDict[op]} t1, t1, t2"] + push("t1")
    elif op == "&&":
        return pop("t2") + unary("!") + push("t2") + unary("!") + binary("||") + unary("!")
    elif op == "||":
        return pop("t2", "t1") + ["or t1, t1, t2", "snez t1, t1"] + push("t1")
    elif op == "<=":
        return binary(">") + unary("!")
    elif op == ">=":
        return binary("<") + unary("!")
```

### 2. 思考题

1. 请给出将寄存器 `t0` 中的数值压入栈中所需的 riscv 汇编指令序列

   ```assembly
   add sp, sp, -4
   sw t0, 0(sp)
   ```

   请给出将栈顶的数值弹出到寄存器 `t0` 中所需的 riscv 汇编指令序列。

   ```assembly
   lw t0, 0(sp)
   add sp, sp, 4
   ```

2. (1) x86 g++ -O0编译 
    ![image-20201010215441858](/home/xw/pictures/typora_pic/image-20201010215441858.png)

  (2) qemu

  ![image-20201010215803639](/home/xw/pictures/typora_pic/image-20201010215803639.png)

### 3. 代码复用与借鉴

(1) 借鉴了实验指导书中的提示

