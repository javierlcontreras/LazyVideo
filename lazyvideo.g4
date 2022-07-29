grammar lazyvideo;

root : (instruction)* EOF;

instruction : 
	WORD modifiers				#WordSlide 
	| '(' WORD+ ')' modifiers 	#SentenceSlide;

modifiers : modifier modifiers | ;

modifier : NUM | '*' | BACK;

WORD : [¿¡"']* [\-'áàäéèëíìïóòöúùüÁÀÄÉÈËÍÌÏÓÒÖÚÙÜñÑa-zA-Z0-9]+ [.,;:?!'"]*;
NUM : '[' [0-9]+ ']';
BACK : '{' [a-zA-Z0-9_ ]+ '}';

WS : [ \t\n]+ -> skip ;
