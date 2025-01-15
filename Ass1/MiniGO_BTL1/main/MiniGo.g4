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

program:  EOF;

struct_decl: TYPE ID STRUCT LBRACE list_field RBRACE;
list_field: field newline? | field list_field newline?;
field: ID type SEMI;

// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

type: INT | FLOAT | STRING | BOOLEAN;
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

// STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
// fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
// fragment ESC_SEQ: '\\' [brnt"\\];
// fragment ESC_ILLEGAL: [\r] | '\\' ~[brnt'\\];
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
// ERROR_CHAR: . {raise ErrorToken(self.text)};
// UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
//     if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
//         raise UncloseString(self.text[1:-2])
//     elif (self.text[-1] == '\n'):
//         raise UncloseString(self.text[1:-1])
//     else:
//         raise UncloseString(self.text[1:])
// };
// ILLEGAL_ESCAPE:
//     '"' STR_CHAR* ESC_ILLEGAL {
//     raise IllegalEscape(self.text[1:])
// };
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