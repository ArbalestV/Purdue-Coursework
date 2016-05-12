// Generated from Micro.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MicroParser}.
 */
public interface MicroListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MicroParser#whitespace}.
	 * @param ctx the parse tree
	 */
	void enterWhitespace(MicroParser.WhitespaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link MicroParser#whitespace}.
	 * @param ctx the parse tree
	 */
	void exitWhitespace(MicroParser.WhitespaceContext ctx);
}