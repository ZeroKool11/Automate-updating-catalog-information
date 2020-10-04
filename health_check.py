#!/usr/bin/env python3

import psutil
import socket 
import time
import emails

def email(subject):
	sender = "automation@example.com"
	receiver = "student-04-14d59004255b@example.com"
	body = "Please check your system and resolve the issue as soon as possible."
	message = emails.generate(sender,receiver,subuject,body," ")
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
		if disk_p < 20:
			subject = "Error - Available disk space is less than 20%"
		if mem_av < 500:
			subject = "Error - Available memory is less than 500MB"
		if socket.gethostbyname("localhost") != "127.0.0.1":
			subject = "Error - localhost cannot be resolved to 127.0.0.1"


if __name__ == "__main__":
	main()




	#print(cpu_p)
	#print(disk_p)
	#print(mem_av)
	#print(socket.gethostbyname("localhost"))
	#time.sleep(5)
