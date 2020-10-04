#!/usr/bin/env python3

import os
from datetime import date
import reports
import locale

source = "supplier-data/descriptions/"

def string_to_report():
	str_to_repo = ""
	for file in os.listdir(source):
		name, ext = os.path.splitext(file)
		if ext == ".txt":
			with open(source + file) as fo:
				str_to_repo = str_to_repo + fo.readline() + "<br/>"
				str_to_repo = str_to_repo + fo.readline() + "<br/>"
				str_to_repo = str_to_repo + "<br/>"
	return str_to_repo

def report(string_to_repo):
	today = date.today()
	title = "Processed Update on {}".format(today)
	reports.generate("processed.pdf",title,string_to_repo)
	reports.generate("/tmp/processed.pdf",title,string_to_repo)

def main():
	locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
	string_to_repo = string_to_report()
	today = date.today()
	report(string_to_repo)
	




if __name__ == "__main__":
	main()

