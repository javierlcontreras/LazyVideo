import os
from icrawler.builtin import BaiduImageCrawler
from parser import Parser
import glob
import simple_image_download.simple_image_download as simp 
import numpy as np
import cv2

class Downloader():
	def __init__(self, path):
		self.IMG_PATH = path
		self.response = simp.simple_image_download()
 
	def word_already_downloaded(self, word, debug=False):
		word = Parser.simplify_word(word)
		wordlist = os.listdir(self.IMG_PATH)
		for item in wordlist:
			if word == item and len(glob.glob(f'{self.IMG_PATH}/{word}/*')) >= 1:
				if debug: print("ALREADY HAVE IT, Folder: ", word)
				return item
		return ""

	def cleanup(self, level=1):
		for file in glob.glob(f"{self.IMG_PATH}/*/*"):
			if file.endswith("_1.jpg") or file.endswith("_2.jpg") or file.endswith("_3.jpg"):
				os.system(f"rm {file}")
			img = cv2.imread(file)
			if np.shape(img) == ():
				os.system(f"rm {file}")

		failed = False
		for fold in glob.glob(f"{self.IMG_PATH}/*"):
			word = fold.split("/")[-1]
			if not self.word_already_downloaded(word):
				self.crawl_image_for(word, "extra", "extra", limit=10 * (level + 1))
				failed = True
		if failed: self.cleanup(level=level+1)

	def crawl_image_for(self, word, it, total, limit=10):
		word = Parser.simplify_word(word)
		if self.word_already_downloaded(word, debug=True) != "":
			return
		print(f"-------------- Downloading {it}/{total}: " + word + ", Limit: " + str(limit) + "-----------------")

		self.response.download(word, limit=limit)


	def download(self, instrs):
		for i_instr, instr in enumerate(instrs):
			word = instr["back"]
			
			hide = False
			for mod in instr["modifiers"]:
				if mod["type"] == "hide":
					hide = True

			if hide: continue

			self.crawl_image_for(word, i_instr, len(instrs))
