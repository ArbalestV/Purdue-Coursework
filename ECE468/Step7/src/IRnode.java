import java.util.*;

public class IRnode {
    public String instr;
    public String op1;
    public String op2;
    public String res;

    public int lineNum;
    public ArrayList<Integer> successors = new ArrayList<Integer>();
    public ArrayList<Integer> predecessors = new ArrayList<Integer>();

    public ArrayList<String> GEN = new ArrayList<String>();
    public ArrayList<String> KILL = new ArrayList<String>();

    public ArrayList<String> LiveIn = new ArrayList<String>();
    public ArrayList<String> LiveOut = new ArrayList<String>();

    public boolean removed = false;
    
    public IRnode(String instr, String op1, String op2, String res, int lineNum) {
	this.instr = instr;
	this.op1 = op1;
	this.op2 = op2;
	this.res = res;
	this.lineNum = lineNum;
    }
    public void printIRnode() {
	System.out.println("");
	if(instr.equals("WRITEI") || instr.equals("WRITEF") || instr.equals("WRITES")
	   ||instr.equals("READI") || instr.equals("READF") || instr.equals("READS")){
	    System.out.print(";"+instr + " " + res);
	}
	else if ( (op1 == null) && (op2 == null) && (res == null)) {
	    System.out.print(";"+instr);	
	}
	else if ( (op2 == null) && (res == null)) {
		System.out.print(";"+instr + " " + op1);
	}
	else if(op2 == null){
	    System.out.print(";"+instr + " " + op1 + " " + res);
	}
	else if(op1 == null){
	    System.out.print(";"+instr + " " + op2 + " " + res);
	}
	else {
	    System.out.print(";"+instr + " " + op1 + " " + op2 + " " + res);
	}
	/*System.out.print("  GEN: ");
	for(String gens: GEN){
	    System.out.print(gens);
	    System.out.print(" ");
	}
	
	System.out.print("   KILL: ");
	for(String kills: KILL){
	    System.out.print(kills);
	    System.out.print(" ");
	}
	if(LiveIn != null){
	System.out.print("	LiveIN: ");
	for(String liveinvar : LiveIn){
	    System.out.print(liveinvar);
	    System.out.print(" ");
	}
	}*/
	if(LiveOut != null){
	System.out.print("	LiveOUT: ");
	for(String liveoutvar: LiveOut){
	    System.out.print(liveoutvar);
	    System.out.print(" ");
	}
	}

    }
}
