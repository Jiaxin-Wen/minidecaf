## 编原step4报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

本次实验和step3非常相似, 

#### (1) 更新g4文件

考虑到运算的优先级特性

把优先级较低的写在靠近树根节点的地方, 优先级较高的写在靠近树叶节点的地方, 这样在visit过程中就自动按照优先级完成了计算.

```

logicOr 
    : logicAnd # tLogicOr
    | logicOr orOp logicAnd # cLogicOr
    ;

logicAnd
    : equal # tLogicAnd
    | logicAnd andOp equal # cLogicAnd
    ;

equal
    :  relation # tEqual
    | equal equalOp relation #cEqual
    ;

relation
    : add #tRelation
    | relation relationOp add # cRelation
    ;
```

#### (2) ir指令类添加

None

#### (3) IRGenVisitor中新增的重载

```python
 def visitCRelation(self, ctx:DecafParser.CRelationContext)
def visitCEqual(self, ctx:DecafParser.CEqualContext)
def visitCLogicOr(self, ctx:DecafParser.CLogicOrContext)
def visitCLogicAnd(self, ctx:DecafParser.CLogicAndContext)
```

同样, 先visitChildren, 将左右两个操作数压栈, 再将op压栈

#### (4) AsmGenVisitor中新增的重载

没有新增的重载函数

只是进一步完善了ir2asm的binary函数

> 新增操作符对应的汇编语句逻辑已经在step3的binary函数中一并汇报过了

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

##### (1) 在表达式计算时，对于某一步运算，是否一定要先计算出所有的操作数的结果才能进行运算？

   不是, 正如第2点中提到的短路求值, 对于一个逻辑或运算, 加入第一个操作数结果为真, 第二个操作数就不需要计算了.

##### (2) 在 MiniDecaf 中，我们对于短路求值未做要求，但在包括 C 语言的大多数流行的语言中，短路求值都是被支持的。为何这一特性广受欢迎？你认为短路求值这一特性会给程序员带来怎样的好处？

   短路求值的特性除了减少运算加快运行速度外, 也可以减少if的嵌套, 使得代码更加简洁.

   比如

   ```python
   if a != None:
       if a.value > 0:
           a.value += 1
   ```

   可以直接写成如下的形式，而不用担心a.value会崩掉

   ```python
   if a != None && a.value:
   	a.value += 1
   ```


### 3. 代码复用与借鉴

(1) 借鉴了实验指导书中的提示

(2) 借鉴了助教在riscv生成阶段对&&的处理

