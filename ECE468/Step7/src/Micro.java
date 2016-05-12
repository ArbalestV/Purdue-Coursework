import org.antlr.v4.runtime.*;
//import org.antlr.runtime.*;
//import org.antlr.runtime.tree.*;
import org.antlr.runtime.debug.*;
import org.stringtemplate.v4.*;
import java.io.IOException;



public class Micro {
	public static void main(String[] args) throws IOException {
		ANTLRFileStream input = new ANTLRFileStream(args[0]);
		MicroLexer lexer = new MicroLexer(input);
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		tokens.setTokenSource(lexer);

		MicroParser parser = new MicroParser(tokens);
		
		ANTLRErrorStrategy es = new CustomErrorStrategy();
                try{
			parser.setErrorHandler(es);
			parser.program();
		}
                catch (RuntimeException e){
		}

	}

    public static String tokenType(int tok_id) {
	String type_tok = null;
	switch (tok_id) {
	case MicroLexer.WHITESPACE:
	    type_tok = "WHITESPACE";
	    break;

	case MicroLexer.IDENTIFIER:
	    type_tok = "IDENTIFIER";
	    break;
	case MicroLexer.INTLITERAL:
	    type_tok = "INTLITERAL";
	    break;
	case MicroLexer.FLOATLITERAL:
	    type_tok = "FLOATLITERAL";
	    break;
	case MicroLexer.STRINGLITERAL:
	    type_tok = "STRINGLITERAL";
	    break;
	case MicroLexer.COMMENT:
	    type_tok = "COMMENT";
	    break;
	case MicroLexer.KEYWORD:
	    type_tok = "KEYWORD";
	    break;
	case MicroLexer.OPERATOR:
	    type_tok = "OPERATOR";
	    break;
	default:
	    break;
	}
	return type_tok;
    }
	    
}
