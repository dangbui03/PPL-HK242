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
variable_decl: VAR ID types? (ASSIGN)? list_expr SEMI? newline*;

// Constant declarations
const_decl: CONST ID types? ASSIGN list_expr SEMI? newline*;

// Struct declarations
struct_decl: TYPE ID STRUCT LBRACE newline* struct_fields RBRACE SEMI newline*;
struct_fields: struct_field SEMI ( newline* struct_field)*;
struct_field: ID types;

// method declarations
method_decl: FUNC;

interface_decl: TYPE ID INTERFACE newline* LBRACE  RBRACE SEMI newline*;

func_decl: FUNC;

// Statements
list_statement: statement list_statement | statement;
statement: 
	(
		declared_statement
		| assign_statement
	// 	| if_statement
	// 	| for_statement
	// 	| break_statement
	// 	| continue_statement
	// 	| call_statement
		| return_statement
	);

declared_statement: variable_decl newline;

assign_statement: lhs ass_operator expr;
lhs: arr_type | ID;
ass_operator: ':=' | '-='| '+=' | '*=' | '/=' | '%=';

return_statement: RETURN expr SEMI newline*;

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
            // | primary_expr DOT ID LPAREN? list_expr? RPAREN?
            | method_call
            | exprd 
            | func_call;
            // | primary_expr LBRACK ID RBRACK | arr_element

exprd: literals | ID | LPAREN expr RPAREN;

// [] [] ...
index_operator: LBRACK DEC_LIT RBRACK index_operator | LBRACK DEC_LIT RBRACK;

// function call & method call
func_call: ID LPAREN list_expr? RPAREN newline?; 
method_call: expr DOT ID LPAREN? list_expr? RPAREN?;

// types
types : primitive_types | composite_types;
primitive_types: INT | FLOAT | STRING | BOOLEAN | NIL;
composite_types: struct_type | interface_type;

// struct type & interface type & array type
struct_type: ID;
interface_type: ID;
arr_type: index_operator types;

// literal list
literal_list: literals COMMA literal_list | literals;
literals: int_lit | float_lit | str_lit | bool_lit | arr_lit | struct_lit;

// struct literal
struct_lit: ID LBRACE list_field? RBRACE;
list_field: field newline? | field COMMA list_field newline?;
field: ID COLON expr;

// array literal
arr_lit: arr_type LBRACE list_expr RBRACE;
arr_list: LBRACE arr_list? RBRACE | LBRACE expr COMMA arr_list? RBRACE;

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