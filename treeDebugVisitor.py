# Generated from lazyvideo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lazyvideoLexer import lazyvideoLexer
    from .lazyvideoParser import lazyvideoParser
else:
    from lazyvideoLexer import lazyvideoLexer
    from lazyvideoParser import lazyvideoParser

# This class defines a complete generic visitor for a parse tree produced by lazyvideoParser.

class TreeDebugVisitor(ParseTreeVisitor):

    def msgBuild(self, name, ctx):
        msg = name + "("
        li = list(ctx.getChildren())
        for i in range(len(li)):
            msgch = self.visit(li[i])
            if msgch != None:
                msg += msgch + ","
        if msg.endswith(","): msg = msg[:-1]
        msg = msg + ")"
        return msg

    # Visit a parse tree produced by lazyvideoParser#root.
    def visitRoot(self, ctx:lazyvideoParser.RootContext):
        return self.msgBuild("Root", ctx)


    # Visit a parse tree produced by lazyvideoParser#instruction.
    def visitInstruction(self, ctx:lazyvideoParser.InstructionContext):
        return self.msgBuild("Instruction", ctx)
        

    # Visit a parse tree produced by lazyvideoParser#wordslide.
    def visitWordslide(self, ctx:lazyvideoParser.WordslideContext):
        return self.msgBuild("WordSlide", ctx)
        

    # Visit a parse tree produced by lazyvideoParser#sentenceslide.
    def visitSentenceslide(self, ctx:lazyvideoParser.SentenceslideContext):
        return self.msgBuild("SentenceSlide", ctx)
        

    # Visit a parse tree produced by lazyvideoParser#modifiers.
    def visitModifiers(self, ctx:lazyvideoParser.ModifiersContext):
        return self.msgBuild("Modifiers", ctx)
        

    # Visit a parse tree produced by lazyvideoParser#modifier.
    def visitModifier(self, ctx:lazyvideoParser.ModifierContext):
        return self.msgBuild("Modifier", ctx)
        

def main():
    text = open("input.txt").read()
    print(text)
    input_stream = InputStream(text)
    lexer = lazyvideoLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    parser = lazyvideoParser(token_stream)
    tree = parser.root()
    debug_visitor = TreeDebugVisitor()
    print( debug_visitor.visit(tree) )

if __name__ == "__main__": main()


del lazyvideoParser