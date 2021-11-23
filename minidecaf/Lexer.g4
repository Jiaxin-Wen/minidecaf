lexer grammar Lexer;


//关键字
Int
    : 'int'
    ;

Return
    : 'return'
    ;

//标点、操作符
Lparen : '(' ;
Rparen : ')' ;
Lbrkt : '[' ;
Rbrkt : ']' ;
Lbrace : '{' ;
Rbrace : '}' ;
Comma : ',' ;
Semicolon : ';' ;

//fragment 辅助定义
fragment Digit:[0-9];
fragment InitalChar:[a-zA-Z_];
fragment SimpleChar:[0-9a-zA-Z_];

Integer
    : Digit+
    ;

Ident //函数名/变量名
    : InitalChar SimpleChar*
    ;

Whitespace
    : [ \t\n\r]+ -> skip
    ;