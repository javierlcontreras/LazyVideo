# Generated from lazyvideo.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,4,1,21,8,1,11,1,12,1,22,1,1,1,1,
        3,1,27,8,1,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,0,0,4,0,2,4,6,
        0,1,2,0,3,3,5,6,36,0,11,1,0,0,0,2,26,1,0,0,0,4,32,1,0,0,0,6,34,1,
        0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,1,0,0,0,16,
        17,5,4,0,0,17,27,3,4,2,0,18,20,5,1,0,0,19,21,5,4,0,0,20,19,1,0,0,
        0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,
        5,2,0,0,25,27,3,4,2,0,26,16,1,0,0,0,26,18,1,0,0,0,27,3,1,0,0,0,28,
        29,3,6,3,0,29,30,3,4,2,0,30,33,1,0,0,0,31,33,1,0,0,0,32,28,1,0,0,
        0,32,31,1,0,0,0,33,5,1,0,0,0,34,35,7,0,0,0,35,7,1,0,0,0,4,11,22,
        26,32
    ]

class lazyvideoParser ( Parser ):

    grammarFileName = "lazyvideo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WORD", "NUM", "BACK", "WS" ]

    RULE_root = 0
    RULE_instruction = 1
    RULE_modifiers = 2
    RULE_modifier = 3

    ruleNames =  [ "root", "instruction", "modifiers", "modifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WORD=4
    NUM=5
    BACK=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(lazyvideoParser.EOF, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lazyvideoParser.InstructionContext)
            else:
                return self.getTypedRuleContext(lazyvideoParser.InstructionContext,i)


        def getRuleIndex(self):
            return lazyvideoParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lazyvideoParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lazyvideoParser.T__0 or _la==lazyvideoParser.WORD:
                self.state = 8
                self.instruction()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(lazyvideoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lazyvideoParser.RULE_instruction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WordSlideContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lazyvideoParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(lazyvideoParser.WORD, 0)
        def modifiers(self):
            return self.getTypedRuleContext(lazyvideoParser.ModifiersContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWordSlide" ):
                return visitor.visitWordSlide(self)
            else:
                return visitor.visitChildren(self)


    class SentenceSlideContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lazyvideoParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def modifiers(self):
            return self.getTypedRuleContext(lazyvideoParser.ModifiersContext,0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(lazyvideoParser.WORD)
            else:
                return self.getToken(lazyvideoParser.WORD, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenceSlide" ):
                return visitor.visitSentenceSlide(self)
            else:
                return visitor.visitChildren(self)



    def instruction(self):

        localctx = lazyvideoParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lazyvideoParser.WORD]:
                localctx = lazyvideoParser.WordSlideContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(lazyvideoParser.WORD)
                self.state = 17
                self.modifiers()
                pass
            elif token in [lazyvideoParser.T__0]:
                localctx = lazyvideoParser.SentenceSlideContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(lazyvideoParser.T__0)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 19
                    self.match(lazyvideoParser.WORD)
                    self.state = 22 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==lazyvideoParser.WORD):
                        break

                self.state = 24
                self.match(lazyvideoParser.T__1)
                self.state = 25
                self.modifiers()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modifier(self):
            return self.getTypedRuleContext(lazyvideoParser.ModifierContext,0)


        def modifiers(self):
            return self.getTypedRuleContext(lazyvideoParser.ModifiersContext,0)


        def getRuleIndex(self):
            return lazyvideoParser.RULE_modifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifiers" ):
                return visitor.visitModifiers(self)
            else:
                return visitor.visitChildren(self)




    def modifiers(self):

        localctx = lazyvideoParser.ModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modifiers)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lazyvideoParser.T__2, lazyvideoParser.NUM, lazyvideoParser.BACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.modifier()
                self.state = 29
                self.modifiers()
                pass
            elif token in [lazyvideoParser.EOF, lazyvideoParser.T__0, lazyvideoParser.WORD]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(lazyvideoParser.NUM, 0)

        def BACK(self):
            return self.getToken(lazyvideoParser.BACK, 0)

        def getRuleIndex(self):
            return lazyvideoParser.RULE_modifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifier" ):
                return visitor.visitModifier(self)
            else:
                return visitor.visitChildren(self)




    def modifier(self):

        localctx = lazyvideoParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lazyvideoParser.T__2) | (1 << lazyvideoParser.NUM) | (1 << lazyvideoParser.BACK))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





