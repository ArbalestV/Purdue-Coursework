import java.util.*;

public class IRnode {
    public String instr;
    public String op1;
    public String op2;
    public String res;
    
    public IRnode(String instr, String op1, String op2, String res) {
	this.instr = instr;
	this.op1 = op1;
	this.op2 = op2;
	this.res = res;
    }
    public void printIRnode() {
	if(instr.equals("WRITEI") || instr.equals("WRITEF") 
	   ||instr.equals("READI") || instr.equals("READF")) {
	    System.out.println(instr + " " + res);
	}
	else {
	    System.out.println(instr + " " + op1 + " " + res);
	}
    }
}
