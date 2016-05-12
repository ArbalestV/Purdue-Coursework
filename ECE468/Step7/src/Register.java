import java.util.*;

public class Register {
    public int num;
    public boolean isDirty;
    public String varStored;


    public Register(int num, boolean isDirty, String varStored){
	this.num = num;
	this.isDirty = isDirty;
	this.varStored = varStored;
    }
}
