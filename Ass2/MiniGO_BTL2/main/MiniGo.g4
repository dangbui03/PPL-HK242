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

    if tk == self.NEWLINE:
        if self.preType == self.NEWLINE:
            return None
        else:
            return super().emit();

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

program: NEWLINE* declared (declared | NEWLINE)* EOF;

declared:
	variables_declared
	| constants_declared
	| function_declared
	| method_declared
	| struct_declared
	| interface_declared;

variables_declared: VAR ID (TYPE_LIT|array_type)? ID? (ASSIGN list_expression)? SEMI NEWLINE*;

constants_declared: CONST ID TYPE_LIT? ASSIGN list_expression (SEMI|NEWLINE) NEWLINE*;

list_array: LBRACE list_literal? RBRACE;
list_literal: literal COMMA list_literal |LBRACE literal LBRACE;

function_declared: FUNC ID LPAREN list_func? RPAREN (array_type | TYPE_LIT)? block_statement NEWLINE*;
list_func: ID (array_type | TYPE_LIT) COMMA list_func | ID (array_type | TYPE_LIT);

method_declared: FUNC LPAREN ID ID RPAREN ID LPAREN list_method? RPAREN (array_type | TYPE_LIT)? ID? block_statement NEWLINE*;
list_method: method COMMA list_method| method;
method: ID (TYPE_LIT|array_type|ID)?;

struct_declared: TYPE ID STRUCT LBRACE NEWLINE* struct_body RBRACE;
struct_body: struct_element struct_body| struct_element;
struct_element: (ID (array_type | TYPE_LIT ) SEMI? NEWLINE*) | ID ID SEMI? NEWLINE;

interface_declared: TYPE ID INTERFACE LBRACE NEWLINE* interface_body RBRACE;
interface_body: interface_element interface_body| interface_element;
interface_element: ID LPAREN list_parameters? RPAREN (TYPE_LIT|array_type|ID)? SEMI? NEWLINE*;

list_parameters: list_para_temp?;
list_para_temp: parameter COMMA list_para_temp| parameter;
parameter: ID (TYPE_LIT|array_type|ID)?;

array_type: array_elements (ID|TYPE_LIT)?;

block_statement
    : LBRACE NEWLINE* list_statement RBRACE SEMI?
    ;
//TODO Statement 5 and 4 pdf
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
declared_statement:NEWLINE* declared;
lhs: ID list_lhs;
list_lhs: (DOT ID | LBRACK expression RBRACK) list_lhs | ;
assign_statement
    : lhs (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | REM_ASSIGN | DOT_ASSIGN) expression SEMI? NEWLINE*
    ;

if_statement
    : IF LPAREN expression RPAREN NEWLINE* block_statement NEWLINE* list_elif? else_statement? NEWLINE*;
list_elif: else_if_statement list_elif | else_if_statement;
else_if_statement: ELSE IF LPAREN expression RPAREN NEWLINE* block_statement NEWLINE*;
else_statement: ELSE NEWLINE* block_statement NEWLINE*;

for_statement
    : FOR expression block_statement NEWLINE*
    | FOR for_init SEMI expression SEMI update_expr block_statement NEWLINE*
    | FOR ID COMMA ID DOT_ASSIGN RANGE expression block_statement NEWLINE*
    ;
for_init
    : VAR ID array_type? (ASSIGN expression)?                
    | ID (DOT_ASSIGN | ASSIGN) expression        
    ;
update_expr
    : ID array_type? (ADD_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | REM_ASSIGN | DOT_ASSIGN) expression
    ;

break_statement
    : BREAK (SEMI| NEWLINE) NEWLINE*
    ;

continue_statement
    : CONTINUE (SEMI| NEWLINE) NEWLINE*
    ;

call_statement
    : lhs LPAREN list_expression? RPAREN (SEMI| NEWLINE) NEWLINE*
    ;

return_statement
    : RETURN expression? (SEMI| NEWLINE) NEWLINE*
    ;
//TODO Literal 6.6 pdf
literal:
	DEC_LIT
    | BIN_LIT
    | HEX_LIT
    | OCT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| array_literal
	| struct_literal;

TYPE_LIT: INT | FLOAT | STRING | BOOLEAN | NIL;
array_literal: array_elements (TYPE_LIT|ID) LBRACE nested_array RBRACE;
array_elements: LBRACK DEC_LIT RBRACK array_elements | LBRACK DEC_LIT RBRACK;
nested_array: LBRACE nested_array | list_expression RBRACE? (COMMA nested_array)?;

struct_literal: ID LBRACE list_elements? RBRACE;
list_elements: ID COLON expression COMMA list_elements | ID COLON expression;

// TODO 5.2 Expressions 6 pdf
list_expression: expression COMMA list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | DIFF | LT | LE | GT | GE) expression3 | expression3;
expression3: expression3 (ADD | MINUS) expression4| expression4;
expression4: expression4 (MULT | DIV | REM) expression5 | expression5;
expression5: (FACT | MINUS) expression5 | expression6;
expression6: expression6 LBRACK expression RBRACK | expression6 DOT ID (LPAREN (list_expression)? RPAREN)? | primary_expression;
primary_expression: ID LPAREN (list_expression)? RPAREN | LPAREN expression RPAREN | ID | literal | RANGE;
// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

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
ADD: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
REM: '%';
EQUAL: '==';
DIFF: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
OR: '||';
FACT: '!';
AND: '&&';
ASSIGN: '=';
ADD_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULT_ASSIGN: '*=';
DIV_ASSIGN: '/=';
REM_ASSIGN: '%=';
DOT: '.'; 
DOT_ASSIGN: ':=';  
//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
SEMI: ';';
COMMA: ',';
COLON: ':';
//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf
// INT_LIT: [0-9];
DEC_LIT: '0'|[1-9][0-9]* ;
BIN_LIT: ('0b'|'0B') [01]+ ;
OCT_LIT: ('0o'|'0O') [0-7]+ ;
HEX_LIT: ('0x'|'0X') [0-9a-fA-F]+ ;
FLOAT_LIT: ([0-9][0-9]*)('.' [0-9]*)( [eE][+-]?([0-9][0-9]*))?;

STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ~[\t\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt"\\];   
fragment ESC_ILLEGAL: [\r] | '\\' ~[rnt'\\];
//TODO skip 3.1 and 3.2 pdf
COMMENT: '/*' (COMMENT | .)*? '*/' -> skip;
SEMICOLON_NEWLINE:
    ';'
    | '\r'? '\n' {
    tk = self.preType;
    if (tk):
        self.emit();
    else:
        self.skip()
};
// Whitespace
WS: [ \f\b\t\r]+ -> skip;
//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[1:])
};

//! ---------------- LEXER ----------------------- */