# LazyVideo
Given a text with annotations, it searches and downloads Google Images and generates a text-on-image slide-show. 

Annotation to video making instructions is implemented through a custom grammar, an **ANTRL** lexer and parser and a custom visitor. Video Instructions to video is implemented using the python libraries **cv2** and **Pillow**. 

## Annotations
There are two types of annotations, coupling slides and slide modifiers.

### Coupling slides 
	(word1 word2 ...)		make a multi-word slide
Word1, word2... will appear in the same slide.

### Slide Modifiers
Modifiers come at the end of the word/sentence.

	{word}					changes default background search to word
The slide (Hello all!){man waving} will have a man waving background.

	[N]					pauses N tenths of a second
The slide (Hi!)[10] will have an extra 10 tenths of second screen time added to its default time. Default times depend on the number of letters of the slide and its puntuations symbols.

	*					doesn't change background for that slide
The slide (Hello world!)* will have the previos slide's background. If it is the first slide, it will have a black background.

## Grammar
You can find the complete Grammar in lazyvideo.g4.

## Example
	(Instead of)				{arrow}				[10]
	("Have a nice day")			{sunny day}			[5]
	(think I'll start saying)		{start}				[5]
	("Have the day you deserve")		{angry man drawing}		[5]
	(You know,)				{karma}				[5]
	(let Karma sort that shit out.)		*				[10]

## Execution

To execute **LazyVideo**, use
```bash
python3 lazyvideo.py --input <input-file-path>
```

If you want to modify the grammar, build the **ANTRL** files with
```{bash}
antlr4 -Dlanguage=Python3 -no-listener -visitor lazyvideo.g4
```
