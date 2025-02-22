// 2153289 - Bùi Hồ Hải Đăng
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;

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

//! Parser rules
program: newline* decllist EOF;

decllist: decl decllist newline* 
        | decl newline*;

decl: variable_decl 
    | const_decl 
    | func_decl 
    | method_decl
    | struct_decl 
    | interface_decl 
    ;

// Variable declarations
// variable_decl: VAR ID types? (types ASSIGN list_expr)? SEMI;//(SEMI | newline) newline*;
variable_decl: VAR ID ( types (ASSIGN list_expr)? | ASSIGN list_expr ) (SEMI | newline) newline*;


// Constant declarations
const_decl: CONST ID types? ASSIGN list_expr (SEMI | newline) newline*;

// Struct declarations
struct_decl: TYPE ID STRUCT newline? LBRACE SEMI* struct_fields RBRACE SEMI+;//(SEMI | newline) newline*;
struct_fields: struct_field struct_fields | struct_field;
struct_field: ID types SEMI;//(SEMI | newline) newline*; ID (primitive_types | arr_type) SEMI newline* | ID composite_types (SEMI | newline) newline*;

// method declarations
method_decl: FUNC LPAREN method_para_list RPAREN ID LPAREN list_para RPAREN types? block_statement (SEMI | newline) newline*;
method_para_list: method_para method_para_list | method_para;
method_para: ID composite_types;

// interface declarations
interface_decl: TYPE ID INTERFACE newline? LBRACE SEMI* interface_method_list RBRACE SEMI;//(SEMI | newline) newline*;
interface_method_list: interface_method interface_method_list | interface_method;
interface_method: ID LPAREN interface_para_list RPAREN types? (SEMI | newline) newline*; 
interface_para_list: interface_para COMMA interface_para_list | interface_para | ;
interface_para: ID types?;

func_decl: FUNC ID LPAREN list_para RPAREN types? block_statement (SEMI | newline)? newline*;
list_para: para COMMA list_para | para | ;
para: ID types?;

block_statement: LBRACE SEMI* list_statement? SEMI* RBRACE ;

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
declared_statement: decl newline*;//variable_decl newline* | const_decl newline*;

// assign statement
assign_statement: lhs ass_operator expr SEMI? newline*;
// lhs: ID lhs_list;
// lhs_list: (DOT | index_operator | ID) lhs_list | ;
// lhs2: ID (DOT ID)? index_operator? ;
lhs: ID 
    | lhs DOT ID 
    | lhs LBRACK expr RBRACK ;
// lhs_list: lhs lhs_list | lhs;
ass_operator: COL_ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | REM_ASSIGN;

// if statement
if_statement: IF LPAREN expr RPAREN SEMI* block_statement list_else_if_statement? else_statement? (SEMI | newline) newline*;
list_else_if_statement: else_if_statement list_else_if_statement | else_if_statement;
else_if_statement: ELSE IF LPAREN expr RPAREN SEMI* block_statement SEMI*;
else_statement: ELSE newline* block_statement;

// for statement
for_statement   : FOR expr newline* block_statement (SEMI | newline) newline*
                | FOR init_for_statement SEMI expr SEMI update_stament newline* block_statement (SEMI | newline)* newline*
                | FOR ID COMMA value_assign expr newline* block_statement (SEMI | newline)* newline*
                ;

init_for_statement  : VAR ID types? ASSIGN expr
                    | ID (':=' | ASSIGN) expr 
                    ;
// init_for_statement  : assign_statement | variable_decl;
update_stament: ID ass_operator expr;

value_assign: ID ':=' RANGE;

// break statement
break_statement: BREAK (SEMI | newline) newline*;

call_statement: lhs LPAREN list_expr? RPAREN (SEMI | newline)* newline*;

continue_statement: CONTINUE (SEMI | newline) newline*;

// return statement
return_statement: RETURN expr? (SEMI | newline) newline*;

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
            | exprd 
            ;

exprd: literals | ID | LPAREN expr RPAREN;

// function call & method call
func_call: ID LPAREN list_expr? RPAREN newline?; 
method_call: DOT ID (LPAREN list_expr? RPAREN)?;

