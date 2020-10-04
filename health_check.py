#!/usr/bin/env python3

import psutil
import socket 
import time
import emails

def email(subject):
	sender = "automation@example.com"
	receiver = "student-04-14d59004255b@example.com"
	body = "Please check your system and resolve the issue as soon as possible."
	message = emails.generate_without_attach(sender,receiver,subject,body)
	emails.send(message)

def main():
	flat = True
	time_s = 60
	cpu_p = psutil.cpu_percent()
	disk_p = psutil.disk_usage("/").percent
	mem_av = psutil.virtual_memory().available / 1048576

	while flat:
		if cpu_p > 80:
			subject = "Error - CPU usage is over 80%"
			email(subject)
		if disk_p < 20:
			subject = "Error - Available disk space is less than 20%"
			email(subject)
		if mem_av < 500:
			subject = "Error - Available memory is less than 500MB"
			email(subject)
		if socket.gethostbyname("localhost") != "127.0.0.1":
			subject = "Error - localhost cannot be resolved to 127.0.0.1"
			email(subject)

		print(cpu_p)
		print(disk_p)
		print(mem_av)
		print(socket.gethostbyname("localhost"))
		time.sleep(time_s)


if __name__ == "__main__":
	main()


