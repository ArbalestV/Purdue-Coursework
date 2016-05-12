grammar Micro;

whitespace: WHITESPACE;

WHITESPACE: ('\n' | '\r' | ' ' | '\t');


KEYWORD: ('PROGRAM' | 'BEGIN' | 'END' | 'FUNCTION' |  
	 'READ' | 'WRITE' | 'IF' | 'ELSE' | 'FI' | 'FOR' | 
	 'ROF' | 'CONTINUE' | 'BREAK' | 'RETURN' | 'INT' | 
	 'VOID' | 'STRING' | 'FLOAT');

IDENTIFIER: [A-Za-z]+[0-9]*[A-Za-z]*;

INTLITERAL: [0-9]+;

FLOATLITERAL: [0-9]*['.'][0-9]*;

STRINGLITERAL: ('"')(~('"'))*('"');

COMMENT: '--'(~'\n')*'\n';


OPERATOR: ( ':=' | '+' | '-' | '*' | '/' | '=' | '!=' | '<' | '>' | '(' | ')' | ';' | ',' | '<=' | '>=');
