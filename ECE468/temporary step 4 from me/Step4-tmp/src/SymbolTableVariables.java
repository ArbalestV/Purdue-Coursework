public class SymbolTableVariables {
    
    public String variable_name;
    public String variable_type;
    public String string_value;
    
    public SymbolTableVariables( String variable_name, String variable_type, String string_value) {
	this.variable_name = variable_name;
	this.variable_type = variable_type;
	this.string_value = string_value;
    }
    
    
    public void printSymbolVariable() {
	if((this.variable_type.equals("FLOAT")) || (this.variable_type.equals("INT"))) {
		System.out.print("name " + this.variable_name + " type " + this.variable_type + "\r\n");
	}
	else {
	    System.out.print("name " + this.variable_name + " type " + this.variable_type + " value " + this.string_value + "\r\n");
	}
    }
}
