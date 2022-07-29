# Generated from lazyvideo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lazyvideoLexer import lazyvideoLexer
    from .lazyvideoParser import lazyvideoParser
else:
    from lazyvideoLexer import lazyvideoLexer
    from lazyvideoParser import lazyvideoParser

# This class defines a complete generic visitor for a parse tree produced by lazyvideoParser.

class InstructionVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by lazyvideoParser#root.
    def visitRoot(self, ctx:lazyvideoParser.RootContext):
        instructions = []
        chld = list(ctx.getChildren())
        for i in range(len(chld) - 1):
            instruction = self.visit(chld[i])
            if instruction != None:
                instructions.append(instruction)
        return instructions

    # Visit a parse tree produced by lazyvideoParser#wordslide.
    def visitWordSlide(self, ctx:lazyvideoParser.WordSlideContext):
        chld = list(ctx.getChildren())
        word = chld[0].getText()
        modifiers = self.visit(chld[1])
        return {"word":word, "modifiers":modifiers}
        

    # Visit a parse tree produced by lazyvideoParser#sentenceslide.
    def visitSentenceSlide(self, ctx:lazyvideoParser.SentenceSlideContext):
        chld = list(ctx.getChildren())
        words = ""
        for i in range(1, len(chld) - 2):
            words = words + " " + chld[i].getText()
        modifiers = self.visit(chld[-1])
        return {"word":words[1:], "modifiers":modifiers}
        

    # Visit a parse tree produced by lazyvideoParser#modifiers.
    def visitModifiers(self, ctx:lazyvideoParser.ModifiersContext):
        chld = list(ctx.getChildren())
        if len(chld) == 0: return []
        mod = self.visit(chld[0])
        mods = self.visit(chld[1])
        return [mod] + mods        

    # Visit a parse tree produced by lazyvideoParser#modifier.
    def visitModifier(self, ctx:lazyvideoParser.ModifierContext):
        chld = list(ctx.getChildren())
        text = chld[0].getText()
        if text == "*":
            return {"type": "hide"}
        elif text.endswith("]") and text.startswith("["):
            time = int(text[1:-1])
            return {"type": "pause", "time":time}
        elif text.endswith("}") and text.startswith("{"):
            back = text[1:-1]
            return {"type": "back", "back":back}

def main():
    text = open("input.txt").read()
    print(text)
    input_stream = InputStream(text)
    lexer = lazyvideoLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    parser = lazyvideoParser(token_stream)
    tree = parser.root()
    debug_visitor = InstructionVisitor()
    print( debug_visitor.visit(tree) )

if __name__ == "__main__": main()


del lazyvideoParser