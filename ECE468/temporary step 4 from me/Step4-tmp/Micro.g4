grammar Micro;

program : 'PROGRAM' id 'BEGIN' pgm_body 'END' {createSymbolTable.popSymbolTable();} ;
id : IDENTIFIER;
pgm_body : {createSymbolTable.GlobalScopeTable();} decl /*{createSymbolTable.printGlobalTable();}*/ func_declarations ;
decl : string_decl decl | var_decl decl | ;

string_decl : 'STRING' id ':=' str ';' {createSymbolTable.insertVariable("STRING", $id.text, $str.text);} ;
str : STRINGLITERAL;

var_decl : var_type id_list ';' {createSymbolTable.insertVariable($var_type.text, $id_list.text, null);} ;
var_type : 'FLOAT' | 'INT';
any_type : var_type | 'VOID';
id_list : id id_tail;
id_tail : ',' id id_tail | ;

param_decl_list : param_decl param_decl_tail | ;
param_decl : var_type id {createSymbolTable.insertVariable($var_type.text, $id.text, null);};
param_decl_tail : ',' param_decl param_decl_tail | ;

func_declarations : func_decl func_declarations | ;
func_decl : 'FUNCTION' any_type id {createSymbolTable.FunctionScopeTable($id.text);} '('param_decl_list')' 'BEGIN' func_body 'END' {createSymbolTable.popSymbolTable();} ;
func_body : decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list;

stmt_list : stmt stmt_list | ;
stmt : base_stmt | if_stmt | for_stmt;
base_stmt : assign_stmt | read_stmt | write_stmt | return_stmt;

assign_stmt : assign_expr ';';

assign_expr : id ':=' {AST.setAST(":=", $id.text);} expr {AST.popFinalNode();};

read_stmt : 'READ' '(' id_list ')'';';
write_stmt : 'WRITE' '(' id_list ')'';';
return_stmt : 'RETURN' expr ';';

expr : expr_prefix factor ;

expr_prefix : expr_prefix factor addop {AST.createNonTerminalNode($addop.text); /*System.out.println($addop.text + "\n");*/} | ;

factor : factor_prefix postfix_expr {System.out.println("In factor production: " + "Factor prefix: " + $factor_prefix.text + " " + "Postfix expression: " + $postfix_expr.text);} {AST.moveRightChildUp();};

factor_prefix : factor_prefix postfix_expr mulop {AST.createNonTerminalNode($mulop.text); /*System.out.println($mulop.text + "\n");*/}| ;

postfix_expr : primary | call_expr; //call_expr is ONLY for function calls

call_expr : id '(' expr_list ')'; //for function calls
expr_list : expr expr_list_tail | ; //for function calls
expr_list_tail : ',' expr expr_list_tail | ; //for function calls

primary : '(' expr ')' | id {AST.createTerminalNode($id.text); /*System.out.println($id.text + "\n");*/} | INTLITERAL {AST.createTerminalNode($INTLITERAL.text); /*System.out.println($INTLITERAL.text + "\n");*/} | FLOATLITERAL {AST.createTerminalNode($FLOATLITERAL.text); /*System.out.println($FLOATLITERAL.text + "\n");*/};

addop : '+' | '-' ;
mulop : '*' | '/' ;

if_stmt : {createSymbolTable.BlockScopeTable();} 'IF' '(' cond ')' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} else_part 'FI';
else_part : {createSymbolTable.BlockScopeTable();} 'ELSE' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} | ;
cond : expr compop expr;
compop : '<' | '>' | '=' | '!=' | '<=' | '>=' ;

init_stmt : assign_expr | ;
incr_stmt : assign_expr | ;

for_stmt : {createSymbolTable.BlockScopeTable();} 'FOR' '(' init_stmt ';' cond ';' incr_stmt ')' decl /*{createSymbolTable.printSymbolTable();}*/ stmt_list {createSymbolTable.popSymbolTable();} 'ROF';

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

