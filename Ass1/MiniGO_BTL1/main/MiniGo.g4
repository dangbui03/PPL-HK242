grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: newline* decllist EOF;

decllist: decl (SEMI decl)*;
decl: variable_decl newline | func_decl | struct_decl | const_decl | interface_decl;

// Variable declarations
variable_decl: VAR ID (ASSIGN expr)?;

// Constant declarations
const_decl: CONST ID ASSIGN expr SEMI;

interface_decl: ;

func_decl: ;

list_expr: expr COMMA list_expr | expr;

// Expressions
expr: or_expr;

or_expr : and_expr OR and_expr 
        | and_expr;

and_expr: rela_expr AND rela_expr
        | rela_expr;

rela_expr: add_expr REL add_expr 
        | add_expr;

add_expr: mul_expr (ADD | MINUS) mul_expr 
        | mul_expr;

mul_expr: unary_expr (MUL | DIV | MOD) unary_expr;

unary_expr: (NOT | MINUS) unary_expr | primary_expr;

primary_expr: literals 
            | ID 
            | LPAREN expr RPAREN 
            // | func_call 
            // | arr_lit
            // | struct_lit
            ;


REL: LT | GT | LE | GE | EQUAL | DIFF;

struct_decl: TYPE ID STRUCT LBRACE list_field RBRACE;
list_field: field newline? | field list_field newline?;
field: ID types SEMI;

// array literal
arr_lit: arr_type LBRACE list_expr RBRACE;

types : INT | FLOAT | STRING | BOOLEAN | arr_type | ID;
arr_type: arr_dim types | arr_dim;
arr_dim: LBRACK INT_LIT RBRACK;

literals: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT | NIL_LIT; //| ARR_LIT | STRUCT_LIT;
newline: '\r'? '\n';

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN : 'return';
FUNC: 'func';
TYPE:'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//TODO Operators 3.3.3 pdf
NOT: '!';
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
DIFF: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
OR: '||';
AND: '&&';
ASSIGN: '=';
ADD_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULT_ASSIGN: '*=';
DIV_ASSIGN: '/=';
REM_ASSIGN: '%=';
DOT: '.';  

//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
SEMI: ';';
COMMA: ',';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf
fragment DIGIT : [0-9] ;
fragment EXP : [eE] [+-]? DIGIT+ ;

// Floating-point Literals
FLOAT_LIT
    :   DIGIT+ '.' DIGIT* EXP?
    |   '.' DIGIT+ EXP?
    |   DIGIT+ EXP
    ;

// Integer Literals
DEC_LIT
    :   '0'
    |   [1-9] DIGIT*
    ;

BIN_LIT
    :   ('0b' | '0B') [01]+
        {
            self.text = str(int(self.text, 2))
        }
    ;

OCT_LIT
    :   ('0o' | '0O') [0-7]+
        {   
            self.text = str(int(self.text, 8))
        }
    ;

HEX_LIT
    :   ('0x' | '0X') [0-9a-fA-F]+
        {
            self.text = str(int(self.text, 16))
        }
    ;

INT_LIT
    :   DEC_LIT
    |   BIN_LIT
    |   OCT_LIT
    |   HEX_LIT
    ;

STR_LIT	: '"' ( ESCAPE_SEQ | ~['"\r\n\f\\])* '"'  {self.text = self.text[1:-1]};

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs 
LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;
BLOCK_COMMENT
    :   '/*' (BLOCK_COMMENT | .)*? '*/' -> skip
    ;

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ( ~[\f\r\n'"\\] | ESCAPE_SEQ )* ( EOF | '\n' | '\r\n') {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' ( ~[\r\n\\b'"] | ESCAPE_SEQ )* ([\r\\'] | IllegalEscape | [']~["]) {
	raise IllegalEscape(self.text[1:])
};
fragment IllegalEscape: '\\' ~[brnt'\\];
fragment ESCAPE_SEQ: '\\' [btnr'\\] | [']["];

//! ---------------- LEXER ----------------------- */