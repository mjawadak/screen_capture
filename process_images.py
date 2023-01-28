'''
Code to convert images from PNG to JPG format in python
'''
from PIL import Image
import os
import time

base_url = '/media/jawad-drive/sky_stream02/'
processed_url = '/media/jawad-drive/sky_stream02_processed/'

while(1):
    image_names = os.listdir(base_url)
    image_names.sort()

    for i in image_names:
        file_url = base_url+i
        im = Image.open(file_url)
        new_filename = i.split(".png")[0]+".jpg"
        im.save(processed_url+new_filename)
        os.remove(file_url)

    time.sleep(900)
