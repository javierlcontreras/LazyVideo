# Generated from lazyvideo.g4 by ANTLR 4.10.1
from antlr4 import *

from lazyvideoLexer import lazyvideoLexer
from lazyvideoParser import lazyvideoParser
from instructionVisitor import InstructionVisitor

class Parser():
	def __init__(self):
		pass

	@staticmethod
	def get_instructions(text):
	    input_stream = InputStream(text)
	    lexer = lazyvideoLexer(input_stream)

	    token_stream = CommonTokenStream(lexer)
	    parser = lazyvideoParser(token_stream)
	    tree = parser.root()
	    debug_visitor = InstructionVisitor()
	    
	    instructions = debug_visitor.visit(tree)

#	    for instruction in instructions:
#	    	print(instruction)

	    return instructions

	@staticmethod
	def simplify_word(word):
		lfrom, lto = 'áàäéèëíìïóòöúùüÁÀÄÉÈËÍÌÏÓÒÖÚÙÜ','aaaeeeiiiooouuuAAAEEEIIIOOOUUU'
		word = word.translate(str.maketrans(lfrom,lto))
		
		alphabet = [chr(ord('a') + i) for i in range(ord('z') - ord('a') + 1)] \
				   + [chr(ord('A') + i) for i in range(ord('Z') - ord('A') + 1)] \
				   + [str(i) for i in range(10)] \
				   + ["-", "ñ", "Ñ", " ", "_"]
		sword = ""
		for ch in word:
			if ch in alphabet:
				sword += ch
		return sword.lower().strip("'-,.?¿!¡;").replace(" ", "_")
