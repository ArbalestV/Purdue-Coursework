import org.antlr.v4.runtime.*;
import org.antlr.runtime.debug.*;
import org.stringtemplate.v4.*;
import java.io.IOException;

public class CustomErrorStrategy extends DefaultErrorStrategy{

    public void reportError(Parser parser, RecognitionException e) {
	//System.out.print("Not accepted\r\n");
	throw new RuntimeException(e);
    }
    
    public boolean inErrorRecoveryMode(Parser parser) {
	return false;
	}
    
    public Token recoverInLine(Parser parser) throws RecognitionException {
	//System.out.print("Not accepted\r\n");
	throw new RuntimeException(new InputMismatchException(parser));
    }
}
