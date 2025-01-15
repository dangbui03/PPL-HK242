// ID: 2153289 - Bui Ho Hai Dang

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// Program
program: NEWLINE* decllist EOF;
decllist: decl decllist | decl;
decl: func_decl | variable_decl newline;

// function declaration
// main_decl: func main LPAREN (para_prime)? RPAREN newline* (block_statement | return_statement)? newline?;
func_decl: func ID para_decl newline* (newline? block_statement | newline? return_statement | newline) ;
para_decl: LPAREN para_list RPAREN;
para_list: para_prime | ;
para_prime: parameter COMMA? para_prime | parameter;
parameter: data_type ID | array_type;

// variable declaration
variable_decl: var | var_implicit | dyn_implicit;
var: data_type ID (ASSIGN expr)? | array_type (ASSIGN expr)?;
var_implicit: vartype ID ASSIGN expr;
dyn_implicit: dyntype ID (ASSIGN expr)?;

// statement
statementlist: statement statementlist | ;
statement: 	decl_statement
			| assignment_statement
			| if_statement
			| for_statement
			| break_statement
			| continue_statement
			| return_statement
			| funcCall_statement
			| block_statement
			;
//variable declaration statement
decl_statement: variable_decl newline;
// block statement
block_statement: beginn newline statementlist newline? endd newline;

// assignment statement
assignment_statement: lhs ASSIGN expr newline;
lhs: ID index_operator | ID;

// if statement
if_statement: ifword expr newline? (statement | block_statement) newline? elif_statement newline? else_statement;
else_statement: elseword newline? (statement | block_statement) newline? | newline?;
elif_statement: elifword expr newline? (statement | block_statement) newline? elif_statement | ;

// for statement
for_statement: forword ID unitlword expr byword expr newline? (statement | block_statement) newline?;

// break and continue and return statement
break_statement: breakword newline;
continue_statement: continueword newline;
return_statement: returnn expr? newline;

// Function call statement
funcCall_statement: ID LPAREN expr_list? RPAREN newline;

// Expressions
expr_list: expr COMMA expr_list | expr;
expr
	: relation_expr ELLIPSIS relation_expr
	| relation_expr
	;
relation_expr
	: andOr_expr (equall | NOT_EQUAL | SMALLER | BIGGER | EQUALSMALLER | EQUALBIGGER | EQUALITY) andOr_expr
	| andOr_expr
	;
andOr_expr
	: andOr_expr (andword | orword) add_expr
	| add_expr
	;
add_expr
	: add_expr (addd | subb) mul_expr
	| mul_expr
	;
mul_expr
	: mul_expr (mull | divv | modd) not_expr
	| not_expr
	;
not_expr
	: notword not_expr 
	| sub_expr
	; 
sub_expr
	: subb sub_expr
	| element_expr
	;

element_expr: array_element | func_expr;

func_expr: funcCall | exprd;

exprd: data_value | ID | '(' expr ')';

funcCall: ID LPAREN expr_list? RPAREN newline?;

index_operator: LBRACE expr_list RBRACE | LBRACE expr_list RBRACE index_operator;
//element_expr: expr LBRACE index_operator element_expr RBRACE | index_operator;

array_element: func_expr index_operator;

// value
data_value: numberliteral | boolliteral | strliteral | array_value;
array_value: LBRACE arr_list? RBRACE;

// type
arr_list: data_value COMMA arr_list | data_value;
data_type: numtype | booltype | stringtype;
array_type: data_type ID LBRACE numlist RBRACE;

numlist: NUM_LIT COMMA numlist | NUM_LIT;

numberliteral: NUM_LIT;
boolliteral: TRUE | FALSE;
strliteral: STR_LIT;

newline: NEWLINE+ ;
NEWLINE: [\n];
//NEWLINE : '\n' {self.text = "NEWLINE";} | '\r\n' {self.text = "\n";} | '\r' {self.text = "NEWLINE";};

// Lexer rules
// Comment
COMMENT: '##' ~[\r\n\f]* -> skip;

// Keywords
TRUE: 'true';
FALSE: 'false';
numtype: 'number';
booltype: 'bool';
stringtype: 'string';
returnn: 'return';
vartype: 'var';
dyntype: 'dynamic';
func: 'func';
forword: 'for';
unitlword: 'until';
byword: 'by';
breakword: 'break';
continueword: 'continue';
ifword: 'if';
elseword: 'else';
elifword: 'elif';
beginn: 'begin';
endd: 'end';

notword: 'not';
andword: 'and';
orword: 'or';

// Operators
addd: '+';
subb: '-';
mull: '*';
divv: '/';
modd: '%';
equall: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
SMALLER: '<';
EQUALSMALLER: '<=';
BIGGER: '>';
EQUALBIGGER: '>=';
ELLIPSIS: '...';
EQUALITY: '==';

// Separators
LPAREN: '(';
RPAREN: ')';
LBRACE: '[';
RBRACE: ']';
COMMA: ',';

// Literals
NUM_LIT	
	: INT DEC_1? EXP?
	;
INT: [0-9]+;
fragment DEC_1: '.' [0-9]*;
fragment DEC_2: '.' [0-9]+;
fragment EXP: [eE] [+-]? INT;

STR_LIT	: '"' ( ESCAPE_SEQ | ~['"\r\n\f\\])* '"'  {self.text = self.text[1:-1]};

WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

// IDs
ID: [a-zA-Z_][a-zA-Z0-9_]*;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ( ~[\f\r\n'"\\] | ESCAPE_SEQ )* ( EOF | '\n' | '\r\n') {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' ( ~[\r\n\f\\b'"] | ESCAPE_SEQ )* ([\r\f\\'] | IllegalEscape | [']~["]) {
	raise IllegalEscape(self.text[1:])
};
fragment IllegalEscape: '\\' ~[bfrnt'\\];
fragment ESCAPE_SEQ: '\\' [btnfr'\\] | [']["];