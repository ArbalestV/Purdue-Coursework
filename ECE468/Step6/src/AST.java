import java.util.*;
import java.lang.*;
public class AST {
    public static String rootequals; //since AST is only called from assignments, ':=' will always be the root. This will be called accordingly from the grammar file
    public static String leftChild; //for an AST since it is only initialized during an assignment statement, we will have have the left child as an identifier. We will be called accordingly from the grammar file
    public static ASTnode rightChild; //the right child could be either an identifier/literal, or another node which would essentially be a subtree. We will declare a different data structure ASTnode for this purpose
    public static Stack<ASTnode> nodestackframe = new Stack<ASTnode>(); //the right child will essentially be a node, consisting of successive left and right children of nodes. Thus, we need to keep pushing it onto the stack, so that we know which stage of the right subtree we are in
    //public static Iterator<ASTnode> iter = nodestackframe.iterator();
    public static String operatorSeen = "no"; //to distinguish between a := b and a := b + c
    public static int stackCount;
    public static String moveOK = "yes";
    public static int factorRecognized = 0;
    //public static int factorRecognizedWithin = 0;
    public static int exprStackCount;
    public static int insideExprCount = 0;
    public static int NUM_OF_TIMES_NOT_HIT = 0;

    //step 5 stuff
    public static int inFor = 0; //to signify the label value for for loop. it will be globalvalue - 2 for if, but globalvalue for for
    public static int currentGlobalLabelValue = 1;

    public static Stack<ASTnode> incrFor = new Stack<ASTnode>();
    public static int incrStmt = 0;
    public static String incrAssignment;
    public static int forLabel = 0;
    public static int exitLabel = 0;
    public static Stack<Integer> labelStack = new Stack<Integer>();
    public static HashMap<String, String> StringVarHM = new HashMap<String, String>();

    //Step 6
    public static String currentFunction;
    public static FunctionClass function; 
    public static LinkedList<FunctionClass> functionList = new LinkedList<FunctionClass>();
    public static String functionResult;
    public static int callingFunction = 0;
    public static List<String> FunctionParameters = new ArrayList<String>();
    public static Stack<ASTnode> returnStack = new Stack<ASTnode>();
    public static int returnText = 0;

    public static FunctionClass currFunc;
    public static FunctionClass tinyFunction;

    public static ArrayList<String> GlobalVarHM = new ArrayList<String>();
    public static HashMap<String, String> GlobalVarTypeHM = new HashMap<String, String>();
    public static HashMap<String, String> GlobalStringHM = new HashMap<String, String>();


    public static boolean addFunctionParameter(String str){
	
	if(function.parameterList.get(str) != null){
	    FunctionParameters.add("$"+function.parameterList.get(str));
	    return true;
	}
	else {
	    return false;	
	}
    }

    public static void popFinalNodeReturn() {
	//System.out.println("Pop Final Node RETURN");
	ASTnode temp = nodestackframe.pop();
	//System.out.println("Just popped off root: "+temp.text);
	stackCount--;
	PostOrderTraversal(temp);
    }

    public static void popFinalNodeFunction() {
	//if(callingFunction == 0) {
	//    return;
	//}
	//System.out.println("popping stack, to post order traverse");
	ASTnode temp = nodestackframe.pop();//assign to the right child
	boolean addParam = addFunctionParameter(temp.text);
	stackCount--;
	//System.out.println("traverse :"+temp.text);
	PostOrderTraversal(temp);
	if (addParam == false) {
	    FunctionParameters.add("$T"+Integer.toString(regCount));	
	}
    }

    public static String checkType(String val) {
	try {
	    Integer.parseInt(val);
	    return "INT";
	}
	catch (NumberFormatException ex) {	
	    return "FLOAT";
	}
    }


    public static void callExpr(String Name, String parameters) {
    	//You are making a function call
	//push space for return value
	int popCount = 0;
	function.irnodelist.add(new IRnode("PUSH", null, null, null));
	//split parameters and push them
	for(int j=0; j<FunctionParameters.size(); j++){
	    function.irnodelist.add(new IRnode("PUSH", FunctionParameters.get(j), null, null));
	    popCount++;
	}
	//JSR
	function.irnodelist.add(new IRnode("JSR", Name, null, null));
	//pop parameters
	for(int i=0; i < popCount; i++) {
	    function.irnodelist.add(new IRnode("POP", null, null, null));	
	}
	//pop result value
	functionResult = createRegister();
	function.irnodelist.add(new IRnode("POP", functionResult, null, null));
	//rightChild.text = register;
	FunctionParameters.clear();
	
    }

    public static void returnNode(){
	//System.out.println("popping off return stack");
	ASTnode result = returnStack.pop();
	
	String type;
	if(SymbolVarNamesHM.get(result.text) != null) {
	    type = SymbolVarNamesHM.get(result.text);	
	}
	else {
	    type = checkType(result.text);	
	}
	//System.out.println("Type: "+type);
	String instr = "";
	if(type.equals("INT")){
	    instr = "STOREI";
	}
	else{
	    instr = "STOREF";	
	}
	if(function.parameterList.get(result.text) != null) {
	    String reg = "$"+function.parameterList.get(result.text);
	    function.irnodelist.add(new IRnode(instr, reg, null, "$R"));
	}
	else {
	    String reg = createRegister();
	    function.irnodelist.add(new IRnode(instr, result.text, null, reg));
	    function.irnodelist.add(new IRnode(instr, reg, null, "$R"));
	}
	
	function.irnodelist.add(new IRnode("RET", null, null, null));
    }

