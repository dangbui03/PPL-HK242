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

program: NEWLINE* declared (declared | NEWLINE)* EOF;
declared:
	variables_declared
	| constants_declared
	| function_declared
	| method_declared
	| struct_declared
	| interface_declared;

variables_declared: VAR ID TYPE_LIT? ASSIGN? list_expression SEMI NEWLINE*;

constants_declared: CONST ID TYPE_LIT? ASSIGN list_expression SEMI NEWLINE*;

function_declared: FUNC ID LPAREN list_parameters RPAREN (array_type | TYPE_LIT)? block_statement NEWLINE*;

method_declared: FUNC LPAREN ID ID RPAREN ID LPAREN list_parameters RPAREN (array_type | TYPE_LIT)? ID? block_statement NEWLINE*;

struct_declared: TYPE ID STRUCT LBRACE NEWLINE* struct_body? RBRACE NEWLINE*;
struct_body: struct_element struct_body| struct_element;
struct_element: ID (array_type | TYPE_LIT) SEMI NEWLINE;

interface_declared: TYPE ID INTERFACE LBRACE NEWLINE* interface_body? RBRACE NEWLINE*;
interface_body: interface_element interface_body| interface_element;
interface_element: ID LPAREN list_parameters RPAREN (TYPE_LIT|array_type)? SEMI? NEWLINE*;

list_parameters: list_para_temp?;
list_para_temp: parameter COMMA list_para_temp| parameter;
parameter: ID (TYPE_LIT|array_type)?;

array_type: array_elements ID;

block_statement
    : LBRACE NEWLINE* list_statement? RBRACE
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
assign_statement
    :NEWLINE* expression (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | REM_ASSIGN | DOT_ASSIGN) expression SEMI? NEWLINE*
    ;

if_statement
    :NEWLINE* IF LPAREN expression RPAREN block_statement else_if_statement? else_statement? NEWLINE*;
else_if_statement: ELSE IF LPAREN expression RPAREN block_statement;
else_statement: ELSE block_statement;

for_statement
    : FOR expression block_statement NEWLINE*        // Vòng lặp điều kiện duy nhất
    | FOR statement expression SEMI statement block_statement NEWLINE*             // Vòng lặp truyền thống
    | FOR ID COMMA statement expression block_statement NEWLINE*                   // Vòng lặp kiểu range
    ;
range_for
    : ID COMMA ID ASSIGN RANGE expression
    ;

break_statement
    : BREAK SEMI NEWLINE*
    ;

continue_statement
    : CONTINUE SEMI NEWLINE*
    ;

call_statement
    : expression LPAREN list_expression? RPAREN SEMI NEWLINE*
    ;

return_statement
    : RETURN (expression SEMI)? NEWLINE*
    ;
//TODO Literal 6.6 pdf
literal:
	DEC_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| array_literal
	| struct_literal;

TYPE_LIT: INT | FLOAT | STRING | BOOLEAN | NIL ;
array_literal: array_elements TYPE_LIT LBRACE nested_array RBRACE;
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
primary_expression: ID? LPAREN (list_expression)? RPAREN | ID | literal | RANGE;

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
DOT_ASSIGN: ':=';
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
COLON: ':';
//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf
BOOL_LIT: TRUE|FALSE;
DEC_LIT: [1-9] [0-9]* | '0'; // Leading zeros are disallowed unless it's '0'
BIN_LIT: ('0b' | '0B') [01]+ 
{
    self.text = str(int(self.text[2:], 2))
};

OCT_LIT: ('0o' | '0O') [0-7]+ 
{
    self.text = str(int(self.text[2:], 8))
};

HEX_LIT: ('0x' | '0X') [0-9a-fA-F]+ 
{
    self.text = str(int(self.text[2:], 16))
};
FLOAT_LIT: [0-9]+ ('.' [0-9]*)? ([eE] [+-]? [0-9]+)?;

// String Literals
STRING_LIT: '"' (~[\r\n\\"] | '\\' [brnt"\\])* '"' {self.text = self.text[1:-1]};
NEWLINE: [\n];
COMMENTS: '//' ~[\n\r]* -> skip; // Comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip; // Nested comments
// Whitespace
WS: [ \f\b\t\r]+ -> skip;

// Error Handling
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"'(~[\r\n\\"] | '\\' [brnt"\\] )* ('\r' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (~[\r\n\\"] | '\\' [brnt"\\] )* '\\' ~[brnt"\\] {
    raise IllegalEscape(self.text[1:])
};