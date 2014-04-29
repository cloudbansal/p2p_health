#!/usr/bin/python
#Super Peer Server code

import socket
import re
#import sys
from threading import Thread

peer_file = "conf/peers.conf"
super_peer_file = "conf/super_peers.conf"
#super_server_ip = socket.gethostbyname(socket.getfqdn())
super_server_ip = "127.0.0.1"
super_server_port = 2223
peer = "peers"
super_peer = "super_peers"
add_peer = "add_peer"
add_super_peer = "add_super_peer"
remove_peer = "remove_peer"
remove_super_peer = "remove_super_peer"

class super_server(Thread):
    def __init__(self):
   
        super(super_server, self).__init__()
        self.keepRunning = True
    
    def receive_data(self):
    
        UDP_IP = super_server_ip
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
                    print("Super Server got peers")
                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)

                    f.close()
                    peers = list(set(peers))
                    data = ';'.join(peers)
                    super_server_sock.sendto(data.encode(), addr)
                    print("Super Server sent Peers " + data + " to " + str(addr))
                
                elif recv_data == super_peer:
                    print("Super Server got Super peers")
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    super_peers = list(set(super_peers))
                    data = ';'.join(super_peers)
                    super_server_sock.sendto(data.encode(), addr)
                    print("Super Server sent Super Peers " + data + " to " + str(addr))
                
                elif recv_data == add_peer:
                    print("Super Server got Add Peer")
                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    peer_ip = str(addr[0])
                    if peer_ip not in peers:
                        peers.append(peer_ip)
                        peers = list(set(peers))
                        with open(peer_file,"a") as f:
                            for peer_ip in peers:
                                re.sub(r'\W+','',peer_ip)
                                if peer_ip.strip():
                                    print >> f,peer_ip
                        f.close()
                        with open(peer_file,"r") as f:
                            peers = list(line for line in (l.strip() for l in f) if line)
                        f.close()
                        peers = list(set(peers))
                        with open(peer_file,"w") as f:
                            for peer_ip in peers:
                                print >> f,peer_ip
                        f.close()
                        print ("Super Peer added peer " + str(addr[0]))

                elif recv_data == add_super_peer:
                    print("Super Server got Add Super Peer")
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    super_peer_ip = str(addr[0])
                    if super_peer_ip not in super_peers:
                        super_peers.append(super_peer_ip)
                        super_peers = list(set(super_peers))
                        
                        with open(super_peer_file,"a") as f:
                            for super_peer_ip in super_peers:
                                re.sub(r'\W+','',super_peer_ip)
                                if super_peer_ip.strip():
                                    print >> f,super_peer_ip
                        f.close()
                        with open(super_peer_file,"r") as f:
                            super_peers = list(line for line in (l.strip() for l in f) if line)
                        f.close()
                        super_peers = list(set(super_peers))
                        with open(super_peer_file,"w") as f:
                            for super_peer_ip in super_peers:
                                print >> f,super_peer_ip
                        f.close()
                        print ("Super Peer added Super Peer " + str(addr[0]))

                elif recv_data == remove_peer:
                    print("Super Server got Remove Peer")
                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    peer_ip = str(addr[0])
                    while peer_ip in peers: 
                        peers.remove(peer_ip) 
                    peers = list(set(peers))
                    with open(peer_file,"w") as f:
                            for peer_ip in peers:
                                print >> f,peer_ip
                    f.close()
                    print ("Super Peer removed peer " + str(addr[0]))       
                
                elif recv_data == remove_super_peer:
                    print("Super Server got Remove Super Peer")
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    super_peer_ip = str(addr[0])
                    while super_peer_ip in super_peers: 
                        super_peers.remove(super_peer_ip) 
                    super_peers = list(set(super_peers))
                    with open(super_peer_file,"w") as f:
                            for super_peer_ip in super_peers:
                                print >> f,super_peer_ip
                    f.close()
                    print ("Super Peer removed Super peer " + str(addr[0]))

            except:
                pass
                #e = sys.exc_info()[0]
                #print(str(e) + "in super_server.py in receive_data")
        super_server_sock.close()
     
    def run(self):
        self.receive_data()