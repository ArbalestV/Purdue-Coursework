import java.util.*;

public class createSymbolTable {
    public static int blockCount = 1;
    public static Stack<SymbolTable> SymbolTableStack = new Stack<SymbolTable>();

    public static void printGlobalTable() {
	SymbolTable CurrentSymbolTable = SymbolTableStack.pop();
	CurrentSymbolTable.printSymbolTable2();
	SymbolTableStack.push(CurrentSymbolTable);
    }

    public static void printSymbolTable() {
	System.out.println();
	SymbolTable CurrentSymbolTable = SymbolTableStack.pop();
	CurrentSymbolTable.printSymbolTable2();
	SymbolTableStack.push(CurrentSymbolTable);
    }

    public static void popSymbolTable() {
	SymbolTableStack.pop();
    }

    public static void insertVariable(String variable_type, String variable_name, String string_value) {
	SymbolTable CurrentSymbolTable = SymbolTableStack.pop();
	CurrentSymbolTable.insertVariables(variable_type, variable_name, string_value);
	SymbolTableStack.push(CurrentSymbolTable);
    }
    
    public static void BlockScopeTable() {
	String blockCnt = Integer.toString(blockCount);
	blockCount = blockCount + 1;
	String totalScope = "BLOCK" + " " + blockCnt;
	SymbolTable block = new SymbolTable(totalScope);
	SymbolTableStack.push(block);
    }
    
    public static void FunctionScopeTable(String functionName) {
	String scope = functionName;
	SymbolTable function = new SymbolTable(scope);
	SymbolTableStack.push(function);
    }

    public static void GlobalScopeTable() {
	String scope = "GLOBAL";
	SymbolTable global = new SymbolTable(scope);
	SymbolTableStack.push(global);
    }  

    //new code added for step 6
    /*
    //this function will take care of adding the variables from the parameter list of the function into the symbol table, and subsequently refer with the notation P$
    public static void AddParameterList(String param_list) {
	System.out.println("The parameter list: " + param_list);
	for (String individual_params : param_list.split(",")) {//split each paramater by exploiting the fact that they are separated by commas
	    //now that we have each paramater in the form TYPE VARx, split them based on " " and call insertVariable() function on that so it gets into the hash map
	    System.out.println("The paramater is :" + individual_params);
	    String[] var = individual_params.split(" ");
	    System.out.println("Calling the function to put into the hash map: " + var[0] + "-" + var[1]);
	    insertVariable(var[0], var[1], null);
	}
    }*/
    public static int numParams;
    public static int insideFunction = 0;
    
}
