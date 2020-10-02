#!/usr/bin/env python3

import os
from PIL import Image

source = "supplier-data/images"
dest = "supplier-data/images"

for file in os.listdir(source):
	name, ext = os.path.splitext(file)
	if ext == ".tiff":
		im = Image.open(source + "/" + file)
		new_image = im.convert("RGB").resize((600,400)).save(dest + "/" + name + ".JPEG")
