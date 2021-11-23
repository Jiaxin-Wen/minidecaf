## 编原step6报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

step6是比较常规的step, 就是借助跳转指令实现了if else和三元表达式

#### (１) ir指令类添加

由于要借助跳转指令，因此需要一个Label做为入口地址，以及一个Branch指令用于实现跳转

```python
class Label(IRInstruction):
    '''定义一个label 用于地址跳转
    '''
    def __init__(self, label):
        self.label = label
	....
    
class Branch(IRInstruction):
    '''有条件/无条件跳转
    '''
    def __init__(self, op, label):
        assert op in branchOps
        self. op = op
        self.label = label
     ...
```

#### (２) IRGenVisitor中新增的重载

即针对新增的两个指令类，写visit函数, 并在他们的accept函数中调用

```python
    def visitLabel(self, ir):
    def visitBranch(self, ir):
```

#### (３) AsmGenVisitor中新增的重载

```python
    def visitLabel(self, ir):
        self.generator.append(label(ir.label)) #即增加一行 label: 

    def visitBranch(self, ir):
        self.generator.append(AsmAnnotation("branch"))
        self.generator.append(branch(ir.op, ir.label))
```

其中visitLabel的行为就是增加一行`label:`

值得一提的是branch的实现．

最初我本想按照实验指导书的指导，写许多if else语句来处理不同的branchOp

后来看了一下参考代码．参考代码将branch语句作为一个binary来实现,　非常优雅地实现了branch语句 

```python
@ir2asm
def branch(op, label):
    '''
    参考python实现:
    作为一个binary进行实现
    以branch2binary中的一项"br":(2, "beq")为例
    j label 等价于 beq 0, 0, label
    所以先push两个0, 再pop出来
    '''
    branch2binary = {"br":(2, "beq"),"beqz":(1, "beq"), "bnez":(1, "bne")}
    if op in branch2binary:
        num, op = branch2binary[op]
        return push(*[0]*num) + branch(op, label)
    return pop("t2", "t1") + [f"{op} t1,t2, {label}"]
```

### 2. 思考题

##### (1) Rust 和 Go 语言中的 if-else 语法与 C 语言中略有不同，它们都要求两个分支必须用大括号包裹起来，而且条件表达式不需要用括号包裹起来.请问相比 C 的语法，这两种语言的语法有什么优点？

通过大括号解决了if-else的语法二义性


### 3. 代码复用与借鉴

(1) 借鉴了实验指导书中的提示

(2) 借鉴了助教对branch的实现

