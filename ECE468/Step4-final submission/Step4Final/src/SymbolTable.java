import java.util.*;


public class SymbolTable {
    public HashMap<String, String> SymbolVarNamesHM = new HashMap<String, String>();
    public ArrayList<SymbolTableVariables> SymbolVarNames = new ArrayList<SymbolTableVariables>();
    public String scope;
    
    public SymbolTable(String scope) {
	this.scope = scope;
    }
    
    
    public void insertVariables(String variable_type, String variable_name, String string_value) {
	String[] StringArray = variable_name.split(",");
	int total_variables = StringArray.length;
	for(int i = 0; i < total_variables; i++) {
	    if(!(SymbolVarNamesHM.containsKey(StringArray[i]))) {
		SymbolTableVariables newObj = new SymbolTableVariables(StringArray[i], variable_type, string_value);
		SymbolVarNames.add(newObj);
		AST.SymbolVarNamesHM.put(StringArray[i], variable_type);
		SymbolVarNamesHM.put(StringArray[i], variable_type);
	    }
	    else {
		String errorMsg = "DECLARATION ERROR " + StringArray[i] + "\r";
		System.out.println(errorMsg);
		System.exit(0);
	    }
	}
    }
    
    public void printSymbolTable2() {
	
	if (this.scope == "GLOBAL") {
	    String to_be_printed = "Symbol table " + this.scope + "\r\n";
	    System.out.print(to_be_printed);
	    for(int i = 0; i < SymbolVarNames.size(); i++) {
		SymbolVarNames.get(i).printSymbolVariable();	
	    }
	    
	}
	else {
	    String to_be_printed = "Symbol table " + this.scope + "\r\n";
	    System.out.print(to_be_printed);
	    for(int i = 0; i < SymbolVarNames.size(); i++) {
		SymbolVarNames.get(i).printSymbolVariable();    
	    }
	}
	//System.out.println();
    }
}

