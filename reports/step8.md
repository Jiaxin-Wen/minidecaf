## 编原step8报告

> 温佳鑫 计84 2017010335

### 1. 实验内容

实验指导书已经给了循环语句的定义方式和ir的生成方法, 这是本次实验中最重要的部分

##### 循环语句的统一定义

将循环语句统一定义为Loop(pre, cond, body, post)
pre: 初始化(可能有定义)
cond: 循环判断
body: 主体
post: 每次循环结束后执行的操作(只有for语句是有post的)

##### 循环语句的ir生成

按如下思路生成循环语句的IR
1. pre 的 IR
2. label BEGINLOOP_LABEL：开始下一轮迭代
3. cond 的 IR
4. beqz BREAK_LABEL：条件不满足就终止循环
5. body 的 IR
6. label CONTINUE_LABEL：continue 跳到这里
7. post 的 IR
8. br BEGINLOOP_LABEL：本轮迭代完成
 9. label BREAK_LABEL：条件不满足，或者 break 语句都会跳到这里

##### 其他

需要补充一下for循环新带来的作用域, 并用一个labelManager管理label


### 2. 思考题

##### (1) 将循环语句翻译成 IR 有许多可行的翻译方法，例如 while 循环可以有以下两种翻译方式. 从执行的指令的条数这个角度（label 指令不计算在内，假设循环体至少执行了一次），请评价这两种翻译方式哪一种更好？

![image-20201108160035067](/home/xw/desktop/minidecaf-2017010335/reports/pics/image-20201108160035067.png)

​	第二种翻译方式更好. 在本轮迭代完成后有一次检查.

​	举例而言, 考虑循环执行一次便退出的过程.

​	第一种方案需要依次执行cond, beqz, body, br, cond, beqz

​	第二种方案执行了cond, beqz, body后, 会先执行一个cond, 然后执行bnez.

### 3. 代码复用与借鉴

如1中提到的, 借鉴了实验指导书循环语句的定义方式和ir的生成方法

