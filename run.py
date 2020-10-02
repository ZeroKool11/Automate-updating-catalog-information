#! /usr/bin/env python3

import os
import requests
import locale
import json

url = "http://35.202.181.107/fruits"
source_img = "supplier-data/images"
source_desc = "supplier-data/descriptions"

for file in os.listdir(source_desc):
	dic = {}
	name, ext = os.path.splitext(file)
	if ext == ".txt":
		with open(source_desc + "/" + file) as fo:
			
			# Save in a dictionary structure the content of the file	
			dic["name"] = fo.readline().strip()
			dic["weight"] = fo.readline().strip().strip(" lbs")
			dic["description"] = fo.readline().strip()
			dic["image_name"] = file

			# Transform the dictionary structure to a json structure
			json_struc = json.dumps(dic)
			break

print(json_struc)
	
			
