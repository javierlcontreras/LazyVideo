import argparse
from parser import Parser
from downloader import Downloader
from videomaker import VideoMaker

IMG_PATH = "/home/jlcontreras/Desktop/RandomProjects/LazyJavier/text2images/simple_images"

def getargs():
	parser = argparse.ArgumentParser(
		description='Make a Lazy video from a LazyLang Text.'
	)
	parser.add_argument('--input', type=str, help='Relative path of input file')
	parser.add_argument('--output', type=str, help='Relative path of output file', default="./video.mp4")

	args = parser.parse_args()

	if args.input == None:
		print("No input!")
		return None

	return args

def gettext(path):
	with open(path, "r") as o:
		return o.read()

def main():	
	args = getargs()
	if args == None: return

	text = gettext(args.input)
	inst = Parser.get_instructions(text)

	downloader = Downloader(IMG_PATH)
	videomaker = VideoMaker(IMG_PATH, args.output)

	inst = videomaker.propagate_modifiers(inst)
	downloader.download(inst)
	downloader.cleanup()
	
	videomaker.make_video(inst)
	videomaker.add_music()
	
if __name__ == "__main__": main()