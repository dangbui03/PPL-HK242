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

program: list_expression;

//TODO Literal 6.6 pdf
literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| NIL
	| TRUE
	| FALSE
	| array_literal
	| struct_literal;

// TODO 5.2 Expressions 6 pdf
list_expression: expression COMMA list_expression | expression;

// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */ todo
// btl1

//! ---------------- LEXER ----------------------- */