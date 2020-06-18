#/usr/bin/python3
# https://medium.com/@ajeetham/image-type-conversion-jpg-png-jpg-webp-png-webp-with-python-7d5df09394c9

import os
from PIL import Image


path = "./"

file_list = os.listdir(path)
file_list_png = [file for file in file_list if file.endswith(".png")]


for a in file_list_png:
    print(a)	
    b = a[0:13] + ".jpg"
    print(b)
    im = Image.open(a).convert("RGB")
    im.save(b,"jpeg")
