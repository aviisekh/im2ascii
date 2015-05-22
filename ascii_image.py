#!/usr/bin/env python

#import cv2
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




#sys.dont_write_bytecode = True
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

	def make_text():
		im = Image.open(imagefilename)
		image_width, image_height = im.size
		print os.path.splitext(imagefilename)

	
		#aalib_screen_width= int(image_width/24.9)*img_new_magnitude
		#aalib_screen_height= int(image_height/41.39)*img_new_magnitude
	
		aalib_screen_width= 80#image_width
		aalib_screen_height= 40#image_height

		screen = aalib.AsciiScreen(width=aalib_screen_width, height=aalib_screen_height )


		im= Image.open(imagefilename).convert("L").resize(screen.virtual_size)
		print im.size
	
		screen.put_image((0,0), im)
		p=open("new.txt","w")
		q=screen.render()
		#print q
		p.write(q)

	def make_img():
		print "Make Image"
	
	def make_gray():
		print "Make gray"

			
	choice=input("Enter the choice:\n1. Create text\n2. Create Image\n3. Create Grayscale\n: ")

	options = {1:make_text,2:make_img,3:make_gray,}
	options[choice]()

	'''
	im = Image.open(imagefilename)
	image_width, image_height = im.size

	
	#aalib_screen_width= int(image_width/24.9)*img_new_magnitude
	#aalib_screen_height= int(image_height/41.39)*img_new_magnitude
	
	aalib_screen_width= 80#image_width
	aalib_screen_height= 40#image_height

	screen = aalib.AsciiScreen(width=aalib_screen_width, height=aalib_screen_height )


	im= Image.open(imagefilename).convert("L").resize(screen.virtual_size)
	print im.size
	
	screen.put_image((0,0), im)
	p=open("new.txt","w")
	q=screen.render()
	#print q
	p.write(q)
	'''
	
	'''	
	y = 0
	
	how_many_rows = len ( screen.render().splitlines() ) 

	new_img_width, font_size = font.getsize (screen.render().splitlines()[0])
	

	img=Image.new('RGB', (new_img_width, how_many_rows*font_size),(120,20,20))
	draw = ImageDraw.Draw(img)
	
	for lines in screen.render().splitlines():
		draw.text( (0,y), lines, (255,255,0),font=font )
		y = y + font_size
		

	imagefit = ImageOps.fit(img, (image_width, image_height), Image.ANTIALIAS)

	grey_img=ImageOps.grayscale(imagefit)
	
	#imagefit.save("ascii_photo.png", "PNG")
	grey_img.save("ascii_photo.png", "PNG")
	img_new = cv2.imread('ascii_photo.png',0)
	a,thresh=cv2.threshold(img_new, 127,255,cv2.THRESH_BINARY) 
	cv2.imwrite('messigray.png',thresh)
	#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	'''


def test_if_image():

	if imghdr.what(imagefilename) != None :
		print ("This is a image file.")
		create_ascii_image()
	else: 
		print ("This is probably not a image.")
		exit()


test_if_image()
