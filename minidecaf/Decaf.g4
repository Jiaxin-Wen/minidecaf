grammar Decaf;
import Lexer;

prog //根节点
    : progitem+ EOF
    ;

progitem
    : func # progFunc
    | declaration ';' # progDeclaration //全局变量
    ;

// //使用atom instead of Ident , to simply distinguish globl variable in ir generation
// globlDeclaration
//     :  ty atom ('=' expr)? //限制初始值只能是整形变量
//     ;

//区分函数声明和函数定义
func
    :ty Ident '(' parameterList ')' block # funcDefinition 
    |ty Ident '(' parameterList ')' ';' # funcDeclaration
    ;

//函数定义的参数
parameterList
    : (declaration (',' declaration)* )? 
    ;

ty //类型
    : Int # intType
    | ty '*' # ptrType
    ;

block
    : '{' blockitem* '}'
    ;

blockitem
    :stat # blockItemStat
    | declaration ';' # blockItemDecl
    ;

stat
    : 'return' expr ';' # returnStat
    | expr ';' # exprStat
    | 'if' '(' expr ')' thenBranch=stat ('else' elseBranch=stat)? # ifStat //设定优先级
    | block # blockStat //{作用域}
    | 'for' '(' pre=declaration ';' cond=expr? ';' post=expr? ')' stat # forDeclStat
    | 'for' '(' pre=expr? ';' cond=expr? ';' post=expr? ')' stat # forStat
    | 'while' '(' expr ')' stat # whileStat
    | 'do' stat 'while' '(' expr ')' ';' # doWhileStat //stat中已经引入了block
    | 'break' ';' # breakStat
    | 'continue' ';' # continueStat
    | ';' #emptyStat
    ;

declaration //声明
    : ty Ident ('[' Integer ']')* ('=' expr)? //包括数组, 但数组声明不能有初始值
    ;

expr 
    : assign
    ;

assign //赋值
    : conditional # tAssign
    | unary assignOP expr # cAssign
    ;

conditional
    : logicOr # tConditional
    | logicOr '?' expr ':' conditional # cConditional
    ;

logicOr //不要与已有or的冲突
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

add
    : mul # tAdd
    | add addOp mul # cAdd
    ;

mul
    : cast # tMul
    | mul mulOp cast # cMul
    ;
    
cast //类型转换
    : unary  # tCast
    | '(' ty ')' cast # cCast
    ;

unary
    : postfix # tUnary
    | unaryOp cast # cUnary
    ;

postfix
    : atom # tPostfix
    | Ident '(' argList ')' # postfixCall
    | postfix '[' expr ']' #postfixArray // 例如a[1+2]  这里需要检查一下越界
    ;

//函数调用的参数
argList
    : (expr ( ',' expr )* )?
    ;

atom
    : Integer # atomInteger
    | '(' expr ')' # atomExpr
    | Ident # atomIdent
    ;

//表示多个op的需要单独设节点
unaryOp
    : '-' | '!' | '~' | '*' | '&'
    ;

addOp
    : '+' | '-'
    ;

mulOp
    : '*' | '/' | '%'
    ;

relationOp
    : '<' | '>' | '<=' | '>='
    ;

equalOp
    : '==' | '!='
    ;

andOp
    : '&&'
    ;

orOp
    : '||'
    ;

assignOP
    : '='
    ;