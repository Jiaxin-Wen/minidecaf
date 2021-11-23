## 编原step1报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

#### 1.1  g4文件编写 

通过编写g4文件, 可以在anltr工具的帮助下自动完成parser, lexer, visitor的自动构造。

我针对step1的需求，初步编写了`lexer.g4`, 和`Decaf.g4`。

- 对于lexer, 初步定义了step1中涉及到的关键字(int, return), 标点符号等。

- 对于parser, 我参考了python框架最终commit中`MiniDecaf.g4`的实现，将一个函数拆分为：返回类型 函数名 参数  函数体。并结合step1"仅一个return的main函数"的需求，做了初步的实现。

#### 1.2 中间码生成

//由于step1的语义检查非常简单，因此选择在中间码生成阶段直接实现。

基本的思路就是：通过重载antlr生成的visitor的函数，由语法树中节点的信息，生成中间码。进而在遍历parser生成的语法树的同时，完成全部中间码的生成。

针对这部分，我实现了三个脚本，分别为:

| 文件 | 类 | 功能 |
| --------------------- | ---- | ---- |
| ir/IRGenVisitor.py  | IRGenVisitor | visitor的派生类，通过重载visitXXX函数，监控语法树遍历过程，完成中间码生成 |
| ir/IRInstruction.py | Const, Ret | 定义了基本的ir指令，包括Const(压栈一个int), Ret(return)。 |
| ir/IRGenerator.py   | IRGenerator | 维护遍历语法树过程中生成的全部中间码，最终会由IRGenerator的接口返回中间码结果。 |

值得一提的有两点:

- 下一部分中我们会看到，IRInstruction.py中定义的指令类，通过实现accept函数，在中间码到汇编生成的实现中起到了重要的作用。

- IRGenerator中，我参考python框架定义了`IRFunc`和`IRProgram`，这使得中间码对于一个函数的表示变得更加简单、清晰。

```
进入函数时（即visit func节点时)，获得函数名，同时开始维护接下来生成的中间码，直到当前函数结束。
退出函数时（即visit return语句时)，利用函数名和函数体对应的中间码，构造一个IRFunc。
```

​    事实上最初我并没有这样做，但在解决函数名时才意识到了这样做的必要性。

#### 1.3 中间码到汇编

仿照中间码生成的思路：

(0) 给IR实现一个visitor,在IR指令类的accept函数(即上一点中提到的)中调用。

(1) 重载IRVisitor, 在遍历中间码的过程中，完成汇编代码的生成。

(2) 实现一个generator,用于维护生成的汇编代码。并提供接口返回汇编代码。

针对这部分，我实现了四个脚本，分别为:

| 文件              | 类                                            | 功能                                                         |
| ----------------- | --------------------------------------------- | ------------------------------------------------------------ |
| ir/IRVisitor.py   | IRVisitor                                     | 定义visitXX接口,在IR指令类中调用，供汇编码生成时重载         |
| asm/AsmGenVisitor | AsmGenVisitor                                 | IRVisitor的派生类，通过重载visitXX函数，监控中间码遍历过程, 完成汇编生成 |
| asm/AsmGenerator  | AsmGenerator                                  | 维护遍历中间码过程中生成的全部汇编代码，最终会提供接口返回汇编代码结果。 |
| asm/AsmCode       | AsmCode, AsmLabel, AsmSection, AsmInstruction | 定义了基本的汇编指令, 通过实现str函数,针对指令特点定义格式。 |

   值得一提的有两点:

- 首先是仿照中间码生成，派生visitor的思路，使得根据每条中间码生成汇编代码的过程简单、清晰。采用if判断在扩展或修改时将是非常麻烦的。
- visitXX重载时,参考python实现, 使用了装饰器，有效地避免了代码重复。

### 2. 思考题

1. 修改 minilexer 的输入（`lexer.setInput` 的参数），使得 lex 报错，给出一个简短的例子。

   ```c
       int main() {
           return !123;
       }
   ```

2. 修改 minilexer 的输入，使得 lex 不报错但 parse 报错，给出一个简短的例子。

   ```c
       int main() {
           return {123;
       }
   ```

3. 在 riscv 中，哪个寄存器是用来存储函数返回值的？

   ra

### 3. 代码复用与借鉴

我没有复用代码，仅借鉴了参考代码的设计思想。

我认为最主要的借鉴可以概括为以下两点:

#####　(1) visitor模式的使用

 虽然visitor的使用在IRGenVisitor时还是十分自然的，但在由中间码生成汇编代码阶段，我第一时间没有想到visitor模式的使用。后来参考了

助教的python实现，非常优美的解决了这个问题。

##### (2) generator的使用

我最初的想法是在visitor中直接维护生成的中间码，但感觉这样的visitor并不符合单一责任原则，太过复杂了。于是参考了助教的python实现，单独实现generator,辅助visitor。