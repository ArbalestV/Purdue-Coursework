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
    
}
