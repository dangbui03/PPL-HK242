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

decllist: decl (decl | newline)*;

decl: variable_decl 
    | const_decl 
    | func_decl 
    | method_decl
    | struct_decl 
    | interface_decl 
    ;

// Variable declarations
variable_decl: VAR ID types? (ASSIGN list_expr)? SEMI newline*;

// Constant declarations
const_decl: CONST ID types? ASSIGN list_expr SEMI? newline*;

// Struct declarations
struct_decl: TYPE ID STRUCT LBRACE newline* struct_fields? RBRACE (SEMI | newline);
struct_fields: struct_field struct_fields | struct_field;
struct_field: ID (primitive_types | arr_type) SEMI newline* | ID composite_types SEMI? newline;

// method declarations
method_decl: FUNC LPAREN method_para RPAREN ID LPAREN list_para RPAREN types? block_statement newline*;
method_para: ID composite_types method_para | ID composite_types;

// interface declarations
interface_decl: TYPE ID INTERFACE newline* LBRACE newline* interface_method_list? RBRACE SEMI? newline*;
interface_method_list: interface_method interface_method_list | interface_method;
interface_method: ID LPAREN interface_para_list RPAREN types? SEMI? newline*; 
interface_para_list: interface_para COMMA interface_para_list | interface_para;
interface_para: ID types? |;

func_decl: FUNC ID LPAREN list_para RPAREN types? block_statement newline*;
list_para: para COMMA list_para | para;
para: ID types | ;

block_statement: LBRACE newline* list_statement? RBRACE newline*;

// Statements
list_statement: statement list_statement | statement;
statement: 
	(
		declared_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

// declared statement
declared_statement: variable_decl newline* | const_decl newline*;

// assign statement
assign_statement: lhs_list ass_operator expr SEMI? newline*;
lhs_list: lhs lhs_list | lhs;
lhs: arr_type | ID | ID DOT ID;
ass_operator: ':=' | '-='| '+=' | '*=' | '/=' | '%=';

// if statement
if_statement: IF LPAREN expr RPAREN newline* block_statement list_else_if_statement? else_statement? newline*;
list_else_if_statement: else_if_statement list_else_if_statement | else_if_statement;
else_if_statement: ELSE IF LPAREN expr RPAREN newline* block_statement;
else_statement: ELSE newline* block_statement;

// for statement
for_statement   : FOR list_expr newline* block_statement newline*
                | FOR assign_statement expr SEMI statement newline* block_statement newline*
                | FOR ID COMMA assign_statement expr newline* block_statement newline*
                ;

// break statement
break_statement: BREAK SEMI newline*;

call_statement: lhs LPAREN list_expr? RPAREN SEMI newline*;

continue_statement: CONTINUE SEMI newline*;

// return statement
return_statement: RETURN expr? SEMI? newline*;

// list_expr
list_expr: expr COMMA list_expr | expr;

// Expressions
expr    : expr OR and_expr 
        | and_expr;

and_expr: and_expr AND rela_expr
        | rela_expr;

rela_expr: rela_expr REL add_expr 
         | add_expr;
// relation
REL: LT | GT | LE | GE | EQUAL | DIFF;

add_expr: add_expr (ADD | MINUS) mul_expr 
        | mul_expr;

mul_expr: mul_expr (MUL | DIV | MOD) unary_expr 
        | unary_expr;

unary_expr  : (NOT | MINUS) unary_expr 
            | primary_expr;

primary_expr: primary_expr LBRACK expr RBRACK 
            | primary_expr DOT ID (LPAREN list_expr? RPAREN)?
            | func_call
            | exprd;
            // | 
            // | primary_expr LBRACK ID RBRACK | arr_element

exprd: literals | ID | LPAREN expr RPAREN | RANGE;

// function call & method call
func_call: ID LPAREN list_expr? RPAREN newline?; 
method_call: expr DOT ID LPAREN? list_expr? RPAREN?;

// types
types : primitive_types | composite_types | arr_type;
primitive_types: INT | FLOAT | STRING | BOOLEAN | NIL;
composite_types: struct_type | interface_type;

// struct type & interface type & array type
struct_type: ID;
interface_type: ID;
arr_type: index_operator types?;
index_operator: LBRACK int_lit RBRACK index_operator | LBRACK int_lit RBRACK;

// literal list
literals: int_lit | FLOAT_LIT | STR_LIT | bool_lit | arr_lit | struct_lit;

// struct literal
struct_lit: ID LBRACE list_field? RBRACE;
list_field: field newline? | field COMMA list_field newline?;
field: ID COLON expr;

// array literal
arr_lit: arr_type LBRACE arr_list? RBRACE;
arr_list: LBRACE arr_list | list_expr RBRACE? (COMMA arr_list)?;

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
fragment DIGIT : [0-9];
fragment EXP : [eE][+-]? DEC_LIT ;

// Integer Literals
DEC_LIT
    :   '0'
    |   [1-9] [0-9]*
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

// Floating-point Literals
FLOAT_LIT
    :  DEC_LIT ('.' [0-9]*)? EXP?;

STR_LIT	: '"' ( ESCAPE_SEQ | ~['"\r\n\f\\])* '"'  {self.text = self.text[1:-1]};

BOOL_LIT: TRUE | FALSE;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\b\r]+ -> skip; // skip spaces, tabs 
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