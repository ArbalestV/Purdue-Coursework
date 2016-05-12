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
	irnodelist.add(new IRnode(storeType, right.text, null , incrAssignment));
		
    }

    public static void for_label(int i) {
	int condLabel = labelStack.pop();
	int incrLabel = labelStack.pop();
	int pre_condLabel = labelStack.pop();

	if(i == 1){
	    irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(pre_condLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if(i == 2){
	    irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(incrLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if( i == 3) {
	    irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(pre_condLabel), null, null));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	}
	if(i == 4){
	    irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(condLabel), null, null));
	}

    }

    public static void jump_label(int i) {
	int exit_label = labelStack.pop();
	int else_label = labelStack.pop();

	if( i == 1) {
	    //System.out.println("Value1: "+value1 + " Value2: "+value2);
	    irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(exit_label), null, null));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(i == 2) {
	    irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(else_label), null, null));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);	
	}
	else if(i == 3) {
	    irnodelist.add(new IRnode("JUMP", "label"+Integer.toString(exit_label), null, null));	
	    labelStack.push(else_label);
	    labelStack.push(exit_label);	
	}
	else {//if(i == 4) {
	    irnodelist.add(new IRnode("LABEL", "label"+Integer.toString(exit_label), null, null));		
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

    //Tiny Code Generation
    public static void printTinyCode() {
	tinyList.add(new TinyNode("sys", "halt", null));
	for (int i = 0; i < tinyList.size(); i++ ) {
	    tinyList.get(i).printTiny();
	}	
    }

    public static void convertToTiny() {
	//System.out.println("IN TINY CONVERSION");
    	for (String key : SymbolVarNamesHM.keySet()) {
	    if(key.substring(0,1).equals("$")) {
	    }
	    else {
		tinyList.add(new TinyNode("var", key, null));
	    }
	}
	//System.out.println("irnodelist.size(): "+irnodelist.size());
	//System.out.println("Scanning through IR list");
	for(int i=0; i < irnodelist.size(); i++) {
	    //System.out.println("in createTiny loop");
	    createTiny(irnodelist.get(i));	
	}
	System.out.println(";tiny code");
	printTinyCode();

    }
    
    public static String tinyFormat(String opcode) {
	//System.out.println("in tinyFormat");
	String tinyOp = opcode;	
	if(opcode.substring(0,1).equals("$")){
	    int count = Integer.parseInt(opcode.substring(2));
	    count = count - 1;
	    String regNum = Integer.toString(count);
	    tinyOp = "r"+regNum;
	}

	return tinyOp;
    }

    public static void createTiny(IRnode irNode) {
	//System.out.println("IRNODE: instr: "+irNode.instr+" op1: "+irNode.op1+" op2: "+irNode.op2+" res: "+irNode.res);
	String opcode = irNode.instr;

	if(opcode.equals("WRITEI")) {
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "writei", res));
	}
	else if(opcode.equals("WRITEF")){
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "writer", res));
	}
	else if(opcode.equals("READI")){
      	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "readi", res));
	}
	else if(opcode.equals("READF")){
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("sys", "readf", res));
	}
	else if(opcode.equals("STOREI")){
	    String op1 = tinyFormat(irNode.op1);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	}
	else if(opcode.equals("STOREF")){
	    String op1 = tinyFormat(irNode.op1);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	}
	else if(opcode.equals("ADDI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("addi", op2, res));	
	}
	else if(opcode.equals("ADDF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("addr", op2, res));
	}
	else if(opcode.equals("SUBI")){
    	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("subi", op2, res));
	}
	else if(opcode.equals("SUBF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("subr", op2, res));
	}
	else if(opcode.equals("MULTI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("muli", op2, res));
	}
	else if(opcode.equals("MULTF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("mulr", op2, res));
	}
	else if(opcode.equals("DIVI")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("divi", op2, res));
	}
	else if(opcode.equals("DIVF")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("move", op1, res));
	    tinyList.add(new TinyNode("divr", op2, res));
	}
	else if(opcode.equals("EQ")){
	    String op1 = tinyFormat(irNode.op1);
	    String op2 = tinyFormat(irNode.op2);
	    String res = tinyFormat(irNode.res);
	    tinyList.add(new TinyNode("cmp", op1, op2));
	    tinyList.add(new TinyNode("jeq", null, res));
	}
	else if(opcode.equals("NE")){
	}
	else if(opcode.equals("GE")){
	}
	else if(opcode.equals("LE")){
	}
	else if(opcode.equals("GT")){
	}
	else if(opcode.equals("LT")){
	}
	else if(opcode.equals("LABEL")){
	    tinyList.add(new TinyNode("label", irNode.op1, null));
	}
	else {//if(opcode.equals("JUMP")){
	    tinyList.add(new TinyNode("jmp", irNode.op1, null));
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
	    irnodelist.add(new IRnode("STOREI", leaf.text, null, register));
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
		irnodelist.add(new IRnode("STOREF", leaf.text, null, register));
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
	    return;	
	}
	//System.out.println("Root: "+root.text+" Right Child: " +root.rightChild.text+" Left Child: "+root.leftChild.text);
	PostOrderTraversal(root.leftChild); //PostOrderTraversal of left side
	PostOrderTraversal(root.rightChild); //PostOrderTraversal of right side

	//Now at a non-leaf node(+,-,*,/)
	//System.out.println("Now back at Non-Leaf Node: "+root.text);
	
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
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, register));
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
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, register));
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
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, register));
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
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, register));
	    root.text = register;
	    SymbolVarNamesHM.put(register, type);
	}
	else if(root.text.equals("<") && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "GE";
	       
            label = "label" + Integer.toString(else_label); 
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));

	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	    
	}
	else if(root.text.equals(">")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "LE";
	       
            label = "label" + Integer.toString(else_label);

	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("<=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "GT";
  
            label = "label" + Integer.toString(else_label);
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals(">=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    
	    instr = "LT";

            label = "label" + Integer.toString(else_label);
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("=")  && (inFor == 0)) {
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "NE";
            label = "label" + Integer.toString(else_label);
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
	    labelStack.push(else_label);
	    labelStack.push(exit_label);
	}
	else if(root.text.equals("!=")  && (inFor == 0)) {
	    //System.out.println("In != if statement");
	    int exit_label = labelStack.pop();
	    int else_label = labelStack.pop();
	    instr = "EQ";
	       
            label = "label" + Integer.toString(else_label);
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));

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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
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
	    
	    irnodelist.add(new IRnode(instr, root.leftChild.text, root.rightChild.text, label));
	    labelStack.push(pre_condLabel);
	    labelStack.push(incrLabel);
	    labelStack.push(condLabel);
	    
	    
	}
	
	    
	
    }

    public static String createRegister() {
	regCount++;
	String regval = "$T" + Integer.toString(regCount);
	regstackframe.push(regval); //push to the stack every time a register is created
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
	       
	    irnodelist.add(new IRnode(instr, null, null, retval));
        }
    }

    public static void ReadFunc(String iden) {
	String instr;
	if (SymbolVarNamesHM.get(iden).equals("INT")) {
	    instr = "READI";
	}
	else {
	    instr = "READF";
	}
	irnodelist.add(new IRnode(instr, null, null, iden));
    }

    public static void printIRnodes() {
	System.out.println(";IR code");
	for (int i = 0; i < irnodelist.size(); i++ ) {
	    irnodelist.get(i).printIRnode();
	}
	//convertToTiny();
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
	/*if(stackCount != 1) {
	    moveRightChildUp();
	    }*/
	String finalType;

	rightChild = nodestackframe.pop();//assign to the right child
	//System.out.println("AT THE END. WILL PRINT THE FINAL CONTENTS OF STACK.");
	/*
	//System.out.println("Temporarily checking the root right child content...");
	//System.out.println("RightChild Text = " + rightChild.text);
	//System.out.println("Left of Right =" + rightChild.leftChild.text);
	//System.out.println("Right of Right =" + rightChild.rightChild.text);
	*/
	stackCount--;
	//System.out.println("Stack count after supposedly popping the last element: " + stackCount);
	operatorSeen = "no";
	if (incrStmt == 1) {
	    //System.out.println("popFinalNode increment");
	    incrAssignment = leftChild;
	    incrFor.push(rightChild);
	    //System.out.println("end of pop");
	    return;
	}
	
	if (checkIfJustOneNode() == 1) { //i.e of form a := b
	    //System.out.println("Of the form a := b");
	    //now we will get the kleftchild's type from the hash map
	    String typeLeftChild = SymbolVarNamesHM.get(leftChild);
	    //System.out.println("LeftChild = " + leftChild);
	    //System.out.println("TypeLeftChild = " + typeLeftChild);
	    String instr;
	    if (typeLeftChild.equals("INT")) {
		instr = "STOREI";
	    }
	    else {
		instr = "STOREF";
	    }
	    irnodelist.add(new IRnode(instr, rightChild.text, null, createRegister()));
	    irnodelist.add(new IRnode(instr, regstackframe.pop(), null, leftChild));
	    //printIRnodes();
	}
	else { //tree has multiple nodes
	    //System.out.println("ABOUT TO ENTER TRAVERSAL");
	    PostOrderTraversal(rightChild);
	    //System.out.println("Finished POTTraversal, type of RC: "+SymbolVarNamesHM.get(rightChild.text));
	    finalType = SymbolVarNamesHM.get(rightChild.text);
	    if(finalType.equals("INT")) {
		instr = "STOREI";
	    }
	    else {
		instr = "STOREF";
	    }
 
	    irnodelist.add(new IRnode(instr, rightChild.text, null, leftChild));
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

