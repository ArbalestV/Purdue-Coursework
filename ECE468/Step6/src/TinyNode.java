import java.util.*;

public class TinyNode {
    public String opcode;
    public String op1;
    public String op2;
    
    public TinyNode(String opcode, String op1, String op2) {
	this.opcode = opcode;
	this.op1 = op1;
	this.op2 = op2;
    }

    public void printTiny() {
	if (op1 == null && op2 == null) {
	    System.out.println(opcode);
	}
	else if(op1 == null) {
	    System.out.println(opcode + " " + op2);	
	}
	else if	(op2 == null) {
	    System.out.println(opcode + " " + op1);	
	}
	else {
	    System.out.println(opcode + " " + op1 + " " + op2);
	}
    }
}

