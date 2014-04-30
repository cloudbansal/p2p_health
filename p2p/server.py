#!/usr/bin/python
#Peer Server side code
from __future__ import print_function
import socket
import os
#import sys
from datetime import datetime
from threading import Thread
from conf.params import *

class server(Thread):

	def __init__(self):

		super(server, self).__init__()
		self.keepRunning = True

	def receive_data(self):
		UDP_IP = peer_server_ip
		UDP_PORT = peer_server_port
		if debug:
			print("Server IP is " + UDP_IP)
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		server_sock.bind((UDP_IP, UDP_PORT))
		server_sock.setblocking(0)

		while self.keepRunning:
			try:
				data, addr = server_sock.recvfrom(1024)
				local_time = str(datetime.utcnow().strftime('%a %Y-%m-%d %H:%M:%S'))

				if debug:
					print("\"System time\":\"" + local_time +"\"," + data.decode())
				if not os.path.exists(os.path.dirname(log_file)):
					os.makedirs(os.path.dirname(log_file))

				if os.path.isfile(log_file) and os.stat(log_file).st_size > max_log_size:
					bak_file = "%s.bak.%s" % (log_file,local_time)
					os.rename(log_file,bak_file)

					with open(log_file,"a") as f:
						line = "\"System time\":\"%s\",%s" % (local_time,data.decode())
						print(line,file=f)
					f.close()

			except:
				pass
		server_sock.close()

	def run(self):
		self.receive_data()
