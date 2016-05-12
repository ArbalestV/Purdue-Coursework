import java.util.HashMap;
import java.util.LinkedList;
import java.util.*;
import java.lang.*;


public class FunctionClass {
    public String functionName;
    public int LocalVarCount;
    public int ParameterCount;
    public int TempCount = 0;
    public int startingTemp;
    public LinkedList<IRnode> irnodelist = new LinkedList<IRnode>();
    public HashMap<String, String> parameterList = new HashMap<String, String>();
    public HashMap<String, String> parameterType = new HashMap<String, String>();
    public SymbolTable symbolTable;

    public HashMap<String, String> SymbolVarNamesHM = new HashMap<String, String>();
    public int regCount;

    public ArrayList<Integer> blockLeaders = new ArrayList<Integer>();
    public ArrayList<Integer> blocks = new ArrayList<Integer>();
    public ArrayList<ArrayList<Integer>> basicBlocks = new ArrayList<ArrayList<Integer>>();
    
    public FunctionClass(String functionName) {
	this.functionName = functionName;
    }
    
}
