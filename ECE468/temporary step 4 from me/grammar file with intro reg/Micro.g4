grammar Micro;


program 
	: 'PROGRAM' id 'BEGIN' pgm_body 'END' {/*AST.printHashMap();*/ createSymbolTable.popSymbolTable(); AST.printIRnodes(); AST.printHashMap2();} 
	;

id 
   : IDENTIFIER
   ;

pgm_body
	: {createSymbolTable.GlobalScopeTable();} decl /*{createSymbolTable.printGlobalTable();}*/ func_declarations 
	;

decl 
     : string_decl decl | var_decl decl | 
     ;

string_decl 
	    : 'STRING' id ':=' str ';' {createSymbolTable.insertVariable("STRING", $id.text, $str.text);} 
	    ;

str 
    : STRINGLITERAL
    ;

var_decl 
	 : var_type id_list ';' {createSymbolTable.insertVariable($var_type.text, $id_list.text, null);} 
	 ;

var_type 
	 : 'FLOAT' | 'INT'
	 ;

any_type 
	 : var_type | 'VOID'
	 ;

id_list 
	: id id_tail
	;

id_tail 
	: ',' id id_tail | 
	;


param_decl_list 
		: param_decl param_decl_tail | 
		;

param_decl 
	   : var_type id {createSymbolTable.insertVariable($var_type.text, $id.text, null);}
	   ;

param_decl_tail 
		: ',' param_decl param_decl_tail | 
		;

func_declarations 
		  : func_decl func_declarations | 
		  ;

func_decl 
	  : 'FUNCTION' any_type id {createSymbolTable.FunctionScopeTable($id.text);} '('param_decl_list')' 'BEGIN' func_body 'END' {createSymbolTable.popSymbolTable();} 
	  ;

func_body 
	  : decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list
	  ;

stmt_list 
	  : stmt stmt_list | 
	  ;

stmt 
     : base_stmt | if_stmt | for_stmt
     ;

base_stmt 
	  : assign_stmt | read_stmt | write_stmt | return_stmt
	  ;

assign_stmt 
	    : assign_expr ';'
	    ;

assign_expr 
	    : id ':=' 
	    {AST.setAST(":=", $id.text); /*System.out.println("\nAT THE BEGINNING OF THE EXPRESSION."); System.out.println("The root node: " + AST.rootequals); System.out.println("The left child: " + AST.leftChild); System.out.println("\nNow will print the AST.....");*/} 
	    expr 
	    {/*AST.checkStack();*/ /*System.out.println("\nAT THE END OF THE EXPRESSION."); System.out.println("The root node: " + AST.rootequals); System.out.println("The left child: " + AST.leftChild); */ AST.popFinalNode(); /* System.out.println("The right child content at the root: " + AST.rightChild.text);*/  System.out.println("\nPRINTED PARSE TREE:"); AST.print(); /*System.out.println("\n");*/}
	    ;

read_stmt 
	  : 'READ' '(' id_list ')' {AST.ReadFunc($id_list.text);} ';'
	  ;

write_stmt 
	   : 'WRITE' '(' id_list ')' {AST.WriteFunc($id_list.text);} ';'
	   ;

return_stmt 
	    : 'RETURN' expr ';'
	    ;


expr 
     : {/* System.out.println("in EXPR");*/} expr_prefix factor/* System.out.println("SUB-EXPRESSION OVER. NOW PRINTING THE CONTENTS OF THE STACK....."); AST.printStackCurr();}*/
     ;

expr_prefix 
	    : expr_prefix {/*System.out.println("in EXPR_PREFIX");*/} factor addop {AST.createNonTerminalNode($addop.text); /* System.out.println($addop.text + "\n"); */}
	    | 
	    ;

factor 
       : {/*System.out.println("in FACTOR");*/} factor_prefix postfix_expr {AST.checkStack();/*AST.moveRightChildUp();*/}
       ;

factor_prefix 
	      : factor_prefix {/*System.out.println("in FACTOR_PREFIX");*/} postfix_expr mulop {AST.createNonTerminalNode($mulop.text); /*System.out.println($mulop.text + "\n");*/}
	      | 
	      ;

postfix_expr 
	     :{/*System.out.println("in POSTFIX_EXPR");*/} primary | call_expr
	     ; //call_expr is ONLY for function calls

call_expr 
	  : {/*System.out.println("in CALL_EXPR");*/} id '(' expr_list ')'
	  ; //for function calls

expr_list 
	  : {/*System.out.println("in EXPR_LIST");*/} expr expr_list_tail 
	  | 
	  ; //for function calls

expr_list_tail 
	       :{/*System.out.println("in EXPR_LIST_TAIL");*/} ',' expr expr_list_tail | 
	       ; //for function calls



primary 
	: {/*System.out.println("in PRIMARYexpr");*/}'(' {AST.dontMove(1);} expr  ')' {AST.dontMove(0); AST.moveRightChildUp();}
	| {/*System.out.println("in PRIMARYid");*/}id {AST.createTerminalNode($id.text); /*System.out.println($id.text + "\n");*/} 
	| {/*System.out.println("in PRIMARYint");*/}INTLITERAL {AST.createTerminalNode($INTLITERAL.text); /*System.out.println($INTLITERAL.text + "\n");*/} 
	| {/*System.out.println("in PRIMARYfloat");*/}FLOATLITERAL {AST.createTerminalNode($FLOATLITERAL.text); /*System.out.println($FLOATLITERAL.text + "\n");*/}
	;

addop 
      : {/*System.out.println("in ADDOP");*/}'+' |{/*System.out.println("in ADDOP");*/} '-' 
      ;

mulop 
      : {/*System.out.println("in MULOP");*/}'*' | '/' 
      ;


if_stmt 
	: {createSymbolTable.BlockScopeTable();} 'IF' '(' cond ')' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} else_part 'FI'
	;

else_part 
	  : {createSymbolTable.BlockScopeTable();} 'ELSE' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} | 
	  ;

cond 
     : expr compop expr
     ;

compop 
       : '<' | '>' | '=' | '!=' | '<=' | '>=' 
       ;


init_stmt 
	  : assign_expr | 
	  ;

incr_stmt 
	  : assign_expr | 
	  ;

for_stmt 
	 : {createSymbolTable.BlockScopeTable();} 'FOR' '(' init_stmt ';' cond ';' incr_stmt ')' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} 'ROF'
	 ;




whitespace: WHITESPACE;

WHITESPACE: ('\n' | '\r' | ' ' | '\t') -> skip;


KEYWORD: ('PROGRAM' | 'BEGIN' | 'END' | 'FUNCTION' |  
	 'READ' | 'WRITE' | 'IF' | 'ELSE' | 'FI' | 'FOR' | 
	 'ROF' | 'CONTINUE' | 'BREAK' | 'RETURN' | 'INT' | 
	 'VOID' | 'STRING' | 'FLOAT');

IDENTIFIER: [A-Za-z]+[0-9]*[A-Za-z]*;

INTLITERAL: [0-9]+;

FLOATLITERAL: [0-9]*['.'][0-9]*;

STRINGLITERAL: ('"')(~('"'))*('"');

COMMENT: '--'(~'\n')*'\n' -> skip;


OPERATOR: ( ':=' | '+' | '-' | '*' | '/' | '=' | '!=' | '<' | '>' | '(' | ')' | ';' | ',' | '<=' | '>=');

