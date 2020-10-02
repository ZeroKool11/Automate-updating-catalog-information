#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
source = "supplier-data/images"

for file in os.listdir(source):
	name, ext = os.path.splitext(file)
	if ext == ".jpeg":
		with open(source + '/' + file , 'rb') as opened:
    			r = requests.post(url, files={'file': opened})
