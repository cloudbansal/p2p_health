#!/usr/bin/python
#Client side code
import psutil
import time
import socket
from datetime import datetime
from threading import Thread

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
                return str("\"IP\":\"" + e + "\",\"System time\":\"" + a +"\",\"CPU USAGE\":\"" + b + "%\",\"MEMORY USAGE\":\"" + c + "%\",\"DISK USAGE\":\"" + d + "%\"")
       
        def send_stats(self,n):
            while self.keepRunning:
                try:
                        UDP_IP = socket.gethostbyname(socket.getfqdn())
                        UDP_PORT = 5005
                        STATS = self.get_usage().encode()
                        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                        sock.sendto(STATS, (UDP_IP, UDP_PORT))
                        time.sleep(n)
                except:
                        pass

            print("Client Killed")
        
        def run(self):
                self.send_stats(self.interval)