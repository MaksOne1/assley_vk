import math
import os
import time
from tkinter.tix import MAX
import urllib.request
from PIL import Image
import PIL
import shutil

from itertools import product


class ImageParser(object):
	def __init__(self):
		pass
	
	def download(self, dir, index, hrefs):
		images = []
		for (i, pic) in enumerate(hrefs):
			filename = str(i) + '.jpg'
			path = os.path.join(__file__, '..', 'assets', dir, str(index))
			os.makedirs(path, exist_ok=True)
			full_path = os.path.join(path, filename)
			try:
				opener = urllib.request.build_opener()
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				urllib.request.install_opener(opener)
				urllib.request.urlretrieve(pic, full_path)
				time.sleep(1/8)
			except:
				print(pic)
			images.append(full_path)
		return images
	

	def slice(filename, dir_in, dir_out, d):
		name, ext = os.path.splitext(filename)
		img = Image.open(os.path.join(dir_in, filename))
		w, h = img.size
		os.makedirs(dir_out, exist_ok=True)

		grid = product(range(0, h-h % d, d), 0)
		sliced_images = []
		for i, j in grid:
			box = (j, i, j+d, i+d)
			out = os.path.join(dir_out, f'{name}_{j}{ext}')
			img.crop(box).save(out)
			sliced_images.append(os.path.join(dir_out, f'{name}_{j}{ext}'))
		return sliced_images
	
	def join(self, dir, index, images):
		path = os.path.join(__file__, '..',
							'assets', dir)
		MAX_HEIGHT = 65535
		images = [Image.open(x)
                    for x in images]
		pages = []
		total_page_height = 0
		last_page = -1
		widths, heights = zip(*(i.size for i in images))
		max_width = max(widths)

		for (i, im) in enumerate(images):
			height = im.size[1]
			if i == len(images) - 1:
				pages.append((last_page + 1, i, total_page_height + height))
			elif height + total_page_height < MAX_HEIGHT:
				total_page_height += height
			else: 
				pages.append((last_page + 1, i, total_page_height))
				total_page_height = 0
				last_page = i
		
		paths = []
		for (i, page) in enumerate(pages):
			page_image = images[page[0]:page[1]]
   
			new_im = Image.new('RGB', (max_width, page[2]))
			y_offset = 0
			for img in page_image:
				new_im.paste(img, (0, y_offset))
				y_offset += img.size[1]
			full_path = os.path.join(path, 'concat', str(index))
			os.makedirs(full_path, exist_ok=True)
			img_path = os.path.join(full_path, str(i) + 'concat.jpg')
			new_im.save(img_path)
			paths.append(img_path)
   
		return paths


	def upload(self):
		pass
