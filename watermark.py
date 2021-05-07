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

import os
from PIL import Image

try:
    PATH = "./input/"
    Copy_to_path="./output/"
    list = os.listdir(PATH)
    number_files = len(list)
    watermark ='logo.png'
    for filename in os.listdir(PATH):
        main = Image.open(os.path.join(PATH, filename))
    mark = Image.open(watermark)
    print (number_files, " Pictures where added to the list from: "+PATH+"")

    mask = mark.convert('L').point(lambda x: min (x, 25))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.25
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)

    tmp_img = Image.new('RGB', main.size)

    for i in range (0, tmp_img.size[0], mark.size[0]):
        for j in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
            main.thumbnail((8000, 8000), Image.ANTIALIAS)
        main.save(Copy_to_path+filename+'.png', quality=100)
    print ("Adding watermark to: "+filename+" was successful [+]")
    print ("[+] All ",number_files," Pictures were successful [+]\n and saved here: "+Copy_to_path)

except FileNotFoundError:
    print ("FileNotFoundError: Please ensure the watermark is correct,and the folders are correct!")
except:
    print("Something, something bad has happen here, and this error has happen.")
