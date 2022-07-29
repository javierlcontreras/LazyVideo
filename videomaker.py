import random
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from downloader import Downloader
from parser import Parser 
import tqdm
import glob
import os

FRAMES_PER_SEC = 100
class VideoMaker():
	def __init__(self, img_path, output_path):
		self.IMG_PATH = img_path
		self.output_path = output_path

	def write_text_on_img(self, img, word, W, H):
		fontsize = 200

		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
		pil_im = Image.fromarray(img)
		draw = ImageDraw.Draw(pil_im)  
		color = (0,0,0)
		
		while True:
			font = ImageFont.truetype(self.IMG_PATH + "/../lazyvideo/fonts/SODORBld.ttf", fontsize)	

			x1, y1, x2, y2 = draw.textbbox((0,0), word, font=font)
			w = x2 - x1
			h = y2 - y1
			if w > 0.7*W or h > 0.7*H: fontsize -= 1
			else:
				break

		draw.text(((W-w)/2,(H-h)/2), word.replace("-", " "), font=font, fill="white", stroke_width=fontsize//10, stroke_fill="black")

		img = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  

		return img

	def img_resize(self, img, W, H):
		(h, w, c) = np.shape(img)

		back = np.zeros((H, W, 3), dtype = "uint8")

		if w/W > h/H:
			swidth = W
			sheight = h*W/w
		else:
			sheight = H
			swidth = w*H/h
		
		sheight = int(sheight)
		swidth = int(swidth)
		img = cv2.resize(img, (swidth, sheight), interpolation = cv2.INTER_AREA)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
		
		pil_back = Image.fromarray(back)
		pil_img = Image.fromarray(img)
		dx = W/2 - swidth/2
		dy = H/2 - sheight/2
		dx = int(dx)
		dy = int(dy)
		pil_back.paste(pil_img, (dx, dy))

		img = cv2.cvtColor(np.array(pil_back), cv2.COLOR_RGB2BGR)  
		return img

	def make_video(self, instrs):
		
		width = 390
		height = 844

		fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
		video = cv2.VideoWriter(self.output_path, fourcc, FRAMES_PER_SEC, (width, height))
		
		downloader = Downloader(self.IMG_PATH) 
		for instr in tqdm.tqdm(instrs):
			word = instr["word"]
			back = instr["back"]
			time = instr["time"]

			backp = downloader.word_already_downloaded(back)
			imgfile = glob.glob(f"{self.IMG_PATH}/{backp}/*")[0]
			print(imgfile)
			img = cv2.imread(imgfile)
			img = self.img_resize(img, width, height)			
			img = self.write_text_on_img(img, word, width, height)

			#cv2.imshow('image',img)
			#cv2.waitKey(0)
			for i in range(time):
				video.write(img)

		#cv2.destroyAllWindows()
		video.release()

	def add_music(self):
		musicfile = random.choice(glob.glob("music/*"))
		os.system(f"ffmpeg -i video.mp4 -i {musicfile} -c copy -map 0:v -map 1:a -c:v copy -shortest -y video_music.mp4")

	def compute_time(self, word, pause):
		time = len(word)*FRAMES_PER_SEC//20
		time += word.count(".")*FRAMES_PER_SEC//5
		time += word.count("?")*FRAMES_PER_SEC//5
		time += word.count("!")*FRAMES_PER_SEC//5
		time += word.count(",")*FRAMES_PER_SEC//10
		time += word.count(";")*FRAMES_PER_SEC//10
		return time + pause*FRAMES_PER_SEC//10

	def propagate_modifiers(self, instrs):
		last_back = "black_wallpaper"
		for instr in instrs:
			hide = False
			pause = 0
			back = instr["word"]
			for mod in instr["modifiers"]:
				if mod["type"] == "hide": hide = True
				if mod["type"] == "pause": pause = mod["time"]
				if mod["type"] == "back": back = mod["back"]

			if not hide: last_back = Parser.simplify_word(back)
			instr["back"] = last_back
			instr["time"] = self.compute_time(instr["word"], pause)
			print(instr)
		return instrs