// types
types : primitive_types | composite_types | arr_type;
primitive_types: INT | FLOAT | STRING | BOOLEAN;
composite_types: struct_type | interface_type;

// struct type & interface type & array type
struct_type: ID;
interface_type: ID;
arr_type: index_operator types?;
index_operator: LBRACK (DEC_LIT | struct_type) RBRACK index_operator | LBRACK (DEC_LIT | struct_type) RBRACK;

// literal list
literals: int_lit | float_lit | str_lit | bool_lit | arr_lit | struct_lit | nil_lit;

// struct literal
struct_lit: ID LBRACE list_field? RBRACE;
list_field: field newline? | field COMMA list_field newline?;
field: ID COLON expr;

// array literal
arr_lit: arr_type LBRACE arr_list RBRACE;
// arr_list: LBRACE arr_list | list_expr RBRACE? (COMMA arr_list)?;
arr_list: LBRACE* arr_ele RBRACE* | LBRACE* arr_ele RBRACE* COMMA arr_list;
arr_ele: literals | struct_type;

int_lit     
        :   DEC_LIT
        |   BIN_LIT
        |   OCT_LIT
        |   HEX_LIT
        ;
float_lit: FLOAT_LIT;
bool_lit: TRUE | FALSE;
str_lit: STR_LIT;
nil_lit: NIL;

newline: NEWLINE;

//! Lexer rules
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
COL_ASSIGN: ':=';
DOT: '.';  
COLON: ':';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
SEMI:
    ';'
    | '\r'? '\n' {
        if self.preType in {self.ID, self.DEC_LIT, self.BIN_LIT, self.OCT_LIT, self.HEX_LIT, self.FLOAT_LIT,
                         self.STR_LIT, self.TRUE, self.FALSE, self.NIL, self.INT, self.FLOAT,
                         self.STRING, self.BOOLEAN, self.RETURN, self.CONTINUE, self.BREAK,
                         self.RPAREN, self.RBRACK, self.RBRACE, self.LBRACE, self.LBRACK}:
            self.type = self.SEMI;
            self.text = ";";
            self.channel = 0;
        else:
            self.skip();
    };

COMMA: ',';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

fragment DIGIT : [0-9][0-9]*;
fragment EXP : [eE][+-]? DIGIT ;

// Integer Literals
DEC_LIT
    :   '0'
    |   [1-9] [0-9]*
    ;

BIN_LIT
    :   ('0b' | '0B') [01]+
        // {
        //     self.text = str(int(self.text[2:], 2))
        // }
    ;

OCT_LIT
    :   ('0o' | '0O') [0-7]+
        // {   
        //     self.text = str(int(self.text[2:], 8))
        // }
    ;

HEX_LIT
    :   ('0x' | '0X') [0-9a-fA-F]+
        // {
        //     self.text = str(int(self.text[2:], 16))
        // }
    ;

NEWLINE: '\r'? '\n' -> skip ; // Newlines

// Floating-point Literals
FLOAT_LIT
    :  DIGIT ('.' [0-9]*) EXP?;

STR_LIT	: '"' ( ESCAPE_SEQ | ~['"\r\t\n\\])* '"'  {self.text};

BOOL_LIT: TRUE | FALSE;

WS: [ \t\f\b\r]+ -> skip; // skip spaces, tabs 
LINE_COMMENT
    :   '//' ~[\n\r]* -> skip
    ;
BLOCK_COMMENT
    :   '/*' (BLOCK_COMMENT | .)*? '*/' -> skip
    ;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ( ~[\t\r\n'"\\] | ESCAPE_SEQ )* ( EOF | '\n' | '\r\n') {
    if(len(self.text) >= 2 and self.text[-1] == '\n'):
        raise UncloseString(f"{self.text[:-1]}")
    else:
        raise UncloseString(f"{self.text}")
};

ILLEGAL_ESCAPE: '"' ( ~[\t\r\n\\'"] | ESCAPE_SEQ )* ([\r\\'] | IllegalEscape | [']~["]) {
	raise IllegalEscape(self.text)
};
fragment IllegalEscape: '\\' ~[rnt"\\];
fragment ESCAPE_SEQ: '\\' [tnr"\\] ;