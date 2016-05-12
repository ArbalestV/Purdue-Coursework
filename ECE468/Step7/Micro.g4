grammar Micro;


program 
	: 'PROGRAM' id 'BEGIN' pgm_body 'END' { createSymbolTable.popSymbolTable(); AST.printIRnodes();} 
	;

id 
   : IDENTIFIER
   ;

pgm_body
	: { createSymbolTable.GlobalScopeTable();} decl /*{createSymbolTable.printGlobalTable();}*/ func_declarations 
	;

decl 
     : string_decl decl |  var_decl decl | 
     ;

string_decl 
	    : 'STRING' id ':=' str ';' {createSymbolTable.insertVariable("STRING", $id.text, $str.text); AST.StringVarHM.put($id.text, $str.text); AST.addToFunctionParameterList($id.text, "L");} 
	    ;

str 
    : STRINGLITERAL
    ;

var_decl 
	 : var_type id_list ';' {createSymbolTable.insertVariable($var_type.text, $id_list.text, null); /*AST.addVartoHM($id_list.text);*/ AST.addToFunctionParameterList($id_list.text, "L");}
	 ;

var_type 
	 : 'FLOAT' | 'INT'
	 ;

any_type 
	 : var_type | 'VOID'
	 ;

id_list 
	: id id_tail {/*AST.addToFunctionParameterList($id.text, "L");*/}
	;

id_tail 
	: ',' id {/*AST.addToFunctionParameterList($id.text, "L");*/} id_tail | 
	;


param_decl_list 
		: param_decl param_decl_tail | 
		;

param_decl 
	   : var_type id {createSymbolTable.insertVariable($var_type.text, $id.text, "PARAMETER"); AST.addToFunctionParameterList($id.text, "P"); createSymbolTable.numParams++;}
	   ;

param_decl_tail 
		: ',' param_decl param_decl_tail | 
		;

func_declarations 
		  : func_decl func_declarations | 
		  ;

func_decl 
	  : 'FUNCTION' any_type id {createSymbolTable.FunctionScopeTable($id.text); AST.createFunction($id.text); createSymbolTable.numParams = 0; createSymbolTable.insideFunction = 1;} '('param_decl_list ')' 'BEGIN' func_body 'END' { AST.addFunctionSymbolTable(); createSymbolTable.popSymbolTable(); createSymbolTable.insideFunction = 0;} 
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
	    :  id ':=' 
	    {AST.setAST(":=", $id.text);} 
	    expr 
	    { AST.popFinalNode(); AST.callingFunction = 0;}
	    ;

read_stmt 
	  : 'READ' '(' id_list ')' {AST.ReadFunc($id_list.text);} ';'
	  ;

write_stmt 
	   : {/*System.out.println("In Write statment");*/} 'WRITE' '(' id_list ')' {AST.WriteFunc($id_list.text);}';' {/*System.out.println("Finished WRite statement");*/}
	   ;

return_stmt 
	    : {AST.returnText = 1;} 'RETURN' expr {AST.popFinalNodeReturn(); AST.returnNode(); AST.returnText = 0;} ';'
	    ;


expr 
     : {/*System.out.println("NEW EXPR");*/} expr_prefix {/*System.out.println("EXPR -> factor");*/} factor {/*System.out.println("end of expression");*/}
     ;

expr_prefix 
	    : expr_prefix {/*System.out.println("ExprPrefix -> factor");*/} factor {/*System.out.println("expr_prefix, FACTOR COMPLETE");*/} addop {/*System.out.println("Expr_prefix complete");*/ /*System.out.println("Element hit: " + $addop.text);*/ AST.createNonTerminalNode($addop.text); }
	    | 
	    ;

factor 
       : {/*System.out.println("NEW FACTOR");*/} factor_prefix {/*System.out.println("Factor -> postfix_expr");*/} postfix_expr {/*System.out.println("factor complete");*/ /*System.out.println("Factor recognized. Calling checkstack func.");*/ AST.factorRecognized = 1; AST.checkStack(); /*System.out.println("factor recognized");*/}
       ;

