# Generated from lazyvideo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lazyvideoParser import lazyvideoParser
else:
    from lazyvideoParser import lazyvideoParser

# This class defines a complete generic visitor for a parse tree produced by lazyvideoParser.

class lazyvideoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lazyvideoParser#root.
    def visitRoot(self, ctx:lazyvideoParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lazyvideoParser#WordSlide.
    def visitWordSlide(self, ctx:lazyvideoParser.WordSlideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lazyvideoParser#SentenceSlide.
    def visitSentenceSlide(self, ctx:lazyvideoParser.SentenceSlideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lazyvideoParser#modifiers.
    def visitModifiers(self, ctx:lazyvideoParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lazyvideoParser#modifier.
    def visitModifier(self, ctx:lazyvideoParser.ModifierContext):
        return self.visitChildren(ctx)



del lazyvideoParser