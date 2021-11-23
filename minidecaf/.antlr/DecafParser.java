// Generated from /home/xw/desktop/minidecaf-2017010335/minidecaf/Decaf.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, Int=27, Return=28, Lparen=29, Rparen=30, Lbrkt=31, 
		Rbrkt=32, Lbrace=33, Rbrace=34, Comma=35, Semicolon=36, Integer=37, Ident=38, 
		Whitespace=39;
	public static final int
		RULE_prog = 0, RULE_progitem = 1, RULE_func = 2, RULE_parameterList = 3, 
		RULE_ty = 4, RULE_block = 5, RULE_blockitem = 6, RULE_stat = 7, RULE_declaration = 8, 
		RULE_expr = 9, RULE_assign = 10, RULE_conditional = 11, RULE_logicOr = 12, 
		RULE_logicAnd = 13, RULE_equal = 14, RULE_relation = 15, RULE_add = 16, 
		RULE_mul = 17, RULE_cast = 18, RULE_unary = 19, RULE_postfix = 20, RULE_argList = 21, 
		RULE_atom = 22, RULE_unaryOp = 23, RULE_addOp = 24, RULE_mulOp = 25, RULE_relationOp = 26, 
		RULE_equalOp = 27, RULE_andOp = 28, RULE_orOp = 29, RULE_assignOP = 30;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "progitem", "func", "parameterList", "ty", "block", "blockitem", 
			"stat", "declaration", "expr", "assign", "conditional", "logicOr", "logicAnd", 
			"equal", "relation", "add", "mul", "cast", "unary", "postfix", "argList", 
			"atom", "unaryOp", "addOp", "mulOp", "relationOp", "equalOp", "andOp", 
			"orOp", "assignOP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", 
			"'continue'", "'='", "'?'", "':'", "'-'", "'!'", "'~'", "'&'", "'+'", 
			"'/'", "'%'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
			"'int'", "'return'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "Int", "Return", "Lparen", "Rparen", "Lbrkt", "Rbrkt", 
			"Lbrace", "Rbrace", "Comma", "Semicolon", "Integer", "Ident", "Whitespace"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DecafParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(DecafParser.EOF, 0); }
		public List<ProgitemContext> progitem() {
			return getRuleContexts(ProgitemContext.class);
		}
		public ProgitemContext progitem(int i) {
			return getRuleContext(ProgitemContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(62);
				progitem();
				}
				}
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Int );
			setState(67);
			match(EOF);
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

	public static class ProgitemContext extends ParserRuleContext {
		public ProgitemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_progitem; }
	 
		public ProgitemContext() { }
		public void copyFrom(ProgitemContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProgDeclarationContext extends ProgitemContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public ProgDeclarationContext(ProgitemContext ctx) { copyFrom(ctx); }
	}
	public static class ProgFuncContext extends ProgitemContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public ProgFuncContext(ProgitemContext ctx) { copyFrom(ctx); }
	}

	public final ProgitemContext progitem() throws RecognitionException {
		ProgitemContext _localctx = new ProgitemContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_progitem);
		try {
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new ProgFuncContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				func();
				}
				break;
			case 2:
				_localctx = new ProgDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				declaration();
				setState(71);
				match(Semicolon);
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

	public static class FuncContext extends ParserRuleContext {
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	 
		public FuncContext() { }
		public void copyFrom(FuncContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FuncDefinitionContext extends FuncContext {
		public TyContext ty() {
			return getRuleContext(TyContext.class,0);
		}
		public TerminalNode Ident() { return getToken(DecafParser.Ident, 0); }
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FuncDefinitionContext(FuncContext ctx) { copyFrom(ctx); }
	}
	public static class FuncDeclarationContext extends FuncContext {
		public TyContext ty() {
			return getRuleContext(TyContext.class,0);
		}
		public TerminalNode Ident() { return getToken(DecafParser.Ident, 0); }
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public FuncDeclarationContext(FuncContext ctx) { copyFrom(ctx); }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_func);
		try {
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new FuncDefinitionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(75);
				ty(0);
				setState(76);
				match(Ident);
				setState(77);
				match(Lparen);
				setState(78);
				parameterList();
				setState(79);
				match(Rparen);
				setState(80);
				block();
				}
				break;
			case 2:
				_localctx = new FuncDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				ty(0);
				setState(83);
				match(Ident);
				setState(84);
				match(Lparen);
				setState(85);
				parameterList();
				setState(86);
				match(Rparen);
				setState(87);
				match(Semicolon);
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

	public static class ParameterListContext extends ParserRuleContext {
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(DecafParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(DecafParser.Comma, i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Int) {
				{
				setState(91);
				declaration();
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(92);
					match(Comma);
					setState(93);
					declaration();
					}
					}
					setState(98);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
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

	public static class TyContext extends ParserRuleContext {
		public TyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ty; }
	 
		public TyContext() { }
		public void copyFrom(TyContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PtrTypeContext extends TyContext {
		public TyContext ty() {
			return getRuleContext(TyContext.class,0);
		}
		public PtrTypeContext(TyContext ctx) { copyFrom(ctx); }
	}
	public static class IntTypeContext extends TyContext {
		public TerminalNode Int() { return getToken(DecafParser.Int, 0); }
		public IntTypeContext(TyContext ctx) { copyFrom(ctx); }
	}

	public final TyContext ty() throws RecognitionException {
		return ty(0);
	}

	private TyContext ty(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TyContext _localctx = new TyContext(_ctx, _parentState);
		TyContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_ty, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new IntTypeContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(102);
			match(Int);
			}
			_ctx.stop = _input.LT(-1);
			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PtrTypeContext(new TyContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_ty);
					setState(104);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(105);
					match(T__0);
					}
					} 
				}
				setState(110);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode Lbrace() { return getToken(DecafParser.Lbrace, 0); }
		public TerminalNode Rbrace() { return getToken(DecafParser.Rbrace, 0); }
		public List<BlockitemContext> blockitem() {
			return getRuleContexts(BlockitemContext.class);
		}
		public BlockitemContext blockitem(int i) {
			return getRuleContext(BlockitemContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(Lbrace);
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Int) | (1L << Return) | (1L << Lparen) | (1L << Lbrace) | (1L << Semicolon) | (1L << Integer) | (1L << Ident))) != 0)) {
				{
				{
				setState(112);
				blockitem();
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(118);
			match(Rbrace);
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

	public static class BlockitemContext extends ParserRuleContext {
		public BlockitemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockitem; }
	 
		public BlockitemContext() { }
		public void copyFrom(BlockitemContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BlockItemStatContext extends BlockitemContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public BlockItemStatContext(BlockitemContext ctx) { copyFrom(ctx); }
	}
	public static class BlockItemDeclContext extends BlockitemContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public BlockItemDeclContext(BlockitemContext ctx) { copyFrom(ctx); }
	}

	public final BlockitemContext blockitem() throws RecognitionException {
		BlockitemContext _localctx = new BlockitemContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_blockitem);
		try {
			setState(124);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case Return:
			case Lparen:
			case Lbrace:
			case Semicolon:
			case Integer:
			case Ident:
				_localctx = new BlockItemStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				stat();
				}
				break;
			case Int:
				_localctx = new BlockItemDeclContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				declaration();
				setState(122);
				match(Semicolon);
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

	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IfStatContext extends StatContext {
		public StatContext thenBranch;
		public StatContext elseBranch;
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public IfStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class DoWhileStatContext extends StatContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public DoWhileStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class BlockStatContext extends StatContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public BlockStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class ExprStatContext extends StatContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public ExprStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class ReturnStatContext extends StatContext {
		public TerminalNode Return() { return getToken(DecafParser.Return, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public ReturnStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class ForDeclStatContext extends StatContext {
		public DeclarationContext pre;
		public ExprContext cond;
		public ExprContext post;
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public List<TerminalNode> Semicolon() { return getTokens(DecafParser.Semicolon); }
		public TerminalNode Semicolon(int i) {
			return getToken(DecafParser.Semicolon, i);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ForDeclStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class ContinueStatContext extends StatContext {
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public ContinueStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class BreakStatContext extends StatContext {
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public BreakStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class EmptyStatContext extends StatContext {
		public TerminalNode Semicolon() { return getToken(DecafParser.Semicolon, 0); }
		public EmptyStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class ForStatContext extends StatContext {
		public ExprContext pre;
		public ExprContext cond;
		public ExprContext post;
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public List<TerminalNode> Semicolon() { return getTokens(DecafParser.Semicolon); }
		public TerminalNode Semicolon(int i) {
			return getToken(DecafParser.Semicolon, i);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ForStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class WhileStatContext extends StatContext {
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public WhileStatContext(StatContext ctx) { copyFrom(ctx); }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_stat);
		int _la;
		try {
			setState(191);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				_localctx = new ReturnStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(Return);
				setState(127);
				expr();
				setState(128);
				match(Semicolon);
				}
				break;
			case 2:
				_localctx = new ExprStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				expr();
				setState(131);
				match(Semicolon);
				}
				break;
			case 3:
				_localctx = new IfStatContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(133);
				match(T__1);
				setState(134);
				match(Lparen);
				setState(135);
				expr();
				setState(136);
				match(Rparen);
				setState(137);
				((IfStatContext)_localctx).thenBranch = stat();
				setState(140);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(138);
					match(T__2);
					setState(139);
					((IfStatContext)_localctx).elseBranch = stat();
					}
					break;
				}
				}
				break;
			case 4:
				_localctx = new BlockStatContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(142);
				block();
				}
				break;
			case 5:
				_localctx = new ForDeclStatContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(143);
				match(T__3);
				setState(144);
				match(Lparen);
				setState(145);
				((ForDeclStatContext)_localctx).pre = declaration();
				setState(146);
				match(Semicolon);
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
					{
					setState(147);
					((ForDeclStatContext)_localctx).cond = expr();
					}
				}

				setState(150);
				match(Semicolon);
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
					{
					setState(151);
					((ForDeclStatContext)_localctx).post = expr();
					}
				}

				setState(154);
				match(Rparen);
				setState(155);
				stat();
				}
				break;
			case 6:
				_localctx = new ForStatContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(157);
				match(T__3);
				setState(158);
				match(Lparen);
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
					{
					setState(159);
					((ForStatContext)_localctx).pre = expr();
					}
				}

				setState(162);
				match(Semicolon);
				setState(164);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
					{
					setState(163);
					((ForStatContext)_localctx).cond = expr();
					}
				}

				setState(166);
				match(Semicolon);
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
					{
					setState(167);
					((ForStatContext)_localctx).post = expr();
					}
				}

				setState(170);
				match(Rparen);
				setState(171);
				stat();
				}
				break;
			case 7:
				_localctx = new WhileStatContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(172);
				match(T__4);
				setState(173);
				match(Lparen);
				setState(174);
				expr();
				setState(175);
				match(Rparen);
				setState(176);
				stat();
				}
				break;
			case 8:
				_localctx = new DoWhileStatContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(178);
				match(T__5);
				setState(179);
				stat();
				setState(180);
				match(T__4);
				setState(181);
				match(Lparen);
				setState(182);
				expr();
				setState(183);
				match(Rparen);
				setState(184);
				match(Semicolon);
				}
				break;
			case 9:
				_localctx = new BreakStatContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(186);
				match(T__6);
				setState(187);
				match(Semicolon);
				}
				break;
			case 10:
				_localctx = new ContinueStatContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(188);
				match(T__7);
				setState(189);
				match(Semicolon);
				}
				break;
			case 11:
				_localctx = new EmptyStatContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(190);
				match(Semicolon);
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

	public static class DeclarationContext extends ParserRuleContext {
		public TyContext ty() {
			return getRuleContext(TyContext.class,0);
		}
		public TerminalNode Ident() { return getToken(DecafParser.Ident, 0); }
		public List<TerminalNode> Lbrkt() { return getTokens(DecafParser.Lbrkt); }
		public TerminalNode Lbrkt(int i) {
			return getToken(DecafParser.Lbrkt, i);
		}
		public List<TerminalNode> Integer() { return getTokens(DecafParser.Integer); }
		public TerminalNode Integer(int i) {
			return getToken(DecafParser.Integer, i);
		}
		public List<TerminalNode> Rbrkt() { return getTokens(DecafParser.Rbrkt); }
		public TerminalNode Rbrkt(int i) {
			return getToken(DecafParser.Rbrkt, i);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			ty(0);
			setState(194);
			match(Ident);
			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Lbrkt) {
				{
				{
				setState(195);
				match(Lbrkt);
				setState(196);
				match(Integer);
				setState(197);
				match(Rbrkt);
				}
				}
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__8) {
				{
				setState(203);
				match(T__8);
				setState(204);
				expr();
				}
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

	public static class ExprContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			assign();
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

	public static class AssignContext extends ParserRuleContext {
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	 
		public AssignContext() { }
		public void copyFrom(AssignContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TAssignContext extends AssignContext {
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public TAssignContext(AssignContext ctx) { copyFrom(ctx); }
	}
	public static class CAssignContext extends AssignContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public AssignOPContext assignOP() {
			return getRuleContext(AssignOPContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public CAssignContext(AssignContext ctx) { copyFrom(ctx); }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assign);
		try {
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				_localctx = new TAssignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				conditional();
				}
				break;
			case 2:
				_localctx = new CAssignContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				unary();
				setState(211);
				assignOP();
				setState(212);
				expr();
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

	public static class ConditionalContext extends ParserRuleContext {
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	 
		public ConditionalContext() { }
		public void copyFrom(ConditionalContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TConditionalContext extends ConditionalContext {
		public LogicOrContext logicOr() {
			return getRuleContext(LogicOrContext.class,0);
		}
		public TConditionalContext(ConditionalContext ctx) { copyFrom(ctx); }
	}
	public static class CConditionalContext extends ConditionalContext {
		public LogicOrContext logicOr() {
			return getRuleContext(LogicOrContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public CConditionalContext(ConditionalContext ctx) { copyFrom(ctx); }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_conditional);
		try {
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				_localctx = new TConditionalContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(216);
				logicOr(0);
				}
				break;
			case 2:
				_localctx = new CConditionalContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(217);
				logicOr(0);
				setState(218);
				match(T__9);
				setState(219);
				expr();
				setState(220);
				match(T__10);
				setState(221);
				conditional();
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

	public static class LogicOrContext extends ParserRuleContext {
		public LogicOrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicOr; }
	 
		public LogicOrContext() { }
		public void copyFrom(LogicOrContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TLogicOrContext extends LogicOrContext {
		public LogicAndContext logicAnd() {
			return getRuleContext(LogicAndContext.class,0);
		}
		public TLogicOrContext(LogicOrContext ctx) { copyFrom(ctx); }
	}
	public static class CLogicOrContext extends LogicOrContext {
		public LogicOrContext logicOr() {
			return getRuleContext(LogicOrContext.class,0);
		}
		public OrOpContext orOp() {
			return getRuleContext(OrOpContext.class,0);
		}
		public LogicAndContext logicAnd() {
			return getRuleContext(LogicAndContext.class,0);
		}
		public CLogicOrContext(LogicOrContext ctx) { copyFrom(ctx); }
	}

	public final LogicOrContext logicOr() throws RecognitionException {
		return logicOr(0);
	}

	private LogicOrContext logicOr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LogicOrContext _localctx = new LogicOrContext(_ctx, _parentState);
		LogicOrContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_logicOr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TLogicOrContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(226);
			logicAnd(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(234);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CLogicOrContext(new LogicOrContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_logicOr);
					setState(228);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(229);
					orOp();
					setState(230);
					logicAnd(0);
					}
					} 
				}
				setState(236);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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

	public static class LogicAndContext extends ParserRuleContext {
		public LogicAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicAnd; }
	 
		public LogicAndContext() { }
		public void copyFrom(LogicAndContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CLogicAndContext extends LogicAndContext {
		public LogicAndContext logicAnd() {
			return getRuleContext(LogicAndContext.class,0);
		}
		public AndOpContext andOp() {
			return getRuleContext(AndOpContext.class,0);
		}
		public EqualContext equal() {
			return getRuleContext(EqualContext.class,0);
		}
		public CLogicAndContext(LogicAndContext ctx) { copyFrom(ctx); }
	}
	public static class TLogicAndContext extends LogicAndContext {
		public EqualContext equal() {
			return getRuleContext(EqualContext.class,0);
		}
		public TLogicAndContext(LogicAndContext ctx) { copyFrom(ctx); }
	}

	public final LogicAndContext logicAnd() throws RecognitionException {
		return logicAnd(0);
	}

	private LogicAndContext logicAnd(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LogicAndContext _localctx = new LogicAndContext(_ctx, _parentState);
		LogicAndContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_logicAnd, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TLogicAndContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(238);
			equal(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(246);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CLogicAndContext(new LogicAndContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_logicAnd);
					setState(240);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(241);
					andOp();
					setState(242);
					equal(0);
					}
					} 
				}
				setState(248);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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

	public static class EqualContext extends ParserRuleContext {
		public EqualContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equal; }
	 
		public EqualContext() { }
		public void copyFrom(EqualContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CEqualContext extends EqualContext {
		public EqualContext equal() {
			return getRuleContext(EqualContext.class,0);
		}
		public EqualOpContext equalOp() {
			return getRuleContext(EqualOpContext.class,0);
		}
		public RelationContext relation() {
			return getRuleContext(RelationContext.class,0);
		}
		public CEqualContext(EqualContext ctx) { copyFrom(ctx); }
	}
	public static class TEqualContext extends EqualContext {
		public RelationContext relation() {
			return getRuleContext(RelationContext.class,0);
		}
		public TEqualContext(EqualContext ctx) { copyFrom(ctx); }
	}

	public final EqualContext equal() throws RecognitionException {
		return equal(0);
	}

	private EqualContext equal(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		EqualContext _localctx = new EqualContext(_ctx, _parentState);
		EqualContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_equal, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TEqualContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(250);
			relation(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(258);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CEqualContext(new EqualContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_equal);
					setState(252);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(253);
					equalOp();
					setState(254);
					relation(0);
					}
					} 
				}
				setState(260);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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

	public static class RelationContext extends ParserRuleContext {
		public RelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation; }
	 
		public RelationContext() { }
		public void copyFrom(RelationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TRelationContext extends RelationContext {
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public TRelationContext(RelationContext ctx) { copyFrom(ctx); }
	}
	public static class CRelationContext extends RelationContext {
		public RelationContext relation() {
			return getRuleContext(RelationContext.class,0);
		}
		public RelationOpContext relationOp() {
			return getRuleContext(RelationOpContext.class,0);
		}
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public CRelationContext(RelationContext ctx) { copyFrom(ctx); }
	}

	public final RelationContext relation() throws RecognitionException {
		return relation(0);
	}

	private RelationContext relation(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RelationContext _localctx = new RelationContext(_ctx, _parentState);
		RelationContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_relation, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TRelationContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(262);
			add(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(270);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CRelationContext(new RelationContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_relation);
					setState(264);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(265);
					relationOp();
					setState(266);
					add(0);
					}
					} 
				}
				setState(272);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
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

	public static class AddContext extends ParserRuleContext {
		public AddContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add; }
	 
		public AddContext() { }
		public void copyFrom(AddContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CAddContext extends AddContext {
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public AddOpContext addOp() {
			return getRuleContext(AddOpContext.class,0);
		}
		public MulContext mul() {
			return getRuleContext(MulContext.class,0);
		}
		public CAddContext(AddContext ctx) { copyFrom(ctx); }
	}
	public static class TAddContext extends AddContext {
		public MulContext mul() {
			return getRuleContext(MulContext.class,0);
		}
		public TAddContext(AddContext ctx) { copyFrom(ctx); }
	}

	public final AddContext add() throws RecognitionException {
		return add(0);
	}

	private AddContext add(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AddContext _localctx = new AddContext(_ctx, _parentState);
		AddContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_add, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TAddContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(274);
			mul(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(282);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CAddContext(new AddContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_add);
					setState(276);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(277);
					addOp();
					setState(278);
					mul(0);
					}
					} 
				}
				setState(284);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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

	public static class MulContext extends ParserRuleContext {
		public MulContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mul; }
	 
		public MulContext() { }
		public void copyFrom(MulContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TMulContext extends MulContext {
		public CastContext cast() {
			return getRuleContext(CastContext.class,0);
		}
		public TMulContext(MulContext ctx) { copyFrom(ctx); }
	}
	public static class CMulContext extends MulContext {
		public MulContext mul() {
			return getRuleContext(MulContext.class,0);
		}
		public MulOpContext mulOp() {
			return getRuleContext(MulOpContext.class,0);
		}
		public CastContext cast() {
			return getRuleContext(CastContext.class,0);
		}
		public CMulContext(MulContext ctx) { copyFrom(ctx); }
	}

	public final MulContext mul() throws RecognitionException {
		return mul(0);
	}

	private MulContext mul(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MulContext _localctx = new MulContext(_ctx, _parentState);
		MulContext _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_mul, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TMulContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(286);
			cast();
			}
			_ctx.stop = _input.LT(-1);
			setState(294);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CMulContext(new MulContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_mul);
					setState(288);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(289);
					mulOp();
					setState(290);
					cast();
					}
					} 
				}
				setState(296);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
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

	public static class CastContext extends ParserRuleContext {
		public CastContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cast; }
	 
		public CastContext() { }
		public void copyFrom(CastContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TCastContext extends CastContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TCastContext(CastContext ctx) { copyFrom(ctx); }
	}
	public static class CCastContext extends CastContext {
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public TyContext ty() {
			return getRuleContext(TyContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public CastContext cast() {
			return getRuleContext(CastContext.class,0);
		}
		public CCastContext(CastContext ctx) { copyFrom(ctx); }
	}

	public final CastContext cast() throws RecognitionException {
		CastContext _localctx = new CastContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cast);
		try {
			setState(303);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				_localctx = new TCastContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				unary();
				}
				break;
			case 2:
				_localctx = new CCastContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(298);
				match(Lparen);
				setState(299);
				ty(0);
				setState(300);
				match(Rparen);
				setState(301);
				cast();
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

	public static class UnaryContext extends ParserRuleContext {
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
	 
		public UnaryContext() { }
		public void copyFrom(UnaryContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TUnaryContext extends UnaryContext {
		public PostfixContext postfix() {
			return getRuleContext(PostfixContext.class,0);
		}
		public TUnaryContext(UnaryContext ctx) { copyFrom(ctx); }
	}
	public static class CUnaryContext extends UnaryContext {
		public UnaryOpContext unaryOp() {
			return getRuleContext(UnaryOpContext.class,0);
		}
		public CastContext cast() {
			return getRuleContext(CastContext.class,0);
		}
		public CUnaryContext(UnaryContext ctx) { copyFrom(ctx); }
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_unary);
		try {
			setState(309);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Lparen:
			case Integer:
			case Ident:
				_localctx = new TUnaryContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				postfix(0);
				}
				break;
			case T__0:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
				_localctx = new CUnaryContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(306);
				unaryOp();
				setState(307);
				cast();
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

	public static class PostfixContext extends ParserRuleContext {
		public PostfixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfix; }
	 
		public PostfixContext() { }
		public void copyFrom(PostfixContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PostfixArrayContext extends PostfixContext {
		public PostfixContext postfix() {
			return getRuleContext(PostfixContext.class,0);
		}
		public TerminalNode Lbrkt() { return getToken(DecafParser.Lbrkt, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Rbrkt() { return getToken(DecafParser.Rbrkt, 0); }
		public PostfixArrayContext(PostfixContext ctx) { copyFrom(ctx); }
	}
	public static class PostfixCallContext extends PostfixContext {
		public TerminalNode Ident() { return getToken(DecafParser.Ident, 0); }
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public PostfixCallContext(PostfixContext ctx) { copyFrom(ctx); }
	}
	public static class TPostfixContext extends PostfixContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TPostfixContext(PostfixContext ctx) { copyFrom(ctx); }
	}

	public final PostfixContext postfix() throws RecognitionException {
		return postfix(0);
	}

	private PostfixContext postfix(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PostfixContext _localctx = new PostfixContext(_ctx, _parentState);
		PostfixContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_postfix, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				_localctx = new TPostfixContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(312);
				atom();
				}
				break;
			case 2:
				{
				_localctx = new PostfixCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(313);
				match(Ident);
				setState(314);
				match(Lparen);
				setState(315);
				argList();
				setState(316);
				match(Rparen);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(327);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PostfixArrayContext(new PostfixContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_postfix);
					setState(320);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(321);
					match(Lbrkt);
					setState(322);
					expr();
					setState(323);
					match(Rbrkt);
					}
					} 
				}
				setState(329);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
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

	public static class ArgListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(DecafParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(DecafParser.Comma, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(338);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << Lparen) | (1L << Integer) | (1L << Ident))) != 0)) {
				{
				setState(330);
				expr();
				setState(335);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(331);
					match(Comma);
					setState(332);
					expr();
					}
					}
					setState(337);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
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

	public static class AtomContext extends ParserRuleContext {
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	 
		public AtomContext() { }
		public void copyFrom(AtomContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AtomIdentContext extends AtomContext {
		public TerminalNode Ident() { return getToken(DecafParser.Ident, 0); }
		public AtomIdentContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class AtomIntegerContext extends AtomContext {
		public TerminalNode Integer() { return getToken(DecafParser.Integer, 0); }
		public AtomIntegerContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class AtomExprContext extends AtomContext {
		public TerminalNode Lparen() { return getToken(DecafParser.Lparen, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(DecafParser.Rparen, 0); }
		public AtomExprContext(AtomContext ctx) { copyFrom(ctx); }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_atom);
		try {
			setState(346);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Integer:
				_localctx = new AtomIntegerContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(340);
				match(Integer);
				}
				break;
			case Lparen:
				_localctx = new AtomExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(341);
				match(Lparen);
				setState(342);
				expr();
				setState(343);
				match(Rparen);
				}
				break;
			case Ident:
				_localctx = new AtomIdentContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(345);
				match(Ident);
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

	public static class UnaryOpContext extends ParserRuleContext {
		public UnaryOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryOp; }
	}

	public final UnaryOpContext unaryOp() throws RecognitionException {
		UnaryOpContext _localctx = new UnaryOpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_unaryOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
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

	public static class AddOpContext extends ParserRuleContext {
		public AddOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addOp; }
	}

	public final AddOpContext addOp() throws RecognitionException {
		AddOpContext _localctx = new AddOpContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_addOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			_la = _input.LA(1);
			if ( !(_la==T__11 || _la==T__15) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
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

	public static class MulOpContext extends ParserRuleContext {
		public MulOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulOp; }
	}

	public final MulOpContext mulOp() throws RecognitionException {
		MulOpContext _localctx = new MulOpContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_mulOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__16) | (1L << T__17))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
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

	public static class RelationOpContext extends ParserRuleContext {
		public RelationOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationOp; }
	}

	public final RelationOpContext relationOp() throws RecognitionException {
		RelationOpContext _localctx = new RelationOpContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_relationOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
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

	public static class EqualOpContext extends ParserRuleContext {
		public EqualOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalOp; }
	}

	public final EqualOpContext equalOp() throws RecognitionException {
		EqualOpContext _localctx = new EqualOpContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_equalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(356);
			_la = _input.LA(1);
			if ( !(_la==T__22 || _la==T__23) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
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

	public static class AndOpContext extends ParserRuleContext {
		public AndOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andOp; }
	}

	public final AndOpContext andOp() throws RecognitionException {
		AndOpContext _localctx = new AndOpContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_andOp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			match(T__24);
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

	public static class OrOpContext extends ParserRuleContext {
		public OrOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orOp; }
	}

	public final OrOpContext orOp() throws RecognitionException {
		OrOpContext _localctx = new OrOpContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_orOp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			match(T__25);
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

	public static class AssignOPContext extends ParserRuleContext {
		public AssignOPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignOP; }
	}

	public final AssignOPContext assignOP() throws RecognitionException {
		AssignOPContext _localctx = new AssignOPContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_assignOP);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(T__8);
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
		case 4:
			return ty_sempred((TyContext)_localctx, predIndex);
		case 12:
			return logicOr_sempred((LogicOrContext)_localctx, predIndex);
		case 13:
			return logicAnd_sempred((LogicAndContext)_localctx, predIndex);
		case 14:
			return equal_sempred((EqualContext)_localctx, predIndex);
		case 15:
			return relation_sempred((RelationContext)_localctx, predIndex);
		case 16:
			return add_sempred((AddContext)_localctx, predIndex);
		case 17:
			return mul_sempred((MulContext)_localctx, predIndex);
		case 20:
			return postfix_sempred((PostfixContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean ty_sempred(TyContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean logicOr_sempred(LogicOrContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean logicAnd_sempred(LogicAndContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean equal_sempred(EqualContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean relation_sempred(RelationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean add_sempred(AddContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean mul_sempred(MulContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean postfix_sempred(PostfixContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)\u016f\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \3\2"+
		"\6\2B\n\2\r\2\16\2C\3\2\3\2\3\3\3\3\3\3\3\3\5\3L\n\3\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\\\n\4\3\5\3\5\3\5\7\5a\n\5"+
		"\f\5\16\5d\13\5\5\5f\n\5\3\6\3\6\3\6\3\6\3\6\7\6m\n\6\f\6\16\6p\13\6\3"+
		"\7\3\7\7\7t\n\7\f\7\16\7w\13\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\177\n\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008f\n\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\5\t\u0097\n\t\3\t\3\t\5\t\u009b\n\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\5\t\u00a3\n\t\3\t\3\t\5\t\u00a7\n\t\3\t\3\t\5\t\u00ab\n\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\5\t\u00c2\n\t\3\n\3\n\3\n\3\n\3\n\7\n\u00c9\n\n\f\n\16\n"+
		"\u00cc\13\n\3\n\3\n\5\n\u00d0\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00d9"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e2\n\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\7\16\u00eb\n\16\f\16\16\16\u00ee\13\16\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\7\17\u00f7\n\17\f\17\16\17\u00fa\13\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\7\20\u0103\n\20\f\20\16\20\u0106\13\20\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\7\21\u010f\n\21\f\21\16\21\u0112\13\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u011b\n\22\f\22\16\22\u011e\13\22"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u0127\n\23\f\23\16\23\u012a\13"+
		"\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0132\n\24\3\25\3\25\3\25\3\25"+
		"\5\25\u0138\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0141\n\26\3"+
		"\26\3\26\3\26\3\26\3\26\7\26\u0148\n\26\f\26\16\26\u014b\13\26\3\27\3"+
		"\27\3\27\7\27\u0150\n\27\f\27\16\27\u0153\13\27\5\27\u0155\n\27\3\30\3"+
		"\30\3\30\3\30\3\30\3\30\5\30\u015d\n\30\3\31\3\31\3\32\3\32\3\33\3\33"+
		"\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \2\n\n\32\34\36 \"$*"+
		"!\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>\2\7"+
		"\4\2\3\3\16\21\4\2\16\16\22\22\4\2\3\3\23\24\3\2\25\30\3\2\31\32\2\u0179"+
		"\2A\3\2\2\2\4K\3\2\2\2\6[\3\2\2\2\be\3\2\2\2\ng\3\2\2\2\fq\3\2\2\2\16"+
		"~\3\2\2\2\20\u00c1\3\2\2\2\22\u00c3\3\2\2\2\24\u00d1\3\2\2\2\26\u00d8"+
		"\3\2\2\2\30\u00e1\3\2\2\2\32\u00e3\3\2\2\2\34\u00ef\3\2\2\2\36\u00fb\3"+
		"\2\2\2 \u0107\3\2\2\2\"\u0113\3\2\2\2$\u011f\3\2\2\2&\u0131\3\2\2\2(\u0137"+
		"\3\2\2\2*\u0140\3\2\2\2,\u0154\3\2\2\2.\u015c\3\2\2\2\60\u015e\3\2\2\2"+
		"\62\u0160\3\2\2\2\64\u0162\3\2\2\2\66\u0164\3\2\2\28\u0166\3\2\2\2:\u0168"+
		"\3\2\2\2<\u016a\3\2\2\2>\u016c\3\2\2\2@B\5\4\3\2A@\3\2\2\2BC\3\2\2\2C"+
		"A\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\7\2\2\3F\3\3\2\2\2GL\5\6\4\2HI\5\22\n"+
		"\2IJ\7&\2\2JL\3\2\2\2KG\3\2\2\2KH\3\2\2\2L\5\3\2\2\2MN\5\n\6\2NO\7(\2"+
		"\2OP\7\37\2\2PQ\5\b\5\2QR\7 \2\2RS\5\f\7\2S\\\3\2\2\2TU\5\n\6\2UV\7(\2"+
		"\2VW\7\37\2\2WX\5\b\5\2XY\7 \2\2YZ\7&\2\2Z\\\3\2\2\2[M\3\2\2\2[T\3\2\2"+
		"\2\\\7\3\2\2\2]b\5\22\n\2^_\7%\2\2_a\5\22\n\2`^\3\2\2\2ad\3\2\2\2b`\3"+
		"\2\2\2bc\3\2\2\2cf\3\2\2\2db\3\2\2\2e]\3\2\2\2ef\3\2\2\2f\t\3\2\2\2gh"+
		"\b\6\1\2hi\7\35\2\2in\3\2\2\2jk\f\3\2\2km\7\3\2\2lj\3\2\2\2mp\3\2\2\2"+
		"nl\3\2\2\2no\3\2\2\2o\13\3\2\2\2pn\3\2\2\2qu\7#\2\2rt\5\16\b\2sr\3\2\2"+
		"\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7$\2\2y\r\3\2\2"+
		"\2z\177\5\20\t\2{|\5\22\n\2|}\7&\2\2}\177\3\2\2\2~z\3\2\2\2~{\3\2\2\2"+
		"\177\17\3\2\2\2\u0080\u0081\7\36\2\2\u0081\u0082\5\24\13\2\u0082\u0083"+
		"\7&\2\2\u0083\u00c2\3\2\2\2\u0084\u0085\5\24\13\2\u0085\u0086\7&\2\2\u0086"+
		"\u00c2\3\2\2\2\u0087\u0088\7\4\2\2\u0088\u0089\7\37\2\2\u0089\u008a\5"+
		"\24\13\2\u008a\u008b\7 \2\2\u008b\u008e\5\20\t\2\u008c\u008d\7\5\2\2\u008d"+
		"\u008f\5\20\t\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u00c2\3"+
		"\2\2\2\u0090\u00c2\5\f\7\2\u0091\u0092\7\6\2\2\u0092\u0093\7\37\2\2\u0093"+
		"\u0094\5\22\n\2\u0094\u0096\7&\2\2\u0095\u0097\5\24\13\2\u0096\u0095\3"+
		"\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\7&\2\2\u0099"+
		"\u009b\5\24\13\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3"+
		"\2\2\2\u009c\u009d\7 \2\2\u009d\u009e\5\20\t\2\u009e\u00c2\3\2\2\2\u009f"+
		"\u00a0\7\6\2\2\u00a0\u00a2\7\37\2\2\u00a1\u00a3\5\24\13\2\u00a2\u00a1"+
		"\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\7&\2\2\u00a5"+
		"\u00a7\5\24\13\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3"+
		"\2\2\2\u00a8\u00aa\7&\2\2\u00a9\u00ab\5\24\13\2\u00aa\u00a9\3\2\2\2\u00aa"+
		"\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7 \2\2\u00ad\u00c2\5\20"+
		"\t\2\u00ae\u00af\7\7\2\2\u00af\u00b0\7\37\2\2\u00b0\u00b1\5\24\13\2\u00b1"+
		"\u00b2\7 \2\2\u00b2\u00b3\5\20\t\2\u00b3\u00c2\3\2\2\2\u00b4\u00b5\7\b"+
		"\2\2\u00b5\u00b6\5\20\t\2\u00b6\u00b7\7\7\2\2\u00b7\u00b8\7\37\2\2\u00b8"+
		"\u00b9\5\24\13\2\u00b9\u00ba\7 \2\2\u00ba\u00bb\7&\2\2\u00bb\u00c2\3\2"+
		"\2\2\u00bc\u00bd\7\t\2\2\u00bd\u00c2\7&\2\2\u00be\u00bf\7\n\2\2\u00bf"+
		"\u00c2\7&\2\2\u00c0\u00c2\7&\2\2\u00c1\u0080\3\2\2\2\u00c1\u0084\3\2\2"+
		"\2\u00c1\u0087\3\2\2\2\u00c1\u0090\3\2\2\2\u00c1\u0091\3\2\2\2\u00c1\u009f"+
		"\3\2\2\2\u00c1\u00ae\3\2\2\2\u00c1\u00b4\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1"+
		"\u00be\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\21\3\2\2\2\u00c3\u00c4\5\n\6"+
		"\2\u00c4\u00ca\7(\2\2\u00c5\u00c6\7!\2\2\u00c6\u00c7\7\'\2\2\u00c7\u00c9"+
		"\7\"\2\2\u00c8\u00c5\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca"+
		"\u00cb\3\2\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7\13"+
		"\2\2\u00ce\u00d0\5\24\13\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0"+
		"\23\3\2\2\2\u00d1\u00d2\5\26\f\2\u00d2\25\3\2\2\2\u00d3\u00d9\5\30\r\2"+
		"\u00d4\u00d5\5(\25\2\u00d5\u00d6\5> \2\u00d6\u00d7\5\24\13\2\u00d7\u00d9"+
		"\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9\27\3\2\2\2\u00da"+
		"\u00e2\5\32\16\2\u00db\u00dc\5\32\16\2\u00dc\u00dd\7\f\2\2\u00dd\u00de"+
		"\5\24\13\2\u00de\u00df\7\r\2\2\u00df\u00e0\5\30\r\2\u00e0\u00e2\3\2\2"+
		"\2\u00e1\u00da\3\2\2\2\u00e1\u00db\3\2\2\2\u00e2\31\3\2\2\2\u00e3\u00e4"+
		"\b\16\1\2\u00e4\u00e5\5\34\17\2\u00e5\u00ec\3\2\2\2\u00e6\u00e7\f\3\2"+
		"\2\u00e7\u00e8\5<\37\2\u00e8\u00e9\5\34\17\2\u00e9\u00eb\3\2\2\2\u00ea"+
		"\u00e6\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2"+
		"\2\2\u00ed\33\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\b\17\1\2\u00f0\u00f1"+
		"\5\36\20\2\u00f1\u00f8\3\2\2\2\u00f2\u00f3\f\3\2\2\u00f3\u00f4\5:\36\2"+
		"\u00f4\u00f5\5\36\20\2\u00f5\u00f7\3\2\2\2\u00f6\u00f2\3\2\2\2\u00f7\u00fa"+
		"\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\35\3\2\2\2\u00fa"+
		"\u00f8\3\2\2\2\u00fb\u00fc\b\20\1\2\u00fc\u00fd\5 \21\2\u00fd\u0104\3"+
		"\2\2\2\u00fe\u00ff\f\3\2\2\u00ff\u0100\58\35\2\u0100\u0101\5 \21\2\u0101"+
		"\u0103\3\2\2\2\u0102\u00fe\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2"+
		"\2\2\u0104\u0105\3\2\2\2\u0105\37\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108"+
		"\b\21\1\2\u0108\u0109\5\"\22\2\u0109\u0110\3\2\2\2\u010a\u010b\f\3\2\2"+
		"\u010b\u010c\5\66\34\2\u010c\u010d\5\"\22\2\u010d\u010f\3\2\2\2\u010e"+
		"\u010a\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2"+
		"\2\2\u0111!\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\b\22\1\2\u0114\u0115"+
		"\5$\23\2\u0115\u011c\3\2\2\2\u0116\u0117\f\3\2\2\u0117\u0118\5\62\32\2"+
		"\u0118\u0119\5$\23\2\u0119\u011b\3\2\2\2\u011a\u0116\3\2\2\2\u011b\u011e"+
		"\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d#\3\2\2\2\u011e"+
		"\u011c\3\2\2\2\u011f\u0120\b\23\1\2\u0120\u0121\5&\24\2\u0121\u0128\3"+
		"\2\2\2\u0122\u0123\f\3\2\2\u0123\u0124\5\64\33\2\u0124\u0125\5&\24\2\u0125"+
		"\u0127\3\2\2\2\u0126\u0122\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2"+
		"\2\2\u0128\u0129\3\2\2\2\u0129%\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u0132"+
		"\5(\25\2\u012c\u012d\7\37\2\2\u012d\u012e\5\n\6\2\u012e\u012f\7 \2\2\u012f"+
		"\u0130\5&\24\2\u0130\u0132\3\2\2\2\u0131\u012b\3\2\2\2\u0131\u012c\3\2"+
		"\2\2\u0132\'\3\2\2\2\u0133\u0138\5*\26\2\u0134\u0135\5\60\31\2\u0135\u0136"+
		"\5&\24\2\u0136\u0138\3\2\2\2\u0137\u0133\3\2\2\2\u0137\u0134\3\2\2\2\u0138"+
		")\3\2\2\2\u0139\u013a\b\26\1\2\u013a\u0141\5.\30\2\u013b\u013c\7(\2\2"+
		"\u013c\u013d\7\37\2\2\u013d\u013e\5,\27\2\u013e\u013f\7 \2\2\u013f\u0141"+
		"\3\2\2\2\u0140\u0139\3\2\2\2\u0140\u013b\3\2\2\2\u0141\u0149\3\2\2\2\u0142"+
		"\u0143\f\3\2\2\u0143\u0144\7!\2\2\u0144\u0145\5\24\13\2\u0145\u0146\7"+
		"\"\2\2\u0146\u0148\3\2\2\2\u0147\u0142\3\2\2\2\u0148\u014b\3\2\2\2\u0149"+
		"\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a+\3\2\2\2\u014b\u0149\3\2\2\2"+
		"\u014c\u0151\5\24\13\2\u014d\u014e\7%\2\2\u014e\u0150\5\24\13\2\u014f"+
		"\u014d\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2"+
		"\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u014c\3\2\2\2\u0154"+
		"\u0155\3\2\2\2\u0155-\3\2\2\2\u0156\u015d\7\'\2\2\u0157\u0158\7\37\2\2"+
		"\u0158\u0159\5\24\13\2\u0159\u015a\7 \2\2\u015a\u015d\3\2\2\2\u015b\u015d"+
		"\7(\2\2\u015c\u0156\3\2\2\2\u015c\u0157\3\2\2\2\u015c\u015b\3\2\2\2\u015d"+
		"/\3\2\2\2\u015e\u015f\t\2\2\2\u015f\61\3\2\2\2\u0160\u0161\t\3\2\2\u0161"+
		"\63\3\2\2\2\u0162\u0163\t\4\2\2\u0163\65\3\2\2\2\u0164\u0165\t\5\2\2\u0165"+
		"\67\3\2\2\2\u0166\u0167\t\6\2\2\u01679\3\2\2\2\u0168\u0169\7\33\2\2\u0169"+
		";\3\2\2\2\u016a\u016b\7\34\2\2\u016b=\3\2\2\2\u016c\u016d\7\13\2\2\u016d"+
		"?\3\2\2\2\"CK[benu~\u008e\u0096\u009a\u00a2\u00a6\u00aa\u00c1\u00ca\u00cf"+
		"\u00d8\u00e1\u00ec\u00f8\u0104\u0110\u011c\u0128\u0131\u0137\u0140\u0149"+
		"\u0151\u0154\u015c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}