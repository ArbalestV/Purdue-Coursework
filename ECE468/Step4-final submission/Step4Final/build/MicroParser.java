// Generated from Micro.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MicroParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		WHITESPACE=32, KEYWORD=33, IDENTIFIER=34, INTLITERAL=35, FLOATLITERAL=36, 
		STRINGLITERAL=37, COMMENT=38, OPERATOR=39;
	public static final int
		RULE_program = 0, RULE_id = 1, RULE_pgm_body = 2, RULE_decl = 3, RULE_string_decl = 4, 
		RULE_str = 5, RULE_var_decl = 6, RULE_var_type = 7, RULE_any_type = 8, 
		RULE_id_list = 9, RULE_id_tail = 10, RULE_param_decl_list = 11, RULE_param_decl = 12, 
		RULE_param_decl_tail = 13, RULE_func_declarations = 14, RULE_func_decl = 15, 
		RULE_func_body = 16, RULE_stmt_list = 17, RULE_stmt = 18, RULE_base_stmt = 19, 
		RULE_assign_stmt = 20, RULE_assign_expr = 21, RULE_read_stmt = 22, RULE_write_stmt = 23, 
		RULE_return_stmt = 24, RULE_expr = 25, RULE_expr_prefix = 26, RULE_factor = 27, 
		RULE_factor_prefix = 28, RULE_postfix_expr = 29, RULE_call_expr = 30, 
		RULE_expr_list = 31, RULE_expr_list_tail = 32, RULE_primary = 33, RULE_addop = 34, 
		RULE_mulop = 35, RULE_if_stmt = 36, RULE_else_part = 37, RULE_cond = 38, 
		RULE_compop = 39, RULE_init_stmt = 40, RULE_incr_stmt = 41, RULE_for_stmt = 42, 
		RULE_whitespace = 43;
	public static final String[] ruleNames = {
		"program", "id", "pgm_body", "decl", "string_decl", "str", "var_decl", 
		"var_type", "any_type", "id_list", "id_tail", "param_decl_list", "param_decl", 
		"param_decl_tail", "func_declarations", "func_decl", "func_body", "stmt_list", 
		"stmt", "base_stmt", "assign_stmt", "assign_expr", "read_stmt", "write_stmt", 
		"return_stmt", "expr", "expr_prefix", "factor", "factor_prefix", "postfix_expr", 
		"call_expr", "expr_list", "expr_list_tail", "primary", "addop", "mulop", 
		"if_stmt", "else_part", "cond", "compop", "init_stmt", "incr_stmt", "for_stmt", 
		"whitespace"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'PROGRAM'", "'BEGIN'", "'END'", "'STRING'", "':='", "';'", "'FLOAT'", 
		"'INT'", "'VOID'", "','", "'FUNCTION'", "'('", "')'", "'READ'", "'WRITE'", 
		"'RETURN'", "'+'", "'-'", "'*'", "'/'", "'IF'", "'FI'", "'ELSE'", "'<'", 
		"'>'", "'='", "'!='", "'<='", "'>='", "'FOR'", "'ROF'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, "WHITESPACE", "KEYWORD", 
		"IDENTIFIER", "INTLITERAL", "FLOATLITERAL", "STRINGLITERAL", "COMMENT", 
		"OPERATOR"
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

	@Override
	public String getGrammarFileName() { return "Micro.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MicroParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Pgm_bodyContext pgm_body() {
			return getRuleContext(Pgm_bodyContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(T__0);
			setState(89);
			id();
			setState(90);
			match(T__1);
			setState(91);
			pgm_body();
			setState(92);
			match(T__2);
			 createSymbolTable.popSymbolTable(); AST.printIRnodes();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MicroParser.IDENTIFIER, 0); }
		public IdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterId(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitId(this);
		}
	}

	public final IdContext id() throws RecognitionException {
		IdContext _localctx = new IdContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pgm_bodyContext extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Func_declarationsContext func_declarations() {
			return getRuleContext(Func_declarationsContext.class,0);
		}
		public Pgm_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pgm_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterPgm_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitPgm_body(this);
		}
	}

	public final Pgm_bodyContext pgm_body() throws RecognitionException {
		Pgm_bodyContext _localctx = new Pgm_bodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_pgm_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			createSymbolTable.GlobalScopeTable();
			setState(98);
			decl();
			setState(99);
			func_declarations();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclContext extends ParserRuleContext {
		public String_declContext string_decl() {
			return getRuleContext(String_declContext.class,0);
		}
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitDecl(this);
		}
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			setState(108);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				string_decl();
				setState(102);
				decl();
				}
				break;
			case T__6:
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				var_decl();
				setState(105);
				decl();
				}
				break;
			case T__2:
			case T__10:
			case T__13:
			case T__14:
			case T__15:
			case T__20:
			case T__21:
			case T__22:
			case T__29:
			case T__30:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class String_declContext extends ParserRuleContext {
		public IdContext id;
		public StrContext str;
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public StrContext str() {
			return getRuleContext(StrContext.class,0);
		}
		public String_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterString_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitString_decl(this);
		}
	}

	public final String_declContext string_decl() throws RecognitionException {
		String_declContext _localctx = new String_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_string_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(T__3);
			setState(111);
			((String_declContext)_localctx).id = id();
			setState(112);
			match(T__4);
			setState(113);
			((String_declContext)_localctx).str = str();
			setState(114);
			match(T__5);
			createSymbolTable.insertVariable("STRING", (((String_declContext)_localctx).id!=null?_input.getText(((String_declContext)_localctx).id.start,((String_declContext)_localctx).id.stop):null), (((String_declContext)_localctx).str!=null?_input.getText(((String_declContext)_localctx).str.start,((String_declContext)_localctx).str.stop):null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StrContext extends ParserRuleContext {
		public TerminalNode STRINGLITERAL() { return getToken(MicroParser.STRINGLITERAL, 0); }
		public StrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterStr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitStr(this);
		}
	}

	public final StrContext str() throws RecognitionException {
		StrContext _localctx = new StrContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_str);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(STRINGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declContext extends ParserRuleContext {
		public Var_typeContext var_type;
		public Id_listContext id_list;
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public Id_listContext id_list() {
			return getRuleContext(Id_listContext.class,0);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterVar_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitVar_decl(this);
		}
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			((Var_declContext)_localctx).var_type = var_type();
			setState(120);
			((Var_declContext)_localctx).id_list = id_list();
			setState(121);
			match(T__5);
			createSymbolTable.insertVariable((((Var_declContext)_localctx).var_type!=null?_input.getText(((Var_declContext)_localctx).var_type.start,((Var_declContext)_localctx).var_type.stop):null), (((Var_declContext)_localctx).id_list!=null?_input.getText(((Var_declContext)_localctx).id_list.start,((Var_declContext)_localctx).id_list.stop):null), null);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_typeContext extends ParserRuleContext {
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterVar_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitVar_type(this);
		}
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_var_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			_la = _input.LA(1);
			if ( !(_la==T__6 || _la==T__7) ) {
			_errHandler.recoverInline(this);
			} else {
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Any_typeContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public Any_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_any_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterAny_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitAny_type(this);
		}
	}

	public final Any_typeContext any_type() throws RecognitionException {
		Any_typeContext _localctx = new Any_typeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_any_type);
		try {
			setState(128);
			switch (_input.LA(1)) {
			case T__6:
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				var_type();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				match(T__8);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Id_listContext extends ParserRuleContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Id_tailContext id_tail() {
			return getRuleContext(Id_tailContext.class,0);
		}
		public Id_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterId_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitId_list(this);
		}
	}

	public final Id_listContext id_list() throws RecognitionException {
		Id_listContext _localctx = new Id_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_id_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			id();
			setState(131);
			id_tail();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Id_tailContext extends ParserRuleContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Id_tailContext id_tail() {
			return getRuleContext(Id_tailContext.class,0);
		}
		public Id_tailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_tail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterId_tail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitId_tail(this);
		}
	}

	public final Id_tailContext id_tail() throws RecognitionException {
		Id_tailContext _localctx = new Id_tailContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_id_tail);
		try {
			setState(138);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				match(T__9);
				setState(134);
				id();
				setState(135);
				id_tail();
				}
				break;
			case T__5:
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_decl_listContext extends ParserRuleContext {
		public Param_declContext param_decl() {
			return getRuleContext(Param_declContext.class,0);
		}
		public Param_decl_tailContext param_decl_tail() {
			return getRuleContext(Param_decl_tailContext.class,0);
		}
		public Param_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_decl_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterParam_decl_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitParam_decl_list(this);
		}
	}

	public final Param_decl_listContext param_decl_list() throws RecognitionException {
		Param_decl_listContext _localctx = new Param_decl_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_param_decl_list);
		try {
			setState(144);
			switch (_input.LA(1)) {
			case T__6:
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				param_decl();
				setState(141);
				param_decl_tail();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_declContext extends ParserRuleContext {
		public Var_typeContext var_type;
		public IdContext id;
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Param_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterParam_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitParam_decl(this);
		}
	}

	public final Param_declContext param_decl() throws RecognitionException {
		Param_declContext _localctx = new Param_declContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_param_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			((Param_declContext)_localctx).var_type = var_type();
			setState(147);
			((Param_declContext)_localctx).id = id();
			createSymbolTable.insertVariable((((Param_declContext)_localctx).var_type!=null?_input.getText(((Param_declContext)_localctx).var_type.start,((Param_declContext)_localctx).var_type.stop):null), (((Param_declContext)_localctx).id!=null?_input.getText(((Param_declContext)_localctx).id.start,((Param_declContext)_localctx).id.stop):null), null);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_decl_tailContext extends ParserRuleContext {
		public Param_declContext param_decl() {
			return getRuleContext(Param_declContext.class,0);
		}
		public Param_decl_tailContext param_decl_tail() {
			return getRuleContext(Param_decl_tailContext.class,0);
		}
		public Param_decl_tailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_decl_tail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterParam_decl_tail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitParam_decl_tail(this);
		}
	}

	public final Param_decl_tailContext param_decl_tail() throws RecognitionException {
		Param_decl_tailContext _localctx = new Param_decl_tailContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_param_decl_tail);
		try {
			setState(155);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(T__9);
				setState(151);
				param_decl();
				setState(152);
				param_decl_tail();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_declarationsContext extends ParserRuleContext {
		public Func_declContext func_decl() {
			return getRuleContext(Func_declContext.class,0);
		}
		public Func_declarationsContext func_declarations() {
			return getRuleContext(Func_declarationsContext.class,0);
		}
		public Func_declarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_declarations; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFunc_declarations(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFunc_declarations(this);
		}
	}

	public final Func_declarationsContext func_declarations() throws RecognitionException {
		Func_declarationsContext _localctx = new Func_declarationsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_func_declarations);
		try {
			setState(161);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(157);
				func_decl();
				setState(158);
				func_declarations();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_declContext extends ParserRuleContext {
		public IdContext id;
		public Any_typeContext any_type() {
			return getRuleContext(Any_typeContext.class,0);
		}
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Param_decl_listContext param_decl_list() {
			return getRuleContext(Param_decl_listContext.class,0);
		}
		public Func_bodyContext func_body() {
			return getRuleContext(Func_bodyContext.class,0);
		}
		public Func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFunc_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFunc_decl(this);
		}
	}

	public final Func_declContext func_decl() throws RecognitionException {
		Func_declContext _localctx = new Func_declContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_func_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(T__10);
			setState(164);
			any_type();
			setState(165);
			((Func_declContext)_localctx).id = id();
			createSymbolTable.FunctionScopeTable((((Func_declContext)_localctx).id!=null?_input.getText(((Func_declContext)_localctx).id.start,((Func_declContext)_localctx).id.stop):null));
			setState(167);
			match(T__11);
			setState(168);
			param_decl_list();
			setState(169);
			match(T__12);
			setState(170);
			match(T__1);
			setState(171);
			func_body();
			setState(172);
			match(T__2);
			createSymbolTable.popSymbolTable();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_bodyContext extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Func_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFunc_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFunc_body(this);
		}
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_func_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			decl();
			setState(176);
			stmt_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Stmt_listContext extends ParserRuleContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Stmt_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterStmt_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitStmt_list(this);
		}
	}

	public final Stmt_listContext stmt_list() throws RecognitionException {
		Stmt_listContext _localctx = new Stmt_listContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_stmt_list);
		try {
			setState(182);
			switch (_input.LA(1)) {
			case T__13:
			case T__14:
			case T__15:
			case T__20:
			case T__29:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				stmt();
				setState(179);
				stmt_list();
				}
				break;
			case T__2:
			case T__21:
			case T__22:
			case T__30:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public Base_stmtContext base_stmt() {
			return getRuleContext(Base_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_stmt);
		try {
			setState(187);
			switch (_input.LA(1)) {
			case T__13:
			case T__14:
			case T__15:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				base_stmt();
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 2);
				{
				setState(185);
				if_stmt();
				}
				break;
			case T__29:
				enterOuterAlt(_localctx, 3);
				{
				setState(186);
				for_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Base_stmtContext extends ParserRuleContext {
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public Read_stmtContext read_stmt() {
			return getRuleContext(Read_stmtContext.class,0);
		}
		public Write_stmtContext write_stmt() {
			return getRuleContext(Write_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Base_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterBase_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitBase_stmt(this);
		}
	}

	public final Base_stmtContext base_stmt() throws RecognitionException {
		Base_stmtContext _localctx = new Base_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_base_stmt);
		try {
			setState(193);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				assign_stmt();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
				read_stmt();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 3);
				{
				setState(191);
				write_stmt();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 4);
				{
				setState(192);
				return_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public Assign_exprContext assign_expr() {
			return getRuleContext(Assign_exprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterAssign_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitAssign_stmt(this);
		}
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			assign_expr();
			setState(196);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_exprContext extends ParserRuleContext {
		public IdContext id;
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterAssign_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitAssign_expr(this);
		}
	}

	public final Assign_exprContext assign_expr() throws RecognitionException {
		Assign_exprContext _localctx = new Assign_exprContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assign_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			((Assign_exprContext)_localctx).id = id();
			setState(199);
			match(T__4);
			AST.setAST(":=", (((Assign_exprContext)_localctx).id!=null?_input.getText(((Assign_exprContext)_localctx).id.start,((Assign_exprContext)_localctx).id.stop):null)); /*System.out.println("NEW ASSIGNMENT!!!! for "+(((Assign_exprContext)_localctx).id!=null?_input.getText(((Assign_exprContext)_localctx).id.start,((Assign_exprContext)_localctx).id.stop):null));*/
			setState(201);
			expr();
			/*System.out.println("assign_expr --> popFinal");*/ AST.popFinalNode(); /*System.out.println("The inorder traversal of the overall tree: ");*/ AST.print(); 
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_stmtContext extends ParserRuleContext {
		public Id_listContext id_list;
		public Id_listContext id_list() {
			return getRuleContext(Id_listContext.class,0);
		}
		public Read_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterRead_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitRead_stmt(this);
		}
	}

	public final Read_stmtContext read_stmt() throws RecognitionException {
		Read_stmtContext _localctx = new Read_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_read_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(T__13);
			setState(205);
			match(T__11);
			setState(206);
			((Read_stmtContext)_localctx).id_list = id_list();
			setState(207);
			match(T__12);
			AST.ReadFunc((((Read_stmtContext)_localctx).id_list!=null?_input.getText(((Read_stmtContext)_localctx).id_list.start,((Read_stmtContext)_localctx).id_list.stop):null));
			setState(209);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Write_stmtContext extends ParserRuleContext {
		public Id_listContext id_list;
		public Id_listContext id_list() {
			return getRuleContext(Id_listContext.class,0);
		}
		public Write_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterWrite_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitWrite_stmt(this);
		}
	}

	public final Write_stmtContext write_stmt() throws RecognitionException {
		Write_stmtContext _localctx = new Write_stmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_write_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			/*System.out.println("In Write statment");*/
			setState(212);
			match(T__14);
			setState(213);
			match(T__11);
			setState(214);
			((Write_stmtContext)_localctx).id_list = id_list();
			setState(215);
			match(T__12);
			AST.WriteFunc((((Write_stmtContext)_localctx).id_list!=null?_input.getText(((Write_stmtContext)_localctx).id_list.start,((Write_stmtContext)_localctx).id_list.stop):null));
			setState(217);
			match(T__5);
			/*System.out.println("Finished WRite statement");*/
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterReturn_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitReturn_stmt(this);
		}
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(T__15);
			setState(221);
			expr();
			setState(222);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public Expr_prefixContext expr_prefix() {
			return getRuleContext(Expr_prefixContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			/*System.out.println("NEW EXPR");*/
			setState(225);
			expr_prefix(0);
			/*System.out.println("EXPR -> factor");*/
			setState(227);
			factor();
			/*System.out.println("end of expression");*/
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_prefixContext extends ParserRuleContext {
		public AddopContext addop;
		public Expr_prefixContext expr_prefix() {
			return getRuleContext(Expr_prefixContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public AddopContext addop() {
			return getRuleContext(AddopContext.class,0);
		}
		public Expr_prefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_prefix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterExpr_prefix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitExpr_prefix(this);
		}
	}

	public final Expr_prefixContext expr_prefix() throws RecognitionException {
		return expr_prefix(0);
	}

	private Expr_prefixContext expr_prefix(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr_prefixContext _localctx = new Expr_prefixContext(_ctx, _parentState);
		Expr_prefixContext _prevctx = _localctx;
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_expr_prefix, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			}
			_ctx.stop = _input.LT(-1);
			setState(240);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr_prefixContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr_prefix);
					setState(231);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					/*System.out.println("ExprPrefix -> factor");*/
					setState(233);
					factor();
					/*System.out.println("expr_prefix, FACTOR COMPLETE");*/
					setState(235);
					((Expr_prefixContext)_localctx).addop = addop();
					/*System.out.println("Expr_prefix complete");*/ /*System.out.println("Element hit: " + (((Expr_prefixContext)_localctx).addop!=null?_input.getText(((Expr_prefixContext)_localctx).addop.start,((Expr_prefixContext)_localctx).addop.stop):null));*/ AST.createNonTerminalNode((((Expr_prefixContext)_localctx).addop!=null?_input.getText(((Expr_prefixContext)_localctx).addop.start,((Expr_prefixContext)_localctx).addop.stop):null)); 
					}
					} 
				}
				setState(242);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public Factor_prefixContext factor_prefix() {
			return getRuleContext(Factor_prefixContext.class,0);
		}
		public Postfix_exprContext postfix_expr() {
			return getRuleContext(Postfix_exprContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_factor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			/*System.out.println("NEW FACTOR");*/
			setState(244);
			factor_prefix(0);
			/*System.out.println("Factor -> postfix_expr");*/
			setState(246);
			postfix_expr();
			/*System.out.println("factor complete");*/ /*System.out.println("Factor recognized. Calling checkstack func.");*/ AST.factorRecognized = 1; AST.checkStack(); /*System.out.println("factor recognized");*/
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Factor_prefixContext extends ParserRuleContext {
		public MulopContext mulop;
		public Factor_prefixContext factor_prefix() {
			return getRuleContext(Factor_prefixContext.class,0);
		}
		public Postfix_exprContext postfix_expr() {
			return getRuleContext(Postfix_exprContext.class,0);
		}
		public MulopContext mulop() {
			return getRuleContext(MulopContext.class,0);
		}
		public Factor_prefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_prefix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFactor_prefix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFactor_prefix(this);
		}
	}

	public final Factor_prefixContext factor_prefix() throws RecognitionException {
		return factor_prefix(0);
	}

	private Factor_prefixContext factor_prefix(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Factor_prefixContext _localctx = new Factor_prefixContext(_ctx, _parentState);
		Factor_prefixContext _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_factor_prefix, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			}
			_ctx.stop = _input.LT(-1);
			setState(259);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Factor_prefixContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_factor_prefix);
					setState(250);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					/*System.out.println("NEW FACTORPREFIX");*/
					setState(252);
					postfix_expr();
					/*System.out.println("PostFixExpr Complete");*/
					setState(254);
					((Factor_prefixContext)_localctx).mulop = mulop();
					/*System.out.println("factor_prefix complete");*/ /*System.out.println("Element hit: " + (((Factor_prefixContext)_localctx).mulop!=null?_input.getText(((Factor_prefixContext)_localctx).mulop.start,((Factor_prefixContext)_localctx).mulop.stop):null));*/ AST.createNonTerminalNode((((Factor_prefixContext)_localctx).mulop!=null?_input.getText(((Factor_prefixContext)_localctx).mulop.start,((Factor_prefixContext)_localctx).mulop.stop):null)); 
					}
					} 
				}
				setState(261);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Postfix_exprContext extends ParserRuleContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public Call_exprContext call_expr() {
			return getRuleContext(Call_exprContext.class,0);
		}
		public Postfix_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfix_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterPostfix_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitPostfix_expr(this);
		}
	}

	public final Postfix_exprContext postfix_expr() throws RecognitionException {
		Postfix_exprContext _localctx = new Postfix_exprContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_postfix_expr);
		try {
			setState(265);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				/*System.out.println("NEW POSTFIXEXPR");*/
				setState(263);
				primary();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
				call_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_exprContext extends ParserRuleContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Call_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterCall_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitCall_expr(this);
		}
	}

	public final Call_exprContext call_expr() throws RecognitionException {
		Call_exprContext _localctx = new Call_exprContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_call_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			id();
			setState(268);
			match(T__11);
			setState(269);
			expr_list();
			setState(270);
			match(T__12);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_listContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_list_tailContext expr_list_tail() {
			return getRuleContext(Expr_list_tailContext.class,0);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterExpr_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitExpr_list(this);
		}
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_expr_list);
		try {
			setState(276);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				expr();
				setState(273);
				expr_list_tail();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_list_tailContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_list_tailContext expr_list_tail() {
			return getRuleContext(Expr_list_tailContext.class,0);
		}
		public Expr_list_tailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list_tail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterExpr_list_tail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitExpr_list_tail(this);
		}
	}

	public final Expr_list_tailContext expr_list_tail() throws RecognitionException {
		Expr_list_tailContext _localctx = new Expr_list_tailContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_expr_list_tail);
		try {
			setState(283);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(278);
				match(T__9);
				setState(279);
				expr();
				setState(280);
				expr_list_tail();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryContext extends ParserRuleContext {
		public IdContext id;
		public Token INTLITERAL;
		public Token FLOATLITERAL;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public TerminalNode INTLITERAL() { return getToken(MicroParser.INTLITERAL, 0); }
		public TerminalNode FLOATLITERAL() { return getToken(MicroParser.FLOATLITERAL, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterPrimary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitPrimary(this);
		}
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_primary);
		try {
			setState(298);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				AST.dontMove(1); /*AST.insideExprCount = 0;*/ AST.exprStackCount = AST.stackCount; /*System.out.println("\nExpression stack count at entry: " + AST.exprStackCount);*/
				setState(286);
				match(T__11);
				setState(287);
				expr();
				setState(288);
				match(T__12);
				/*System.out.println("Found nested expression");*/ AST.dontMove(0); /*AST.moveRightChildUp();*/
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(291);
				((PrimaryContext)_localctx).id = id();
				/*System.out.println("Element hit: " + $id.text);*//*System.out.println($id.text);*/ AST.createTerminalNode((((PrimaryContext)_localctx).id!=null?_input.getText(((PrimaryContext)_localctx).id.start,((PrimaryContext)_localctx).id.stop):null)); 
				}
				break;
			case INTLITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(294);
				((PrimaryContext)_localctx).INTLITERAL = match(INTLITERAL);
				/*System.out.println("Element hit: " + $INTLITERAL.text);*/ /*System.out.println((((PrimaryContext)_localctx).INTLITERAL!=null?((PrimaryContext)_localctx).INTLITERAL.getText():null));*/ AST.createTerminalNode((((PrimaryContext)_localctx).INTLITERAL!=null?((PrimaryContext)_localctx).INTLITERAL.getText():null)); 
				}
				break;
			case FLOATLITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(296);
				((PrimaryContext)_localctx).FLOATLITERAL = match(FLOATLITERAL);
				/*System.out.println("Element hit: " + $FLOATLITERAL.text);*//*System.out.println($FLOATLITERAL.text);*/ AST.createTerminalNode((((PrimaryContext)_localctx).FLOATLITERAL!=null?((PrimaryContext)_localctx).FLOATLITERAL.getText():null)); 
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AddopContext extends ParserRuleContext {
		public AddopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterAddop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitAddop(this);
		}
	}

	public final AddopContext addop() throws RecognitionException {
		AddopContext _localctx = new AddopContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_addop);
		try {
			setState(304);
			switch (_input.LA(1)) {
			case T__16:
				enterOuterAlt(_localctx, 1);
				{
				/*System.out.println("+");*/
				setState(301);
				match(T__16);
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 2);
				{
				/*System.out.println("-");*/
				setState(303);
				match(T__17);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MulopContext extends ParserRuleContext {
		public MulopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterMulop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitMulop(this);
		}
	}

	public final MulopContext mulop() throws RecognitionException {
		MulopContext _localctx = new MulopContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_mulop);
		try {
			setState(310);
			switch (_input.LA(1)) {
			case T__18:
				enterOuterAlt(_localctx, 1);
				{
				/*System.out.println("*");*/
				setState(307);
				match(T__18);
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 2);
				{
				/*System.out.println("/");*/
				setState(309);
				match(T__19);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Else_partContext else_part() {
			return getRuleContext(Else_partContext.class,0);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterIf_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitIf_stmt(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_if_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			/*System.out.println("IN IF STATEMENT");*/ createSymbolTable.BlockScopeTable(); AST.pushIfLabels();
			setState(313);
			match(T__20);
			setState(314);
			match(T__11);
			setState(315);
			cond();
			setState(316);
			match(T__12);
			/*System.out.print("Finished condition");*/
			setState(318);
			decl();
			/*System.out.println("IF --> StmtList");*/
			setState(320);
			stmt_list();
			createSymbolTable.popSymbolTable(); AST.jump_label(1); 
			setState(322);
			else_part();
			setState(323);
			match(T__21);
			AST.jump_label(4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_partContext extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Else_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_part; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterElse_part(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitElse_part(this);
		}
	}

	public final Else_partContext else_part() throws RecognitionException {
		Else_partContext _localctx = new Else_partContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_else_part);
		try {
			setState(334);
			switch (_input.LA(1)) {
			case T__22:
				enterOuterAlt(_localctx, 1);
				{
				createSymbolTable.BlockScopeTable(); AST.jump_label(2);
				setState(327);
				match(T__22);
				setState(328);
				decl();
				setState(329);
				stmt_list();
				AST.jump_label(3);
				createSymbolTable.popSymbolTable();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				AST.jump_label(2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondContext extends ParserRuleContext {
		public CompopContext compop;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CompopContext compop() {
			return getRuleContext(CompopContext.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			/*System.out.println("IN COND");*/
			setState(337);
			expr();
			/*System.out.println("COND --> COMPOP");*/
			setState(339);
			((CondContext)_localctx).compop = compop();
			AST.createNonTerminalNode((((CondContext)_localctx).compop!=null?_input.getText(((CondContext)_localctx).compop.start,((CondContext)_localctx).compop.stop):null));
			setState(341);
			expr();
			AST.popFinalNodeCondition();
			/*System.out.println("End of condition");*/
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompopContext extends ParserRuleContext {
		public CompopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterCompop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitCompop(this);
		}
	}

	public final CompopContext compop() throws RecognitionException {
		CompopContext _localctx = new CompopContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_compop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__28))) != 0)) ) {
			_errHandler.recoverInline(this);
			} else {
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Init_stmtContext extends ParserRuleContext {
		public Assign_exprContext assign_expr() {
			return getRuleContext(Assign_exprContext.class,0);
		}
		public Init_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterInit_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitInit_stmt(this);
		}
	}

	public final Init_stmtContext init_stmt() throws RecognitionException {
		Init_stmtContext _localctx = new Init_stmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_init_stmt);
		try {
			setState(349);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				assign_expr();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Incr_stmtContext extends ParserRuleContext {
		public Assign_exprContext assign_expr() {
			return getRuleContext(Assign_exprContext.class,0);
		}
		public Incr_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incr_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterIncr_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitIncr_stmt(this);
		}
	}

	public final Incr_stmtContext incr_stmt() throws RecognitionException {
		Incr_stmtContext _localctx = new Incr_stmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_incr_stmt);
		try {
			setState(356);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				AST.incrStmt = 1; /*System.out.println("in INCR_STATEMENT");*/
				setState(352);
				assign_expr();
				/*System.out.println("Out of Increment statment");*/ AST.incrStmt = 0;
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				/*System.out.println("IN EMPTY INCR_STMT.");*/
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_stmtContext extends ParserRuleContext {
		public Init_stmtContext init_stmt() {
			return getRuleContext(Init_stmtContext.class,0);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public Incr_stmtContext incr_stmt() {
			return getRuleContext(Incr_stmtContext.class,0);
		}
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterFor_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitFor_stmt(this);
		}
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			createSymbolTable.BlockScopeTable();
			setState(359);
			match(T__29);
			setState(360);
			match(T__11);
			setState(361);
			init_stmt();
			setState(362);
			match(T__5);
			/*System.out.println("Out of init_statment");*/ AST.pushForLabels(); AST.for_label(1); AST.inFor = 1;
			setState(364);
			cond();
			 AST.inFor = 0;
			setState(366);
			match(T__5);
			setState(367);
			incr_stmt();
			setState(368);
			match(T__12);
			setState(369);
			decl();
			setState(370);
			stmt_list();
			 /*System.out.println("AST.incrIRnode");*/ AST.for_label(2); /*System.out.println("INCRIRNODE");*/ AST.incrIRnode(); AST.for_label(3); createSymbolTable.popSymbolTable();
			setState(372);
			match(T__30);
			AST.for_label(4); 
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhitespaceContext extends ParserRuleContext {
		public TerminalNode WHITESPACE() { return getToken(MicroParser.WHITESPACE, 0); }
		public WhitespaceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whitespace; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).enterWhitespace(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MicroListener ) ((MicroListener)listener).exitWhitespace(this);
		}
	}

	public final WhitespaceContext whitespace() throws RecognitionException {
		WhitespaceContext _localctx = new WhitespaceContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_whitespace);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			match(WHITESPACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 26:
			return expr_prefix_sempred((Expr_prefixContext)_localctx, predIndex);
		case 28:
			return factor_prefix_sempred((Factor_prefixContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_prefix_sempred(Expr_prefixContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean factor_prefix_sempred(Factor_prefixContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3)\u017c\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u0083\n\n\3\13\3\13\3\13\3\f\3\f"+
		"\3\f\3\f\3\f\5\f\u008d\n\f\3\r\3\r\3\r\3\r\5\r\u0093\n\r\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u009e\n\17\3\20\3\20\3\20\3\20\5\20"+
		"\u00a4\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00b9\n\23\3\24\3\24\3\24\5\24"+
		"\u00be\n\24\3\25\3\25\3\25\3\25\5\25\u00c4\n\25\3\26\3\26\3\26\3\27\3"+
		"\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3"+
		"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3"+
		"\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u00f1\n\34"+
		"\f\34\16\34\u00f4\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3"+
		"\36\3\36\3\36\3\36\3\36\7\36\u0104\n\36\f\36\16\36\u0107\13\36\3\37\3"+
		"\37\3\37\5\37\u010c\n\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\5!\u0117\n!\3\"\3"+
		"\"\3\"\3\"\3\"\5\"\u011e\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5"+
		"#\u012d\n#\3$\3$\3$\3$\5$\u0133\n$\3%\3%\3%\3%\5%\u0139\n%\3&\3&\3&\3"+
		"&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0151"+
		"\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3*\3*\5*\u0160\n*\3+\3+\3+\3+\3"+
		"+\5+\u0167\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3"+
		"-\3-\2\4\66:.\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64"+
		"\668:<>@BDFHJLNPRTVX\2\4\3\2\t\n\3\2\32\37\u0169\2Z\3\2\2\2\4a\3\2\2\2"+
		"\6c\3\2\2\2\bn\3\2\2\2\np\3\2\2\2\fw\3\2\2\2\16y\3\2\2\2\20~\3\2\2\2\22"+
		"\u0082\3\2\2\2\24\u0084\3\2\2\2\26\u008c\3\2\2\2\30\u0092\3\2\2\2\32\u0094"+
		"\3\2\2\2\34\u009d\3\2\2\2\36\u00a3\3\2\2\2 \u00a5\3\2\2\2\"\u00b1\3\2"+
		"\2\2$\u00b8\3\2\2\2&\u00bd\3\2\2\2(\u00c3\3\2\2\2*\u00c5\3\2\2\2,\u00c8"+
		"\3\2\2\2.\u00ce\3\2\2\2\60\u00d5\3\2\2\2\62\u00de\3\2\2\2\64\u00e2\3\2"+
		"\2\2\66\u00e8\3\2\2\28\u00f5\3\2\2\2:\u00fb\3\2\2\2<\u010b\3\2\2\2>\u010d"+
		"\3\2\2\2@\u0116\3\2\2\2B\u011d\3\2\2\2D\u012c\3\2\2\2F\u0132\3\2\2\2H"+
		"\u0138\3\2\2\2J\u013a\3\2\2\2L\u0150\3\2\2\2N\u0152\3\2\2\2P\u015b\3\2"+
		"\2\2R\u015f\3\2\2\2T\u0166\3\2\2\2V\u0168\3\2\2\2X\u0179\3\2\2\2Z[\7\3"+
		"\2\2[\\\5\4\3\2\\]\7\4\2\2]^\5\6\4\2^_\7\5\2\2_`\b\2\1\2`\3\3\2\2\2ab"+
		"\7$\2\2b\5\3\2\2\2cd\b\4\1\2de\5\b\5\2ef\5\36\20\2f\7\3\2\2\2gh\5\n\6"+
		"\2hi\5\b\5\2io\3\2\2\2jk\5\16\b\2kl\5\b\5\2lo\3\2\2\2mo\3\2\2\2ng\3\2"+
		"\2\2nj\3\2\2\2nm\3\2\2\2o\t\3\2\2\2pq\7\6\2\2qr\5\4\3\2rs\7\7\2\2st\5"+
		"\f\7\2tu\7\b\2\2uv\b\6\1\2v\13\3\2\2\2wx\7\'\2\2x\r\3\2\2\2yz\5\20\t\2"+
		"z{\5\24\13\2{|\7\b\2\2|}\b\b\1\2}\17\3\2\2\2~\177\t\2\2\2\177\21\3\2\2"+
		"\2\u0080\u0083\5\20\t\2\u0081\u0083\7\13\2\2\u0082\u0080\3\2\2\2\u0082"+
		"\u0081\3\2\2\2\u0083\23\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\5\26\f"+
		"\2\u0086\25\3\2\2\2\u0087\u0088\7\f\2\2\u0088\u0089\5\4\3\2\u0089\u008a"+
		"\5\26\f\2\u008a\u008d\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u0087\3\2\2\2"+
		"\u008c\u008b\3\2\2\2\u008d\27\3\2\2\2\u008e\u008f\5\32\16\2\u008f\u0090"+
		"\5\34\17\2\u0090\u0093\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u008e\3\2\2\2"+
		"\u0092\u0091\3\2\2\2\u0093\31\3\2\2\2\u0094\u0095\5\20\t\2\u0095\u0096"+
		"\5\4\3\2\u0096\u0097\b\16\1\2\u0097\33\3\2\2\2\u0098\u0099\7\f\2\2\u0099"+
		"\u009a\5\32\16\2\u009a\u009b\5\34\17\2\u009b\u009e\3\2\2\2\u009c\u009e"+
		"\3\2\2\2\u009d\u0098\3\2\2\2\u009d\u009c\3\2\2\2\u009e\35\3\2\2\2\u009f"+
		"\u00a0\5 \21\2\u00a0\u00a1\5\36\20\2\u00a1\u00a4\3\2\2\2\u00a2\u00a4\3"+
		"\2\2\2\u00a3\u009f\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\37\3\2\2\2\u00a5"+
		"\u00a6\7\r\2\2\u00a6\u00a7\5\22\n\2\u00a7\u00a8\5\4\3\2\u00a8\u00a9\b"+
		"\21\1\2\u00a9\u00aa\7\16\2\2\u00aa\u00ab\5\30\r\2\u00ab\u00ac\7\17\2\2"+
		"\u00ac\u00ad\7\4\2\2\u00ad\u00ae\5\"\22\2\u00ae\u00af\7\5\2\2\u00af\u00b0"+
		"\b\21\1\2\u00b0!\3\2\2\2\u00b1\u00b2\5\b\5\2\u00b2\u00b3\5$\23\2\u00b3"+
		"#\3\2\2\2\u00b4\u00b5\5&\24\2\u00b5\u00b6\5$\23\2\u00b6\u00b9\3\2\2\2"+
		"\u00b7\u00b9\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9%\3"+
		"\2\2\2\u00ba\u00be\5(\25\2\u00bb\u00be\5J&\2\u00bc\u00be\5V,\2\u00bd\u00ba"+
		"\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\'\3\2\2\2\u00bf"+
		"\u00c4\5*\26\2\u00c0\u00c4\5.\30\2\u00c1\u00c4\5\60\31\2\u00c2\u00c4\5"+
		"\62\32\2\u00c3\u00bf\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3"+
		"\u00c2\3\2\2\2\u00c4)\3\2\2\2\u00c5\u00c6\5,\27\2\u00c6\u00c7\7\b\2\2"+
		"\u00c7+\3\2\2\2\u00c8\u00c9\5\4\3\2\u00c9\u00ca\7\7\2\2\u00ca\u00cb\b"+
		"\27\1\2\u00cb\u00cc\5\64\33\2\u00cc\u00cd\b\27\1\2\u00cd-\3\2\2\2\u00ce"+
		"\u00cf\7\20\2\2\u00cf\u00d0\7\16\2\2\u00d0\u00d1\5\24\13\2\u00d1\u00d2"+
		"\7\17\2\2\u00d2\u00d3\b\30\1\2\u00d3\u00d4\7\b\2\2\u00d4/\3\2\2\2\u00d5"+
		"\u00d6\b\31\1\2\u00d6\u00d7\7\21\2\2\u00d7\u00d8\7\16\2\2\u00d8\u00d9"+
		"\5\24\13\2\u00d9\u00da\7\17\2\2\u00da\u00db\b\31\1\2\u00db\u00dc\7\b\2"+
		"\2\u00dc\u00dd\b\31\1\2\u00dd\61\3\2\2\2\u00de\u00df\7\22\2\2\u00df\u00e0"+
		"\5\64\33\2\u00e0\u00e1\7\b\2\2\u00e1\63\3\2\2\2\u00e2\u00e3\b\33\1\2\u00e3"+
		"\u00e4\5\66\34\2\u00e4\u00e5\b\33\1\2\u00e5\u00e6\58\35\2\u00e6\u00e7"+
		"\b\33\1\2\u00e7\65\3\2\2\2\u00e8\u00f2\b\34\1\2\u00e9\u00ea\f\4\2\2\u00ea"+
		"\u00eb\b\34\1\2\u00eb\u00ec\58\35\2\u00ec\u00ed\b\34\1\2\u00ed\u00ee\5"+
		"F$\2\u00ee\u00ef\b\34\1\2\u00ef\u00f1\3\2\2\2\u00f0\u00e9\3\2\2\2\u00f1"+
		"\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\67\3\2\2"+
		"\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\b\35\1\2\u00f6\u00f7\5:\36\2\u00f7"+
		"\u00f8\b\35\1\2\u00f8\u00f9\5<\37\2\u00f9\u00fa\b\35\1\2\u00fa9\3\2\2"+
		"\2\u00fb\u0105\b\36\1\2\u00fc\u00fd\f\4\2\2\u00fd\u00fe\b\36\1\2\u00fe"+
		"\u00ff\5<\37\2\u00ff\u0100\b\36\1\2\u0100\u0101\5H%\2\u0101\u0102\b\36"+
		"\1\2\u0102\u0104\3\2\2\2\u0103\u00fc\3\2\2\2\u0104\u0107\3\2\2\2\u0105"+
		"\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106;\3\2\2\2\u0107\u0105\3\2\2\2"+
		"\u0108\u0109\b\37\1\2\u0109\u010c\5D#\2\u010a\u010c\5> \2\u010b\u0108"+
		"\3\2\2\2\u010b\u010a\3\2\2\2\u010c=\3\2\2\2\u010d\u010e\5\4\3\2\u010e"+
		"\u010f\7\16\2\2\u010f\u0110\5@!\2\u0110\u0111\7\17\2\2\u0111?\3\2\2\2"+
		"\u0112\u0113\5\64\33\2\u0113\u0114\5B\"\2\u0114\u0117\3\2\2\2\u0115\u0117"+
		"\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0115\3\2\2\2\u0117A\3\2\2\2\u0118"+
		"\u0119\7\f\2\2\u0119\u011a\5\64\33\2\u011a\u011b\5B\"\2\u011b\u011e\3"+
		"\2\2\2\u011c\u011e\3\2\2\2\u011d\u0118\3\2\2\2\u011d\u011c\3\2\2\2\u011e"+
		"C\3\2\2\2\u011f\u0120\b#\1\2\u0120\u0121\7\16\2\2\u0121\u0122\5\64\33"+
		"\2\u0122\u0123\7\17\2\2\u0123\u0124\b#\1\2\u0124\u012d\3\2\2\2\u0125\u0126"+
		"\5\4\3\2\u0126\u0127\b#\1\2\u0127\u012d\3\2\2\2\u0128\u0129\7%\2\2\u0129"+
		"\u012d\b#\1\2\u012a\u012b\7&\2\2\u012b\u012d\b#\1\2\u012c\u011f\3\2\2"+
		"\2\u012c\u0125\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u012a\3\2\2\2\u012dE"+
		"\3\2\2\2\u012e\u012f\b$\1\2\u012f\u0133\7\23\2\2\u0130\u0131\b$\1\2\u0131"+
		"\u0133\7\24\2\2\u0132\u012e\3\2\2\2\u0132\u0130\3\2\2\2\u0133G\3\2\2\2"+
		"\u0134\u0135\b%\1\2\u0135\u0139\7\25\2\2\u0136\u0137\b%\1\2\u0137\u0139"+
		"\7\26\2\2\u0138\u0134\3\2\2\2\u0138\u0136\3\2\2\2\u0139I\3\2\2\2\u013a"+
		"\u013b\b&\1\2\u013b\u013c\7\27\2\2\u013c\u013d\7\16\2\2\u013d\u013e\5"+
		"N(\2\u013e\u013f\7\17\2\2\u013f\u0140\b&\1\2\u0140\u0141\5\b\5\2\u0141"+
		"\u0142\b&\1\2\u0142\u0143\5$\23\2\u0143\u0144\b&\1\2\u0144\u0145\5L\'"+
		"\2\u0145\u0146\7\30\2\2\u0146\u0147\b&\1\2\u0147K\3\2\2\2\u0148\u0149"+
		"\b\'\1\2\u0149\u014a\7\31\2\2\u014a\u014b\5\b\5\2\u014b\u014c\5$\23\2"+
		"\u014c\u014d\b\'\1\2\u014d\u014e\b\'\1\2\u014e\u0151\3\2\2\2\u014f\u0151"+
		"\b\'\1\2\u0150\u0148\3\2\2\2\u0150\u014f\3\2\2\2\u0151M\3\2\2\2\u0152"+
		"\u0153\b(\1\2\u0153\u0154\5\64\33\2\u0154\u0155\b(\1\2\u0155\u0156\5P"+
		")\2\u0156\u0157\b(\1\2\u0157\u0158\5\64\33\2\u0158\u0159\b(\1\2\u0159"+
		"\u015a\b(\1\2\u015aO\3\2\2\2\u015b\u015c\t\3\2\2\u015cQ\3\2\2\2\u015d"+
		"\u0160\5,\27\2\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2"+
		"\2\2\u0160S\3\2\2\2\u0161\u0162\b+\1\2\u0162\u0163\5,\27\2\u0163\u0164"+
		"\b+\1\2\u0164\u0167\3\2\2\2\u0165\u0167\b+\1\2\u0166\u0161\3\2\2\2\u0166"+
		"\u0165\3\2\2\2\u0167U\3\2\2\2\u0168\u0169\b,\1\2\u0169\u016a\7 \2\2\u016a"+
		"\u016b\7\16\2\2\u016b\u016c\5R*\2\u016c\u016d\7\b\2\2\u016d\u016e\b,\1"+
		"\2\u016e\u016f\5N(\2\u016f\u0170\b,\1\2\u0170\u0171\7\b\2\2\u0171\u0172"+
		"\5T+\2\u0172\u0173\7\17\2\2\u0173\u0174\5\b\5\2\u0174\u0175\5$\23\2\u0175"+
		"\u0176\b,\1\2\u0176\u0177\7!\2\2\u0177\u0178\b,\1\2\u0178W\3\2\2\2\u0179"+
		"\u017a\7\"\2\2\u017aY\3\2\2\2\26n\u0082\u008c\u0092\u009d\u00a3\u00b8"+
		"\u00bd\u00c3\u00f2\u0105\u010b\u0116\u011d\u012c\u0132\u0138\u0150\u015f"+
		"\u0166";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}