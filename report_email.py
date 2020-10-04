#!/usr/bin/env python3

import os
from datetime import date
import reports
import locale
import emails

source = "supplier-data/descriptions/"
username = "student-04-14d59004255b"
def string_to_report():
	str_to_repo = ""
	for file in os.listdir(source):
		name, ext = os.path.splitext(file)
		if ext == ".txt":
			with open(source + file) as fo:
				str_to_repo = str_to_repo +  "name: " + fo.readline() + "<br/>"
				str_to_repo = str_to_repo + "weight: " + fo.readline() + "<br/>"
				str_to_repo = str_to_repo + "<br/>"
	return str_to_repo

def report(string_to_repo):
	today = date.today()
	title = "Processed Update on {}".format(today)
	reports.generate("processed.pdf",title,string_to_repo)
	reports.generate("/tmp/processed.pdf",title,string_to_repo)


def email():
	sender = "automation@example.com"
	receiver = username + "@example.com"
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	Attachment = "/tmp/processed.pdf"

	message = emails.generate(sender,receiver,subject,body,Attachment)
	emails.send(message)

def main():
	locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
	string_to_repo = string_to_report()
	today = date.today()
	report(string_to_repo)
	email()
	




if __name__ == "__main__":
	main()

