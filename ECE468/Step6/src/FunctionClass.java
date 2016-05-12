import java.util.HashMap;
import java.util.LinkedList;


public class FunctionClass {
    public String functionName;
    public int LocalVarCount;
    public int ParameterCount;
    public LinkedList<IRnode> irnodelist = new LinkedList<IRnode>();
    public HashMap<String, String> parameterList = new HashMap<String, String>();
    public HashMap<String, String> parameterType = new HashMap<String, String>();
    public SymbolTable symbolTable;

    public HashMap<String, String> SymbolVarNamesHM = new HashMap<String, String>();
    public int regCount;
    
    public FunctionClass(String functionName) {
	this.functionName = functionName;
    }
    
}
