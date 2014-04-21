#!/usr/bin/python
#Server side code
import socket
from threading import Thread
class server(Thread):
	def __init__(self):
		super(server, self).__init__()
		self.keepRunning = True
	
	def receive_data(self):
		UDP_IP = socket.gethostbyname(socket.getfqdn())
		UDP_PORT = 5005

		sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.bind((UDP_IP, UDP_PORT))
		sock.setblocking(0)

		while self.keepRunning:
			try:
				data, addr = sock.recvfrom(1024)
 		   		print (data.decode())
 		   	except:
 		   		pass

 		sock.close()
 		print("Server Killed")   	
 	
 	def run(self):
 		self.receive_data()