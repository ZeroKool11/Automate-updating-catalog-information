#! /usr/bin/env python3

import os
import requests
import locale
import json

url = "http://35.202.181.107/fruits/"
source_img = "supplier-data/images/"
source_desc = "supplier-data/descriptions/"
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

for file in os.listdir(source_desc):
	dic = {}
	name, ext = os.path.splitext(file)
	if ext == ".txt":
		with open(source_desc + file) as fo:
			
			# Save in a dictionary structure the content of the file	
			dic["name"] = fo.readline().strip()
			dic["weight"] = fo.readline().strip().strip(" lbs")
			dic["description"] = fo.readline().strip()
			dic["image_name"] = name + ".jpeg"

			# Upload the data
			r = requests.post(url, json = dic)
			r.raise_for_status()
print(r.status_code)	

	
			
