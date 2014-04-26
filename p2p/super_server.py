#!/usr/bin/python
#Super Peer Server code

import socket
#import sys
from threading import Thread

peer_file = "conf/peers.conf"
super_peer_file = "conf/super_peers.conf"
super_server_port = 2222
peer = "peers"
super_peer = "super_peers"

class super_server(Thread):
    def __init__(self):
   
        super(super_server, self).__init__()
        self.keepRunning = True
    
    def receive_data(self):
    
        UDP_IP = socket.gethostbyname(socket.getfqdn())
        UDP_PORT = super_server_port
        #print("Super Server IP is " + UDP_IP)
        super_server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        super_server_sock.bind((UDP_IP, UDP_PORT))
        #super_server_sock.settimeout(10)
        super_server_sock.setblocking(0)

        while self.keepRunning:
            
            try:
                data, addr = super_server_sock.recvfrom(1024)
                recv_data = data.decode()
            
                if recv_data == peer:
                    #print("Super Server got peers")
                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)

                    f.close()
                    peers = list(set(peers))
                    data = ';'.join(peers)
                    super_server_sock.sendto(data.encode(), addr)
                    #print("Super Server sent " + data + "to" + str(addr))
                elif recv_data == super_peer:
                    #print("Super Server got Super peers")
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    super_peers = list(set(super_peers))
                    data = ';'.join(super_peers)
                    
                    super_server_sock.sendto(data.encode(), addr)
                    #print("Super Server sent " + data + "to" + str(addr))
            except:
                pass
                #e = sys.exc_info()[0]
                #print(str(e) + "in super_server.py in receive_data")

        super_server_sock.close()
     
    def run(self):
        self.receive_data()
