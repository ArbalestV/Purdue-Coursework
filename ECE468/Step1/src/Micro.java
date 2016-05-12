import org.antlr.v4.runtime.*;
import java.io.IOException;

public class Micro {
	public static void main(String[] args) throws IOException {
		ANTLRFileStream input = new ANTLRFileStream(args[0]);
		MicroLexer lexer = new MicroLexer(input);

		Token tok = lexer.nextToken();
		while (tok.getType() != lexer.EOF)
		    {
			
			String type_tok = tokenType(tok.getType());
			String value_tok = tok.getText();
			if (type_tok != "WHITESPACE" 
			    && 
			    type_tok != "COMMENT") {
			    System.out.println("Token Type: " + type_tok);
			    System.out.println("Value: " + value_tok);
			}
			tok = lexer.nextToken();
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
