#!/usr/bin/env python

import sys

import aalib
import Image
import os

#import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import imghdr
import ImageOps

imagefilename=str(sys.argv[1]).strip()

#These two variables control the resolution and font size.  They are interconnected.
#img_new_magnitude
#fontsize

try:
	img_new_magnitude= int (str(sys.argv[2]).strip() )
except :
	img_new_magnitude=4

try:
	fontsize= int (str(sys.argv[3]).strip())
except :
	fontsize= 15

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", fontsize, encoding="unic")


def create_ascii_image():
	global name
	name,typ=imagefilename.split(".")
	
	global image_width, image_height
	image_width, image_height = Image.open(imagefilename).size
	
	def make_screen_and_image(aalib_screen_width,aalib_screen_height):
		screen = aalib.AsciiScreen(width=aalib_screen_width, height=aalib_screen_height )
		im= Image.open(imagefilename).convert("L").resize(screen.virtual_size)
		return screen,im
	
	

	def  make_img():
		
		aalib_screen_width= int(image_width/30)*img_new_magnitude
		aalib_screen_height= int(image_height/45)*img_new_magnitude
		
		screen,im=make_screen_and_image(aalib_screen_width,aalib_screen_height)
		screen.put_image((0,0), im)

		y = 0
	
		how_many_rows = len ( screen.render().splitlines() ) 

		new_img_width, font_size = font.getsize (screen.render().splitlines()[0])	

		img=Image.new('RGB', (new_img_width, how_many_rows*font_size),(120,20,20))
		draw = ImageDraw.Draw(img)
	
		for lines in screen.render().splitlines():
			draw.text( (0,y), lines, (255,255,0),font=font )
			y = y + font_size
		

		imagefit = ImageOps.fit(img, (image_width, image_height), Image.ANTIALIAS)
		return imagefit

	

	def make_text():
		screen,im=make_screen_and_image(80,40)
	
		screen.put_image((0,0), im)
		
		p=open(name+".txt","w")
		q=screen.render()
		p.write(q)
		p.close()

	def norm():
		image=make_img()
		image.save(name+"_converted.jpg", "JPEG")

	def gray():
		image=make_img()
		gray_img=ImageOps.grayscale(image)
		gray_img.save(name+"_converted_gray.jpg", "JPEG")
		
	#Switch Statement	
	choice=input("Enter the choice:\n1. Create text\n2. Create Image\n3. Create Grayscale\n: ")

	options = {1:make_text,2:norm,3:gray,}
	options[choice]()

	
def test_if_image():

	if imghdr.what(imagefilename) != None :
		print ("This is a image file.")
		create_ascii_image()
	else: 
		print ("This is probably not a image.")
		exit()

test_if_image()
