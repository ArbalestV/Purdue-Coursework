grammar Micro;


program : 'PROGRAM' id 'BEGIN' pgm_body 'END' {createSymbolTable.popSymbolTable();} ;
id : IDENTIFIER;
pgm_body : {createSymbolTable.GlobalScopeTable();} decl {createSymbolTable.printGlobalTable();} func_declarations ;
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
func_body : decl {createSymbolTable.printSymbolTable();} stmt_list;

stmt_list : stmt stmt_list | ;
stmt : base_stmt | if_stmt | for_stmt;
base_stmt : assign_stmt | read_stmt | write_stmt | return_stmt;

assign_stmt : assign_expr ';';
assign_expr : id ':=' expr;
read_stmt : 'READ' '(' id_list ')'';';
write_stmt : 'WRITE' '(' id_list ')'';';
return_stmt : 'RETURN' expr ';';

expr : expr_prefix factor;
expr_prefix : expr_prefix factor addop | ;
factor : factor_prefix postfix_expr;
factor_prefix : factor_prefix postfix_expr mulop | ;
postfix_expr : primary | call_expr;
call_expr : id '(' expr_list ')';
expr_list : expr expr_list_tail | ;
expr_list_tail : ',' expr expr_list_tail | ;
primary : '(' expr ')' | id | INTLITERAL | FLOATLITERAL;
addop : '+' | '-';
mulop : '*' | '/';

if_stmt : {createSymbolTable.BlockScopeTable();} 'IF' '(' cond ')' decl {createSymbolTable.printSymbolTable();} stmt_list {createSymbolTable.popSymbolTable();} else_part 'FI';
else_part : {createSymbolTable.BlockScopeTable();} 'ELSE' decl {createSymbolTable.printSymbolTable();} stmt_list {createSymbolTable.popSymbolTable();} | ;
cond : expr compop expr;
compop : '<' | '>' | '=' | '!=' | '<=' | '>=' ;

init_stmt : assign_expr | ;
incr_stmt : assign_expr | ;

for_stmt : {createSymbolTable.BlockScopeTable();} 'FOR' '(' init_stmt ';' cond ';' incr_stmt ')' decl {createSymbolTable.printSymbolTable();} stmt_list {createSymbolTable.popSymbolTable();} 'ROF';

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



//whitespace: WHITESPACE;
//@rulecatch
//{
//	catch (RecognitionException re) {
//	      throw re;
//	}
//}

//@parser::members {
		 //@Override
//		 public void displayRecognitionError(String[] tokenNames, RecognitionException re) {
	//	 	String hdr = getErrorHeader(re);      
	//		String msg = getErrorMessage(re, tokenNames);
	//		msg = "Not Accepted";
	//	 	throw new RuntimeException(msg);
	//		}
//}

//@lexer::members {
		 //@Override
//		 public void displayRecognitionError(String[] tokenNames, RecognitionException re) {
//		 	throw new RuntimeException("Not Accepted");
//			}
//}