factor_prefix 
	      : factor_prefix {/*System.out.println("NEW FACTORPREFIX");*/} postfix_expr {/*System.out.println("PostFixExpr Complete");*/} mulop {/*System.out.println("factor_prefix complete");*/ /*System.out.println("Element hit: " + $mulop.text);*/ AST.createNonTerminalNode($mulop.text); }
	      | 
	      ;

postfix_expr 
	     : {/*System.out.println("NEW POSTFIXEXPR");*/} primary | call_expr
	     ; //call_expr is ONLY for function calls

call_expr 
	  : {AST.callingFunction = 1;} id '(' expr_list {AST.callExpr($id.text, $expr_list.text); AST.createTerminalNode($id.text);} ')'
	  ; //for function calls

expr_list 
	  : expr  {AST.popFinalNodeFunction();} expr_list_tail 
	  | 
	  ; //for function calls

expr_list_tail 
	       : ',' expr {AST.popFinalNodeFunction();} expr_list_tail | 
	       ; //for function calls



primary 
	: {AST.dontMove(1); /*AST.insideExprCount = 0;*/ AST.exprStackCount = AST.stackCount; /*System.out.println("\nExpression stack count at entry: " + AST.exprStackCount);*/} '('  expr  ')' {/*System.out.println("Found nested expression");*/ AST.dontMove(0); /*AST.moveRightChildUp();*/}
	| id {/*System.out.println("Element hit: " + $id.text);*//*System.out.println($id.text);*/ AST.createTerminalNode($id.text); } 
	| INTLITERAL {/*System.out.println("Element hit: " + $INTLITERAL.text);*/ /*System.out.println($INTLITERAL.text);*/ AST.createTerminalNode($INTLITERAL.text); } 
	| FLOATLITERAL {/*System.out.println("Element hit: " + $FLOATLITERAL.text);*//*System.out.println($FLOATLITERAL.text);*/ AST.createTerminalNode($FLOATLITERAL.text); }
	;

addop 
      : {/*System.out.println("+");*/} '+' | {/*System.out.println("-");*/} '-' 
      ;

mulop 
      : {/*System.out.println("*");*/} '*' | {/*System.out.println("/");*/} '/' 
      ;


if_stmt 
	: {/*System.out.println("IN IF STATEMENT"); System.out.println("StackCount = "+AST.stackCount);*/ createSymbolTable.BlockScopeTable(); AST.pushIfLabels();} 'IF' '(' cond ')' {/*System.out.print("Finished condition");*/} decl /*{createSymbolTable.printSymbolTable();}*/ {/*System.out.println("IF --> StmtList");*/} stmt_list {createSymbolTable.popSymbolTable(); AST.jump_label(1); } else_part 'FI' {AST.jump_label(4); /*System.out.println("Out of IF statement");*/}
	;

else_part 
	  : {createSymbolTable.BlockScopeTable(); AST.jump_label(2); /*System.out.println("in ELSE statement");*/} 'ELSE' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {AST.jump_label(3);} {createSymbolTable.popSymbolTable();} | {AST.jump_label(2);}
	  ;

cond 
     :  {/*System.out.println("IN COND");*/}expr  {/*System.out.println("COND --> COMPOP");*/}compop {AST.createNonTerminalNode($compop.text);} expr {AST.popFinalNodeCondition();}{/*System.out.println("End of condition");*/}
     ;

compop 
       : '<' | '>' | '=' | '!=' | '<=' | '>=' 
       ;


init_stmt 
	  : assign_expr | 
	  ;

incr_stmt 
	  : {AST.incrStmt = 1; /*System.out.println("in INCR_STATEMENT");*/} assign_expr {/*System.out.println("Out of Increment statment");*/ AST.incrStmt = 0;}| {/*System.out.println("IN EMPTY INCR_STMT.");*/}
	  ;

for_stmt 
	 : {createSymbolTable.BlockScopeTable();} 'FOR'  '(' init_stmt ';'{/*System.out.println("Out of init_statment");*/ AST.pushForLabels(); AST.for_label(1); AST.inFor = 1;} cond { AST.inFor = 0;}';' incr_stmt ')' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list { /*System.out.println("AST.incrIRnode");*/ AST.for_label(2); /*System.out.println("INCRIRNODE");*/ AST.incrIRnode(); AST.for_label(3); createSymbolTable.popSymbolTable();} 'ROF' {AST.for_label(4); }
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

