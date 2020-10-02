#! /usr/bin/env python3

import os
import requests

url = "http://35.202.181.107/fruits"
source_img = "supplier-data/images"
source_desc = "supplier-data/descriptions"

for file in os.listdir(source_desc):
	name, ext = os.path.splitext(file)
	if ext == ".txt":
		print(file)
