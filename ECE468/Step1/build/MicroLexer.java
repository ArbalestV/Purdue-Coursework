// Generated from Micro.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MicroLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.5.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WHITESPACE=1, KEYWORD=2, IDENTIFIER=3, INTLITERAL=4, FLOATLITERAL=5, STRINGLITERAL=6, 
		COMMENT=7, OPERATOR=8;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"WHITESPACE", "KEYWORD", "IDENTIFIER", "INTLITERAL", "FLOATLITERAL", "STRINGLITERAL", 
		"COMMENT", "OPERATOR"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "WHITESPACE", "KEYWORD", "IDENTIFIER", "INTLITERAL", "FLOATLITERAL", 
		"STRINGLITERAL", "COMMENT", "OPERATOR"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MicroLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Micro.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\n\u00ad\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3i\n\3\3\4\6\4l\n\4"+
		"\r\4\16\4m\3\4\7\4q\n\4\f\4\16\4t\13\4\3\4\7\4w\n\4\f\4\16\4z\13\4\3\5"+
		"\6\5}\n\5\r\5\16\5~\3\6\7\6\u0082\n\6\f\6\16\6\u0085\13\6\3\6\3\6\7\6"+
		"\u0089\n\6\f\6\16\6\u008c\13\6\3\7\3\7\7\7\u0090\n\7\f\7\16\7\u0093\13"+
		"\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b\u009b\n\b\f\b\16\b\u009e\13\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ac\n\t\2\2\n\3\3\5\4\7\5"+
		"\t\6\13\7\r\b\17\t\21\n\3\2\n\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62;\4\2"+
		"))\60\60\3\2$$\3\2\f\f\6\2,-//\61\61??\6\2*+..=>@@\u00ca\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\2\21\3\2\2\2\3\23\3\2\2\2\5h\3\2\2\2\7k\3\2\2\2\t|\3\2\2\2\13\u0083"+
		"\3\2\2\2\r\u008d\3\2\2\2\17\u0096\3\2\2\2\21\u00ab\3\2\2\2\23\24\t\2\2"+
		"\2\24\4\3\2\2\2\25\26\7R\2\2\26\27\7T\2\2\27\30\7Q\2\2\30\31\7I\2\2\31"+
		"\32\7T\2\2\32\33\7C\2\2\33i\7O\2\2\34\35\7D\2\2\35\36\7G\2\2\36\37\7I"+
		"\2\2\37 \7K\2\2 i\7P\2\2!\"\7G\2\2\"#\7P\2\2#i\7F\2\2$%\7H\2\2%&\7W\2"+
		"\2&\'\7P\2\2\'(\7E\2\2()\7V\2\2)*\7K\2\2*+\7Q\2\2+i\7P\2\2,-\7T\2\2-."+
		"\7G\2\2./\7C\2\2/i\7F\2\2\60\61\7Y\2\2\61\62\7T\2\2\62\63\7K\2\2\63\64"+
		"\7V\2\2\64i\7G\2\2\65\66\7K\2\2\66i\7H\2\2\678\7G\2\289\7N\2\29:\7U\2"+
		"\2:i\7G\2\2;<\7H\2\2<i\7K\2\2=>\7H\2\2>?\7Q\2\2?i\7T\2\2@A\7T\2\2AB\7"+
		"Q\2\2Bi\7H\2\2CD\7E\2\2DE\7Q\2\2EF\7P\2\2FG\7V\2\2GH\7K\2\2HI\7P\2\2I"+
		"J\7W\2\2Ji\7G\2\2KL\7D\2\2LM\7T\2\2MN\7G\2\2NO\7C\2\2Oi\7M\2\2PQ\7T\2"+
		"\2QR\7G\2\2RS\7V\2\2ST\7W\2\2TU\7T\2\2Ui\7P\2\2VW\7K\2\2WX\7P\2\2Xi\7"+
		"V\2\2YZ\7X\2\2Z[\7Q\2\2[\\\7K\2\2\\i\7F\2\2]^\7U\2\2^_\7V\2\2_`\7T\2\2"+
		"`a\7K\2\2ab\7P\2\2bi\7I\2\2cd\7H\2\2de\7N\2\2ef\7Q\2\2fg\7C\2\2gi\7V\2"+
		"\2h\25\3\2\2\2h\34\3\2\2\2h!\3\2\2\2h$\3\2\2\2h,\3\2\2\2h\60\3\2\2\2h"+
		"\65\3\2\2\2h\67\3\2\2\2h;\3\2\2\2h=\3\2\2\2h@\3\2\2\2hC\3\2\2\2hK\3\2"+
		"\2\2hP\3\2\2\2hV\3\2\2\2hY\3\2\2\2h]\3\2\2\2hc\3\2\2\2i\6\3\2\2\2jl\t"+
		"\3\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2nr\3\2\2\2oq\t\4\2\2po\3"+
		"\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2sx\3\2\2\2tr\3\2\2\2uw\t\3\2\2vu\3"+
		"\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\b\3\2\2\2zx\3\2\2\2{}\t\4\2\2|{"+
		"\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\n\3\2\2\2\u0080\u0082\t"+
		"\4\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083"+
		"\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u008a\t\5"+
		"\2\2\u0087\u0089\t\4\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a"+
		"\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\f\3\2\2\2\u008c\u008a\3\2\2\2"+
		"\u008d\u0091\7$\2\2\u008e\u0090\n\6\2\2\u008f\u008e\3\2\2\2\u0090\u0093"+
		"\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093"+
		"\u0091\3\2\2\2\u0094\u0095\7$\2\2\u0095\16\3\2\2\2\u0096\u0097\7/\2\2"+
		"\u0097\u0098\7/\2\2\u0098\u009c\3\2\2\2\u0099\u009b\n\7\2\2\u009a\u0099"+
		"\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d"+
		"\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7\f\2\2\u00a0\20\3\2\2"+
		"\2\u00a1\u00a2\7<\2\2\u00a2\u00ac\7?\2\2\u00a3\u00ac\t\b\2\2\u00a4\u00a5"+
		"\7#\2\2\u00a5\u00ac\7?\2\2\u00a6\u00ac\t\t\2\2\u00a7\u00a8\7>\2\2\u00a8"+
		"\u00ac\7?\2\2\u00a9\u00aa\7@\2\2\u00aa\u00ac\7?\2\2\u00ab\u00a1\3\2\2"+
		"\2\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7"+
		"\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\22\3\2\2\2\r\2hmrx~\u0083\u008a\u0091"+
		"\u009c\u00ab\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}