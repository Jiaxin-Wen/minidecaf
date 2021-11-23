## 编原step2报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

step1已经实现了基础的框架.

因此本次更新只需在step1的基础上, 根据新功能的要求, 更新以下几处

1. 更新g4文件: 修改或加入新的规则
2. 根据需要, 添加新的ir指令类
3. 根据需要, 重载g4文件修改后产生的新`visitXXX`函数, 进而更新ir生成的逻辑
4. 根据需要, 在`IRVisitor`中添加新的`visitXXX`函数,到`AsmGenVisitor`中重载, 进而更新ir到asm生成的逻辑

接下来我也会按照这几点来汇报

#### (1) 更新g4文件

参照实验指导书, 加入unary.

考虑到一元运算符有多个, 所以选择单独用一个unaryOp来表示, 代码中根据这个节点具体的text来区分操作.

```
unary
    : atom # tUnary
    | unaryOp unary # cUnary
    ;
    
unaryOp
    : '-' | '!' | '~' | '*' | '&'
    ;
```

#### (2) ir指令类添加

添加`Unary`类

#### (3) IRGenVisitor中新增的重载

```python
    def visitCUnary(self, ctx:DecafParser.UnaryContext):
        op = ctx.unaryOp().getText()
        self.visitChildren(ctx) #先压栈操作数
        self.generator.append(Unary(op))
```

#### (4) AsmGenVisitor中新增的重载

```python
    def visitUnary(self, ir):
        self.generator.append(unary(ir.op))
```

其中unary返回的汇编指令列表依次做了:

将操作数从栈中弹出, 根据op, 得到计算结果, 更新寄存器的值, 再压栈. 即

```python
@ir2asm
def unary(op):
    op = {'-':'neg', '~': 'not', '!': 'seqz'}[op]
    codeStrList = pop("t1") + [f"{op} t1, t1"] + push("t1")
    return codeStrList
```

### 2. 思考题

-~2147483647

### 3. 代码复用与借鉴

借鉴了实验指导书中的提示

借鉴了助教参考代码中, _pop和pop的命名方法(感觉很妙