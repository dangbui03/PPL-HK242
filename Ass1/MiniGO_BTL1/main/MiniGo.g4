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

program: newline* decllist  EOF;

decllist: decl (decl | newline)*;

decl: variable_decl 
    | const_decl 
    | func_decl 
    | struct_decl 
    | interface_decl 
    | method_decl;

// Variable declarations
variable_decl: VAR ID (ASSIGN expr)? types? SEMI?;

// Constant declarations
const_decl: CONST ID ASSIGN expr types? SEMI?;

// Struct declarations
struct_decl: TYPE ID STRUCT LBRACE struct_fields RBRACE;
struct_fields: struct_field SEMI ( newline* struct_field)*;
struct_field: ID types;

// method declarations
method_decl: FUNC;

interface_decl: TYPE ID INTERFACE LBRACE  RBRACE;

func_decl: FUNC;

// Statements
// list_statement: statement list_statement | statement;
// statement: ;
	// (
	// 	declared_statement
	// 	| assign_statement
	// 	| if_statement
	// 	| for_statement
	// 	| break_statement
	// 	| continue_statement
	// 	| call_statement
	// 	| return_statement
	// );

// list_expr
list_expr: expr COMMA list_expr | expr;

// Expressions
expr    : expr OR and_expr 
        | and_expr;

and_expr: and_expr AND rela_expr
        | rela_expr;

rela_expr: rela_expr REL add_expr 
         | add_expr;

add_expr: add_expr (ADD | MINUS) mul_expr 
        | mul_expr;

mul_expr: mul_expr (MUL | DIV | MOD) unary_expr 
        | unary_expr;

unary_expr  : (NOT | MINUS) unary_expr 
            | primary_expr;

primary_expr: exprd
            | arr_element
            | func_call 
            | method_call
            | arr_lit
            | struct_lit
            | LBRACK ID RBRACK
            ;

exprd: literals | ID | ID? LPAREN list_expr? RPAREN;
func_expr: func_call | exprd;

index_operator: LBRACK list_expr RBRACK | LBRACK list_expr RBRACK index_operator;
args: literal_list | ;

arr_element: func_expr index_operator;

// function call
func_call: ID LPAREN args RPAREN;

// method call
method_call: (func_expr | arr_element) DOT list_expr LPAREN? args RPAREN? method_call | (func_expr | arr_element) DOT list_expr LPAREN? args RPAREN? ;

// relation
REL: LT | GT | LE | GE | EQUAL | DIFF;



arr_lit: arr_type LBRACE list_expr RBRACE;

// struct literal
struct_lit: ID LBRACE list_field? RBRACE;
list_field: field newline? | field COMMA list_field newline?;
field: ID COLON expr;

// array literal


// types
types : primitive_types | composite_types;
primitive_types: INT | FLOAT | STRING | BOOLEAN ;
composite_types: struct_type | interface_type;

// struct type
struct_type: ID;

// interface type
interface_type: ID;

// array type
arr_type: arr_dim arr_type | arr_dim types;
arr_dim: LBRACK (DEC_LIT)? RBRACK; // const_decl

// literal list
literal_list: literals COMMA literal_list | literals;
literals: int_lit | float_lit | str_lit | bool_lit | nil_lit;
int_lit     
        :   DEC_LIT
        |   BIN_LIT
        |   OCT_LIT
        |   HEX_LIT
        ;
float_lit: FLOAT_LIT;
bool_lit: TRUE | FALSE;
str_lit: STR_LIT;

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
COLON: ':';

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
fragment EXP : [eE] [+-]? DEC_LIT ;

// Floating-point Literals
FLOAT_LIT
    :  DEC_LIT ('.' DIGIT*)? EXP?;


// Integer Literals
DEC_LIT
    :   '0'
    |   [1-9] DIGIT*
    ;

BIN_LIT
    :   ('0b' | '0B') [01]+
        {
            self.text = str(int(self.text[2:], 2))
        }
    ;

OCT_LIT
    :   ('0o' | '0O') [0-7]+
        {   
            self.text = str(int(self.text[2:], 8))
        }
    ;

HEX_LIT
    :   ('0x' | '0X') [0-9a-fA-F]+
        {
            self.text = str(int(self.text[2:], 16))
        }
    ;

STR_LIT	: '"' ( ESCAPE_SEQ | ~['"\r\n\f\\])* '"'  {self.text = self.text[1:-1]};

BOOL_LIT: TRUE | FALSE;
nil_lit: NIL;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs 
LINE_COMMENT
    :   '//' ~[\n\r]* -> skip
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