    public static String checkLocal(String var) {
	if(function.parameterList.get(var) != null) {
	    var = "$"+function.parameterList.get(var);	
	}
	
	return var;
    }

    public static void createFunction(String FunctionName) {
	currentFunction = FunctionName;
	function = new FunctionClass(FunctionName);
	functionList.add(function);
	function.LocalVarCount = 0;
	function.ParameterCount = 0;
	
	function.irnodelist.add(new IRnode("LABEL", FunctionName, null, null));
	function.irnodelist.add(new IRnode("LINK", null, null, null));
    }

   public static void addFunctionSymbolTable() {
	SymbolTable tmp = createSymbolTable.SymbolTableStack.pop();
	function.symbolTable = tmp;
	createSymbolTable.SymbolTableStack.push(tmp);
   }

    public static void addToFunctionParameterList(String name, String PorL) {
	for(String retval: name.split(",")) {	
	if(StringVarHM.get(retval) == null){
	    if(function.parameterList.get(retval) == null) {
	    	String tmp = PorL;		
	    	if(createSymbolTable.insideFunction == 1) {
	       	    if(PorL == "P"){
		        function.ParameterCount++;
	                tmp = tmp + Integer.toString(function.ParameterCount);
	            }
	            else{
		        function.LocalVarCount++;	
		        tmp = tmp + Integer.toString(function.LocalVarCount);
	            }
	            function.parameterList.put(retval, tmp);
		    /*
		    for(String key: SymbolVarNamesHM.keySet()){
		   	System.out.println("Key: "+key);
	 	    }
	  	    */
		    String type = SymbolVarNamesHM.get(retval);
		    //System.out.println("Adding to parameter type - name: "+retval+" type: "+type);
		    function.parameterType.put(tmp, type);	
		}
	    }
	}
	}
    }

    public static void pushForLabels() {
	//System.out.println("PUSHING FOR LABELS");
	labelStack.push(currentGlobalLabelValue);
	currentGlobalLabelValue++;
	labelStack.push(currentGlobalLabelValue);
	currentGlobalLabelValue++;
	labelStack.push(currentGlobalLabelValue);
	currentGlobalLabelValue++;
    }
    
    public static void pushIfLabels() {
	//System.out.println("PUSHING IF LABELS");
	labelStack.push(currentGlobalLabelValue);
	currentGlobalLabelValue++;
	labelStack.push(currentGlobalLabelValue);
	currentGlobalLabelValue++;
    }

    public static void incrIRnode() {
	String storeType = "";
	//System.out.println("CHECKING IF THE INCRFOR STACK IS EMPTY: " + incrFor.empty());
	//if the incrFor stack is empty which means that the incr_Stmt is null, then just get out by not displaying anything. The label display will have been taken care of earlier.
	if (incrFor.empty()) {
	    return; 
	}
	ASTnode right = incrFor.pop();
	PostOrderTraversal(right);
	String typeLeftChild = SymbolVarNamesHM.get(incrAssignment);
	//System.out.println("TYPE LEFT CHILD: "+typeLeftChild);
	if(typeLeftChild.equals("INT")){
	    storeType = "STOREI"; 
	}
	else{
	    storeType = "STOREF";
	}
	function.irnodelist.add(new IRnode(storeType, checkLocal(right.text), null , checkLocal(incrAssignment)));
		
    }

