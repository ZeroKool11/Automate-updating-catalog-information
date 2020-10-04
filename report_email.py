#!/usr/bin/env python3

import os
import datetime
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
				str_to_repo = str_to_repo + fo.readline()
				#str_to_repo = str_to_repo + "<br/>"

	return str_to_repo


def report(string_to_repo):
	reports.generate("processed.pdf","Report",string_to_repo)





def main():
	locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
	string_to_repo = string_to_report()
	report(string_to_repo)
	print(string_to_repo)




if __name__ == "__main__":
	main()

