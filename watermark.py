#!/usr/bin/python3

#Python3 script that will add a .png file to other image's in a folder in one script.

#GitHub Link: https://github.com/MrJSec/watermark-batch-images-python3.git

#Credits:
#Anthony Lister for the idea and code: https://pybit.es/pillow-intro.html
#JC for helping me fix a looping issue. https://twitter.com/JC_SoCal

#How to use:
#pip3 install pillow
#Create a folder called "input" and add images, .jpg, .png etc..
#Create a folder called "output"
#Have a logo ready and ensure it's called "logo.png" transparent works best!
#Run script python3 watermark.py
#Enjoy?


#Imports, ensure you have pillow installed.
from PIL import Image
import glob
from random import random, seed


#Watermark, change if needed, please ensure a .png is used.
watermark = 'logo.png'


#Code block.
def create_watermark():

    main = Image.open(file)
    mark = Image.open(watermark)

    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.25
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)

    tmp_img = Image.new('RGB', main.size)

    for i in range(0, tmp_img.size[0], mark.size[0]):
        for j  in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
            main.thumbnail((8000, 8000), Image.ANTIALIAS)
    main.save('{}{}{}'.format("./output/",random(),'.png', quality=100))


#Main.
if __name__ == '__main__':
        for infile in glob.glob("./input/*"):
            with open (infile, 'rb+') as file:
                img = Image.open(file)
                create_watermark()