    public static void for_label(int i) {
	int condLabel = labelStack.pop();
	int incrLabel = labelStack.pop();
	int pre_condLabel = labelStack.pop();

	if(i == 1){
	    function.irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(pre_condLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if(i == 2){
	    function.irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(incrLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if( i == 3) {
	    function.irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(pre_condLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if(i == 4){
	    function.irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(condLabel), null, null));
	}

    }

    public static void jump_label(int i) {
	int exit_label = labelStack.pop();
	int else_label = labelStack.pop();

	if( i == 1) {
	    //System.out.println("Value1: "+value1 + " Value2: "+value2);
	    function.irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(exit_label), null, null));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(i == 2) {
	    function.irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(else_label), null, null));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);	
	}
	else if(i == 3) {
	    function.irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(exit_label), null, null));	
	    labelStack.push(else_label);
	    labelStack.push(exit_label);	
	}
	else {//if(i == 4) {
	    function.irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(exit_label), null, null));		
	}
	

	
    }	

    public static void popFinalNodeCondition() {

	ASTnode temp = nodestackframe.pop();//assign to the right child

	PostOrderTraversal(temp);
    }

   

    //IR Node Stuff
    public static LinkedList<IRnode> irnodelist = new LinkedList<IRnode>();
    public static HashMap<String, String> SymbolVarNamesHM = new HashMap<String, String>();
    public static int regCount = 0;
    public static Stack<String> regstackframe = new Stack<String>();
    public static String instr = "";

    public static int childCount;
    public static String type = "";
    public static String register = "";

    //Tiny node stuff
    public static LinkedList<TinyNode> tinyList = new LinkedList<TinyNode>();
    public static HashMap<String, String> RegisterHM = new HashMap<String, String>();


    public static String createTinyReg(){
	return( "r"+(regCount++));
	
    }	

    public static String checkRegister(String op2){
 	//System.out.println("Op2 = "+op2);
	//System.out.println("op2.substring(0,1) = "+op2.substring(0,1));
	//System.out.println("op2.substring(1) = "+op2.substring(1));
	String checkReg = "$T"+op2.substring(1);
	if(RegisterHM.get(checkReg) != null){
	    //System.out.println("THIS IS A REGISTER");	
	    return op2;
	}
	else {
	    //System.out.println("THIS IS NOT A REGISTER");	
	    String Tinyregister = createTinyReg();
	    RegisterHM.put(Tinyregister, "register");
	    return Tinyregister;
	}
    }

    //Tiny Code Generation
    public static void printTinyCode() {
	
	for (int i = 0; i < tinyList.size(); i++ ) {
	    tinyList.get(i).printTiny();
	}
	/*System.out.println("Register HM after tiny code");
	for (String key : RegisterHM.keySet()) {
	    String Value = RegisterHM.get(key);
	    System.out.println("Key: "+key+" Value: "+Value);	
	}
	*/
    }

    public static void convertToTiny() {
	for(int i=0; i<GlobalVarHM.size(); i++){
	    String key = GlobalVarHM.get(i);
	    String type = GlobalVarTypeHM.get(key);
	    if(type == "STRING"){
		String str = GlobalStringHM.get(key);
		tinyList.add(new TinyNode("str", key, str));
	    }
	    else {
		tinyList.add(new TinyNode("var", key, null));
	    }
	}	
	
	//adding in initial nodes for pushes, jump to main, sys halt
	tinyList.add(new TinyNode("push", null, null));
	tinyList.add(new TinyNode("push", "r0", null));
	tinyList.add(new TinyNode("push", "r1", null));
	tinyList.add(new TinyNode("push", "r2", null));
	tinyList.add(new TinyNode("push", "r3", null));
	tinyList.add(new TinyNode("jsr", "main", null));
	tinyList.add(new TinyNode("sys", "halt", null));

	//Scan through Function IR Lists
	for(int i=0; i < functionList.size(); i++){
	    //System.out.println("\nPrinting IR nodes for: "+functionList.get(i).functionName);
	    for(int j=0; j < (functionList.get(i)).irnodelist.size(); j++) {
		currFunc = functionList.get(i);
	    	createTiny((functionList.get(i)).irnodelist.get(j));
	    }	
	}

	//add end instruction
	tinyList.add(new TinyNode("end", null, null));
	System.out.println(";tiny code");
	printTinyCode();

    }
    
    public static String tinyFormat(String opcode) {
	if(opcode == null) {
	    return opcode;	
	}
	String tinyOp = opcode;	
	if(opcode.substring(0,1).equals("$")){
	    if(opcode.substring(0,2).equals("$R")){
		int Pnum = tinyFunction.ParameterCount;
		tinyOp = "$"+Integer.toString(6+Pnum);
		return tinyOp;
	    }

	    int count = Integer.parseInt(opcode.substring(2));
	    int rNum = count;
	    if(opcode.substring(0,2).equals("$T")){ 	
		rNum = count - 1;
	    	String regNum = Integer.toString(rNum);
	    	tinyOp = "r"+regNum;
	    }
	    else if(opcode.substring(0,2).equals("$P")){
		tinyOp = "$"+Integer.toString(6+count-1);
	    }
	    else {// if(opcode.substring(0,2).equals("$L")){
		tinyOp = "$-"+Integer.toString(count);
	    }
	}

	return tinyOp;
    }

    public static void createTiny(IRnode irNode) {
	//System.out.println("IRNODE: instr: "+irNode.instr+" op1: "+irNode.op1+" op2: "+irNode.op2+" res: "+irNode.res);
	String opcode = irNode.instr;
	String cmp = "cmp";
	//System.out.println("Tiny Node being created - opcode: "+opcode+ "op1: "+irNode.op1+" op2: "+irNode.op2+" res: "+irNode.res);

	if(opcode.equals("WRITEI")) {
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "writei", res));
	    //System.out.println("TinyNode: sys writei "+res);
	}
	else if(opcode.equals("WRITEF")){
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "writer", res));
	    //System.out.println("TinyNode: sys writer "+res);
	}
	else if(opcode.equals("WRITES")){
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "writes", res));
	    //System.out.println("TinyNode: sys writes "+res);
	}
	else if(opcode.equals("READI")){
      	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "readi", res));
	    //System.out.println("TinyNode: sys readi "+res);
	}
	else if(opcode.equals("READF")){
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "readr", res));
	    //System.out.println("TinyNode: sys readr "+res);
	}
	else if(opcode.equals("STOREI")){
	    String op1 = tinyFormat(irNode.op1);
	    String res = tinyFormat(irNode.res);
	    if(op1.substring(0,1).equals("r") || res.substring(0,1).equals("r")){
	 	tinyList.add(new TinyNode("move", op1, res));
	   	//System.out.println("TinyNode: move "+op1+" "+res);
	    }
	    else {
		String tmpreg = createTinyReg();
		tinyList.add(new TinyNode("move", op1, tmpreg));
		tinyList.add(new TinyNode("move", tmpreg, res));
	    }
	    
	}
	else if(opcode.equals("STOREF")){
	    String op1 = tinyFormat(irNode.op1);
	    String res = tinyFormat(irNode.res);

	    if(op1.substring(0,1).equals("r") || res.substring(0,1).equals("r")){
	 	tinyList.add(new TinyNode("move", op1, res));
	   	//System.out.println("TinyNode: move "+op1+" "+res);
	    }
	    else {
		String tmpreg = createTinyReg();
		tinyList.add(new TinyNode("move", op1, tmpreg));
		tinyList.add(new TinyNode("move", tmpreg, res));
	    }

	}
	else if(opcode.equals("ADDI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("addi", op2, res));
	    //tinyList.add(new TinyNode("addi", op2, op1));	
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: addi "+op2+" "+res);
	}
	else if(opcode.equals("ADDF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("addr", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: addr "+op2+" "+res);
	    //tinyList.add(new TinyNode("addr", op2, op1));
	}
	else if(opcode.equals("SUBI")){
    	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("subi", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: subi "+op2+" "+res);
	    //tinyList.add(new TinyNode("subi", op2, op1));
	}
	else if(opcode.equals("SUBF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("subr", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: subr "+op2+" "+res);
	    //tinyList.add(new TinyNode("subr", op2, op1));
	}
	else if(opcode.equals("MULTI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("muli", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: multi "+op2+" "+res);
	    //tinyList.add(new TinyNode("muli", op2, op1));
	}
	else if(opcode.equals("MULTF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("mulr", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: mulr "+op2+" "+res);
	    //tinyList.add(new TinyNode("mulr", op2, op1));
	}
	else if(opcode.equals("DIVI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("divi", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: divi "+op2+" "+res);
	    //tinyList.add(new TinyNode("divi", op2, op1));
	}
	else if(opcode.equals("DIVF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("divr", op2, res));
	    //System.out.println("TinyNode: move "+op1+" "+res);
	    //System.out.println("TinyNode: divr "+op2+" "+res);
	    //tinyList.add(new TinyNode("divr", op2, op1));
	}
	else if(opcode.equals("EQ")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){
	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);

	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jeq", null, res));
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jeq "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jeq", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jeq "+res);
	    }
	    
	}
	else if(opcode.equals("NE")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){
	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);

	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jne", null, res));
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jne "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jne", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jne "+res);
	    }
	}
	else if(opcode.equals("GE")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){
	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jge", null, res));
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jge "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jge", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jge "+res);
	    }
	    
	}
	else if(opcode.equals("LE")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){

	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    //System.out.println("type = "+type);
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jle", null, res));
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jle "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jle", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jle "+res);
	    }
	}
	else if(opcode.equals("GT")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){
	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jgt", null, res));	 
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jgt "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jgt", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jgt "+res);
	    }
	}
	else if(opcode.equals("LT")){
	    String type = SymbolVarNamesHM.get(irNode.op1);
	    if(type == null){
	    	type = currFunc.parameterType.get(irNode.op1.substring(1));
	    }
	    if(type.equals("INT")){
	    	cmp = "cmpi";
	    }
	    else{
		cmp = "cmpr";
 	    }
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    String check = checkRegister(op2);
	    if(check.equals(op2)){
		tinyList.add(new TinyNode(cmp, op1, op2));
	    	tinyList.add(new TinyNode("jlt", null, res));
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+op2);
	        //System.out.println("TinyNode: jlt "+res);
	    }
	    else{
		tinyList.add(new TinyNode("move", op2, check));
		tinyList.add(new TinyNode(cmp, op1, check));
	    	tinyList.add(new TinyNode("jlt", null, res));
		//System.out.println("TinyNode: move "+op2+" "+check);
	        //System.out.println("TinyNode: "+cmp+" "+op1+" "+check);
	        //System.out.println("TinyNode: jlt "+res);
	    }
	}
	else if(opcode.equals("LABEL")){
	    //initialize tinyFunction so other tinyNodes have access to variables
	    for(int i=0; i<functionList.size(); i++){
		if(functionList.get(i).functionName.equals(irNode.op1)){
		    tinyFunction = functionList.get(i);		
		}
	    }

	    tinyList.add(new TinyNode("label", irNode.op1, null));
	    //System.out.println("TinyNode: label "+irNode.op1);
	}
	else if(opcode.equals("JUMP")){
	    tinyList.add(new TinyNode("jmp", irNode.op1, null));
	    //System.out.println("TinyNode: jmp "+irNode.op1);
	}
	else if(opcode.equals("JSR")){
	    tinyList.add(new TinyNode("push", "r0", null));
	    tinyList.add(new TinyNode("push", "r1", null));
	    tinyList.add(new TinyNode("push", "r2", null));
	    tinyList.add(new TinyNode("push", "r3", null));
	    tinyList.add(new TinyNode("jsr", irNode.op1, null));
	    tinyList.add(new TinyNode("pop", "r3", null));
	    tinyList.add(new TinyNode("pop", "r2", null));
	    tinyList.add(new TinyNode("pop", "r1", null));
	    tinyList.add(new TinyNode("pop", "r0", null));
	    //System.out.println("TinyNode: push r0-r3");
	    //System.out.println("TinyNode: jsr "+irNode.op1);
	    //System.out.println("TinyNode: pop r0-r3");
	   	
	}
	else if(opcode.equals("PUSH")) {
	    String op1 = tinyFormat(irNode.op1);
	    tinyList.add(new TinyNode("push", op1, null));
	    //System.out.println("TinyNode: push "+op1);	
	}
	else if(opcode.equals("POP")) {
	    String op1 = tinyFormat(irNode.op1);
	    tinyList.add(new TinyNode("pop", op1, null));
	    //System.out.println("TinyNode: pop "+op1);	
	}
	else if(opcode.equals("LINK")){
	    int localCount = tinyFunction.LocalVarCount;
	    String linkCount;
	    if(localCount == 0){
		linkCount = null;
	    }
	    else {
		linkCount = Integer.toString(localCount);
	    }
	    tinyList.add(new TinyNode("link", linkCount, null));
	    //System.out.println("TinyNode: link");	
	}
	else {//if(opcode.equals("RET") {
	    //System.out.println("RET");
	    tinyList.add(new TinyNode("unlnk", null, null));
	    tinyList.add(new TinyNode("ret", null, null));	
	   // System.out.println("TinyNode: unlnk");
	    //System.out.println("TinyNode: ret");
	}

	//System.out.println("At end of createTiny!");
	

    }

    //IR Code Generation

    public static void printHashMap() {
	/*
	Iterator it = SymbolVarNamesHM.entrySet().iterator();
	while (it.hasNext()) {
	    HashMap.Entry pair = (HashMap.Entry)it.next();
	    System.out.println(pair.getKey() + " = " + pair.getValue());
	}
	*/
	//System.out.println("\nPrinting the hash map.");
	for (String key : SymbolVarNamesHM.keySet()) {
	    //System.out.println(key + " = " + SymbolVarNamesHM.get(key));
	}
    }
    public static void checkLeafType(ASTnode leaf) {
	//check to see if leaf node is an INTLITERAL or a FLOATLITERAL
	//System.out.println("!!!!!!!!!!!!!!HIT A LEAF NODE!!!!!!!!!!!!!!!!!!!!!!!!");
	//System.out.println("Leaf Node: "+leaf.text);	
	boolean isValidInteger = false;

	try {
	    //System.out.println("CHECKING LEAF TYPE: "+leaf.text);
	    Integer.parseInt(leaf.text);
	    isValidInteger = true;
	    //System.out.println("LEAF IS AN INTEGER");
	    register = createRegister();
	    function.irnodelist.add(new IRnode("STOREI", checkLocal(leaf.text), null, register));
	    leaf.text = register;
	    
	    SymbolVarNamesHM.put(register, "INT");
	}
	catch (NumberFormatException ex) {
	    //System.out.println(leaf.text +" IS NOT AN INTEGER, TYPE: "+SymbolVarNamesHM.get(leaf.text));	
	    if(SymbolVarNamesHM.get(leaf.text) != null) {
		//System.out.println("LEAF IS IN THE HM === IT IS A VARIABLE");		
		return;
	    }
	    else { //leaf is float
		//System.out.println("LEAF IS A FLOAT");
		register = createRegister();
		function.irnodelist.add(new IRnode("STOREF", checkLocal(leaf.text), null, register));
		leaf.text = register;
		
		SymbolVarNamesHM.put(register, "FLOAT");
	    }
	}
	
    }

    public static int getChildCount(ASTnode node) {
	//System.out.println("in GETCHILDCOUNT");
	if(node.leftChild == null && node.rightChild == null) {
	    childCount = 0;
	    return(0);	
	}
	else {
	    childCount = 1;
	    return(1);	
	}
    }
    public static void PostOrderTraversal(ASTnode root) {
	//System.out.println("In POTTRAVERSAL");
	String label;
	
	//System.out.println("ROOT: "+root.text);
	if(getChildCount(root) == 0) {
	    //System.out.println("Node: "+root.text+" Children: "+childCount);
	    checkLeafType(root);
	    if(returnText == 1) {
		returnStack.push(root);
	    }
	    
	    return;	
	}
	
	PostOrderTraversal(root.leftChild); //PostOrderTraversal of left side
	PostOrderTraversal(root.rightChild); //PostOrderTraversal of right side

	//Now at a non-leaf node(+,-,*,/)
	//System.out.println("Now back at Non-Leaf Node: "+root.text+ " right child: "+root.rightChild.text+ " Left child: "+root.leftChild.text);
	
	String right = root.rightChild.text;
	String left = root.leftChild.text;
	

	if(function.parameterList.get(root.leftChild.text) != null){
	    left = "$"+function.parameterList.get(root.leftChild.text);
	}
	if(function.parameterList.get(root.rightChild.text) != null){
	    right = "$"+function.parameterList.get(root.rightChild.text);
	}

	//System.out.println("Right: "+right+" Left: "+left);
	if(root.text.equals("*")) {
	    //System.out.println("in MULTIPLICATION");
	    type = SymbolVarNamesHM.get(root.leftChild.text);
	    
	    if(type.equals("INT")) {
		instr = "MULTI";
	        //System.out.println("Set Instruction MULTI");
	    }
	    else {
		instr = "MULTF";
	    }
	    //System.out.println("Creating Register");
            register = createRegister();
	    //System.out.println("Adding IR Node ---- opcode: "+instr + " op1: "+root.leftChild.text+" op2: "+root.rightChild.text+" result: "+register);
	    function.irnodelist.add(new IRnode(instr, left, right, register));
	    //System.out.println("Changing text to register");
	    root.text = register;
	    SymbolVarNamesHM.put(register, type);
	}
	else if(root.text.equals("/")) {
	    //System.out.println("Left Child Text: "+root.leftChild.text);
	    type = SymbolVarNamesHM.get(root.leftChild.text);
	    
	    if(type.equals("INT")) {
		instr = "DIVI";
	    }
	    else {
		instr = "DIVF";
	    }
	    
            register = createRegister();
	    //System.out.println("Adding IR Node ---- opcode: "+instr + " op1: "+root.leftChild.text+" op2: "+root.rightChild.text+" result: "+register);
	    function.irnodelist.add(new IRnode(instr, left, right, register));
	    root.text = register;
	    SymbolVarNamesHM.put(register, type);
	}
	else if(root.text.equals("+")) {
	    type = SymbolVarNamesHM.get(root.leftChild.text);
	    
	    if(type.equals("INT")) {
		instr = "ADDI";
	    }
	    else {
		instr = "ADDF";
	    }
	    
            register = createRegister();
	    //System.out.println("Adding IR Node ---- opcode: "+instr + " op1: "+root.leftChild.text+" op2: "+root.rightChild.text+" result: "+register);
	    function.irnodelist.add(new IRnode(instr, left, right, register));
	    root.text = register;
	    SymbolVarNamesHM.put(register, type);
	}
	else if(root.text.equals("-")) {// if(root.text.equals("-") {
		//System.out.println("In SUBTRACTION, leftChildtext = "+root.leftChild.text);
	    type = SymbolVarNamesHM.get(root.leftChild.text);
	    
	    if(type.equals("INT")) {
		instr = "SUBI";
	    }
	    else {
		instr = "SUBF";
	    }
	    
            register = createRegister();
	    //System.out.println("Adding IR Node ---- opcode: "+instr + " op1: "+root.leftChild.text+" op2: "+root.rightChild.text+" result: "+register);
	    function.irnodelist.add(new IRnode(instr, left, right, register));
	    root.text = register;
	    SymbolVarNamesHM.put(register, type);
	}
	else if(root.text.equals("<") && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "GE";
	       
            label = "label" + Integer.toString(else_label); 
	    function.irnodelist.add(new IRnode(instr, left, right, label));

	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	    
	}
	else if(root.text.equals(">")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "LE";
	       
            label = "label" + Integer.toString(else_label);

	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("<=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "GT";
  
            label = "label" + Integer.toString(else_label);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals(">=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    
	    instr = "LT";

            label = "label" + Integer.toString(else_label);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "NE";
            label = "label" + Integer.toString(else_label);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("!=")  && (inFor == 0)) {
	    //System.out.println("In != if statement");
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "EQ";
	       
            label = "label" + Integer.toString(else_label);
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}



	//for the for loop. the label values will be different here
	else if(root.text.equals("<") && (inFor == 1)) {
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();

	    instr = "GE";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));

	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	}
	else if(root.text.equals(">")  && (inFor == 1)) {
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();
	    instr = "LE";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	}
	else if(root.text.equals("<=")  && (inFor == 1)) {
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();
	    instr = "GT";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	}
	else if(root.text.equals(">=")  && (inFor == 1)) {
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();
	    instr = "LT";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	}
	else if(root.text.equals("=")  && (inFor == 1)) {
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();
	    instr = "NE";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	}
	else if(root.text.equals("!=")  && (inFor == 1)) {
	    
	    int condLabel = labelStack.pop();
	    int incrLabel = labelStack.pop();
	    int pre_condLabel = labelStack.pop();
	    
	    
	    instr = "EQ";
	       
            label = "label" + Integer.toString(condLabel);
	    
	    function.irnodelist.add(new IRnode(instr, left, right, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	    
	}
	//System.out.println("if in return statement, push node onto return stack");
	//System.out.println("Currently root text: "+root.text);
	if(returnText == 1){
	    //System.out.println("Pushing onto return stack");
	    returnStack.push(root);	
	}
	    
	
    }

    public static String createRegister() {
	regCount++;
	String regval = "$T" + Integer.toString(regCount);
	regstackframe.push(regval); //push to the stack every time a register is created
	RegisterHM.put(regval, "register");
	return regval;
    }


    public static void WriteFunc(String iden) {
	String instr;
	for(String retval: iden.split(",")) {
	    if (SymbolVarNamesHM.get(retval).equals("INT")) {
	        instr = "WRITEI";
	    }
	    else if(SymbolVarNamesHM.get(retval).equals("FLOAT")) {
	        instr = "WRITEF";
	    }
	    else {
		instr = "WRITES";
	    }
	       
	    function.irnodelist.add(new IRnode(instr, null, null, checkLocal(retval)));
        }
    }

    public static void ReadFunc(String iden) {
	String instr;
	String ident = iden;
	if(function.parameterList.get(iden) != null){
	    ident = "$"+function.parameterList.get(iden);	
	}

	if (SymbolVarNamesHM.get(iden).equals("INT")) {
	    instr = "READI";
	}
	else {
	    instr = "READF";
	}
	function.irnodelist.add(new IRnode(instr, null, null, ident));
    }

    public static void printIRnodes() {
	/*System.out.println("Printing SymbolVarNamesHM");
	for (String key : SymbolVarNamesHM.keySet()) {
	    String Value = SymbolVarNamesHM.get(key);
	    System.out.println("Key: "+key+" Value: "+Value);	
	}

	System.out.println("Pringing RegisterHM");
	for (String key : RegisterHM.keySet()) {
	    String Value = RegisterHM.get(key);
	    System.out.println("Key: "+key+" Value: "+Value);	
	}
	*/
	System.out.println(";IR code");
	for (int j = 0; j < functionList.size(); j++) {
	
	/*
            //Printing out symbol table
	    System.out.println("");
	    System.out.println("Printing Symbol Table for: "+functionList.get(j).functionName);
	    SymbolTable table = functionList.get(j).symbolTable;
	    String to_be_printed = "Symbol table " + table.scope + "\r\n";
	    System.out.print(to_be_printed);
	    for(int i = 0; i < table.SymbolVarNames.size(); i++) {
		table.SymbolVarNames.get(i).printSymbolVariable();    
	    }
	    //
	    //Printing out parameter mapping list
	    System.out.println("Printing Parameter List");
	    for(String name: functionList.get(j).parameterList.keySet()){
		String key = name.toString();
		String value = functionList.get(j).parameterList.get(name).toString();
		System.out.println("key: "+key+ " value: "+value);
	    }
	    System.out.println("");
	*/

	    //Adding "RET" at end if final node is not already return
	    int sizeofList = functionList.get(j).irnodelist.size() - 1;
	    if(!(functionList.get(j).irnodelist.get(sizeofList).instr.equals("RET"))){
		functionList.get(j).irnodelist.add(new IRnode("RET", null, null, null));
	    }

	    for (int i = 0; i < functionList.get(j).irnodelist.size(); i++ ) {
	        functionList.get(j).irnodelist.get(i).printIRnode();
	    }


	    System.out.println("");
	}
	convertToTiny();
    }

//-----------------------------------------------------------------------------------------------------

    public static int checkIfJustOneNode() { //to check if the right child of the := contains 1 node
	if (rightChild.leftChild == null) {
	    return 1;
	}
	else {
	    return 0;
	}
    }

    public static void setAST(String root, String left) {
	stackCount = 0;
	rootequals = root;
	leftChild = left;
	rightChild = null;
    }

    public static void createTerminalNode(String text) {
      
	//System.out.println("IN TERMINAL");
	ASTnode node = new ASTnode(text, null, null); //create the terminal node. leftchild and rightchild will both be null
	
	nodestackframe.push(node);
	//System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	//printStackCurr();
	stackCount++;
	//System.out.println("The element pushed to the stack: " + node.text);
	//System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	//System.out.println("Stack Count: "+stackCount);
	insideExprCount++;
    }
    
    public static void createNonTerminalNode(String text) {
	//System.out.println("IN NON TERMINAL");
	ASTnode node = new ASTnode(text, nodestackframe.pop(), null); //create the non-terminal node. rightchild will both be null initially, but will be updated along the way. leftchild can be gotten by popping the current node in the stack
	nodestackframe.push(node); //push the newly created node into the stack
	operatorSeen = "yes";
        //System.out.println("The element pushed to the stack: " + node.text);
	//System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	//System.out.println("Stack Count: "+stackCount);
	insideExprCount++;
	//printStackCurr();
    }
    
    
    public static void popFinalNode() { //this function will essentially return the final node in the stack, which will contain the entire right child of the expression as a binary tree
	//System.out.println("Pop Final Node -- Stack Count = "+stackCount);
	String finalType;
	rightChild = nodestackframe.pop();//assign to the right child
	stackCount--;	
	operatorSeen = "no";
	//System.out.println("Right Child = "+rightChild.text);
	
	if (incrStmt == 1) {
	    incrAssignment = leftChild;
	    incrFor.push(rightChild);
	    return;
	}
	
	if (checkIfJustOneNode() == 1) { //i.e of form a := b
	    //System.out.println("Of the form a := b");
	    //now we will get the kleftchild's type from the hash map
	    String typeLeftChild = SymbolVarNamesHM.get(leftChild);
	    String instr;

	    if (typeLeftChild.equals("INT")) {
		instr = "STOREI";
	    }
	    else {
		instr = "STOREF";
	    }
	    
	    if(callingFunction == 1) {
		function.irnodelist.add(new IRnode(instr, functionResult, null, checkLocal(leftChild)));
	    }
	    else {
	    	function.irnodelist.add(new IRnode(instr, checkLocal(rightChild.text), null, createRegister()));
	    	function.irnodelist.add(new IRnode(instr, regstackframe.pop(), null, checkLocal(leftChild)));
	    }

	}
	else { //tree has multiple nodes
	    
	    PostOrderTraversal(rightChild);
	    
	    finalType = SymbolVarNamesHM.get(rightChild.text);
	    if(finalType.equals("INT")) {
		instr = "STOREI";
	    }
	    else {
		instr = "STOREF";
	    }
 
	    function.irnodelist.add(new IRnode(instr, checkLocal(rightChild.text), null, checkLocal(leftChild)));
	}
    }
	
    //}
    

    public static void checkStack() {
	//System.out.println("The stack count value in checkStack(): " + stackCount);
	//System.out.println("MOVEOK: "+moveOK);

	if (moveOK == "yes") {
	    
	    while (stackCount != 1) {
		//System.out.println("And forth.");
		//System.out.println("Stack Count is now: "+stackCount);
		ASTnode node1 = nodestackframe.pop();
		//System.out.println("popped 1:" + node1.text);
		if (nodestackframe.empty()) {
		    //System.out.println("STACK IS EMPTY... EXITING TO AVOID ISSUES.");
		    nodestackframe.push(node1);
		    stackCount = 1;
		    return;
		}
		ASTnode node2 = nodestackframe.pop();
		//System.out.println("node1: "+node1.text+" node2: "+node2.text);
		nodestackframe.push(node2);
		nodestackframe.push(node1);
		moveRightChildUp();
		//factorRecognized = 0;
		//System.out.println("in move ok yes. Stack Count = "+stackCount);
	    }
	}
	else {//not move ok
	    /*if (stackCount == 2) {//only one move ups is possible
		moveRightChildUp();
		return;
	    }*/
	    /*if (exprStackCount == 0) {//basically to take of egde case
		exprStackCount = 1;
		return;
	    }*/
	    while (stackCount != (exprStackCount + 1)) {
		//System.out.println("exprStackCount :" + exprStackCount);
		//System.out.println("IN THE OTHER CASE ");
		moveRightChildUp();
		//moveOK = "yes";
		}
	}
	//System.out.println("Getting out of checkStack().");
    }
    
    public static void dontMove(int move) {
	if(move == 1) {
	    moveOK = "no";
	}
	else {
	    moveOK = "yes";
	}
    }
	
    public static void moveRightChildUp() { //this function will move up one level the right child
	//System.out.println("Move Right Child Up");
	//System.out.println("operator seen: "+operatorSeen);
	if (insideExprCount == 1){
	    factorRecognized = 0;
	}
	    if(moveOK == "no"  && factorRecognized != 1) {
		//System.out.println("Back.");
		//System.out.println("HERE..");
		NUM_OF_TIMES_NOT_HIT++;
		if(NUM_OF_TIMES_NOT_HIT == 2) {
		    moveOK = "yes";
		    NUM_OF_TIMES_NOT_HIT = 0;
		}
		return;
	    }
	    else{
		//System.out.println("Move ok value: " + moveOK);
		//System.out.println("factorRecognized value:" + factorRecognized);
		if (operatorSeen == "no") { //only one terminal node was present then just return
		    //printStackCurr();
		    //System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
		    //System.out.println("Stack Count: "+stackCount);
		    return;
		}
		else { //at least moving up needs to be done
		    ASTnode right = nodestackframe.pop(); //get the right node
		    //System.out.println("The child to be joined: " + right.text); 
		    ASTnode parent = nodestackframe.pop(); //get the parent. They are always going to be the topmost two
		    //System.out.println("The parent to be joined to: " + parent.text);
		    parent.rightChild = right; //make the assignment
		    //System.out.println("After the move up is complete");
		    //System.out.println("The inorder traversal of the recently joined nodes...");
		    inorderTraversal(parent);
		    nodestackframe.push(parent); //now push the parent right back to the stack
		    //System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
		    //printStackCurr();
		    factorRecognized = 0;
		    stackCount--;
		    //System.out.println("\nStack Count: " + stackCount);
		    return;
		}
	    }
	
    }
    
    public static void print() { //print using inorder traversal ->called only from grammar file
	//System.out.println("Printing in Print");
	/*
	//System.out.println("Temporarily checking the root right child content...");
	//System.out.println("RightChild Text = " + rightChild.text);
	//System.out.println("Left of Right =" + rightChild.leftChild.text);
	//System.out.println("Right of Right =" + rightChild.rightChild.text);
	*/
	//System.out.println("The inorder traversal...");
        inorderTraversal(rightChild); //print starting from the right child
	//System.out.print("\n");
	//System.out.println("Stack count now (should be 0):" + Integer.toString(stackCount));
    }

    public static void inorderTraversal(ASTnode curr) {
	if (curr == null) {
	    //System.out.print(")");
	    return;
	}
	//System.out.print("(");
	inorderTraversal(curr.leftChild);
	//System.out.print("(");
	//System.out.print(curr.text);
	inorderTraversal(curr.rightChild);
	//System.out.print("end");
	//System.out.print(")");
	//System.out.print(")");
	
    }
	
    public static void printStackCurr() {
	
	ASTnode temp = nodestackframe.pop();
	inorderTraversal(temp);
	nodestackframe.push(temp);
    }
	
}

