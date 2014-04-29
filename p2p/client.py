#!/usr/bin/python
#Peer Client side code

import psutil
import time
#import sys
import socket
from datetime import datetime
from threading import Thread
from p2p.validate import is_valid_IP

peer_file = "conf/peers.conf"
peer_server_port = 2220

class client(Thread):
        
        def __init__(self,sec):
            
                super(client, self).__init__()
                self.interval = sec;
                self.keepRunning = True

        def get_usage(self):
            
                a = str(datetime.utcnow().strftime('%a %Y-%m-%d %H:%M:%S'))
                b = str(psutil.cpu_percent(interval=0))
                c = str(psutil.virtual_memory().percent)
                d = str(psutil.disk_usage('/').percent)
                e = str(socket.gethostbyname(socket.gethostname()))
            
                return str("\"IP\":\"" + e + "\",\"Remote System time\":\"" + a +"\",\"CPU USAGE\":\"" + b + "%\",\"MEMORY USAGE\":\"" + c + "%\",\"DISK USAGE\":\"" + d + "%\"")
       
        def send_stats(self,n):
            
            while self.keepRunning:
                with open(peer_file,"r") as f:
                    content = f.readlines()
                f.close()
                
                try:
                        for IP in content:
                            if IP.strip() and is_valid_IP(IP):
                                UDP_IP = IP
                                UDP_PORT = peer_server_port
                                STATS = self.get_usage().encode()
                                client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                                print ("Sending to " + UDP_IP)
                                client_sock.sendto(STATS, (UDP_IP, UDP_PORT))
                                time.sleep(0.5)
                        time.sleep(n)  
                except:
                    pass
                    #e = sys.exc_info()[0]
                    #print(str(e) + "in client.py in send_stats")

        
        def run(self):
                self.send_stats(self.interval)
