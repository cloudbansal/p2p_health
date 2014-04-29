#!/usr/bin/python
#Super Peer Client side code

import socket
import time
import re
import os
#import sys
from threading import Thread
from p2p.validate import is_valid_IP


peer_file = "conf/peers.conf"
super_peer_file = "conf/super_peers.conf"
super_request_port = 2221
peer_request_port =  2222
super_server_port = 2223
peer = "peers"
super_peer = "super_peers"
add_peer = "add_peer"
remove_peer = "remove_peer"
#peer_client_ip = socket.gethostbyname(socket.getfqdn())
peer_client_ip = "127.0.0.1"

class peer_client(Thread):
        
    def __init__(self,sec):
        super(peer_client, self).__init__()
        self.interval = sec;
        self.keepRunning = True

    def update_super_conf(self):
        with open(super_peer_file,"r") as f:
            content = f.readlines()
        f.close()

        content = list(set(content))
        for IP in content:
            if IP.strip() and is_valid_IP(IP):
                try:
                    UDP_IP = IP
                    UDP_PORT = super_server_port
                    peer_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    #peer_client_sock.setblocking(0)
                    peer_client_sock.settimeout(2)
                    peer_client_sock.bind((peer_client_ip,super_request_port))
                    peer_client_sock.sendto(super_peer.encode(),(UDP_IP, UDP_PORT))
                    print("Peer Client sent super peers")
                    
                    super_peer_data, addr = peer_client_sock.recvfrom(1024)
                    recv_super_peer_data = super_peer_data.decode().split(';')

                    print("Peer Client got super peers as " + str(recv_super_peer_data) )
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()

                    for super_peer_ip in recv_super_peer_data:
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
                    time.sleep(2)
                except:
                    pass
                    #e = sys.exc_info()[0]
                    #print(str(e) + "in peer_client.py in update_super_conf")
                
    def update_peer_conf(self):
        with open(super_peer_file,"r") as f:
            content = f.readlines()
        f.close()

        content = list(set(content))
        for IP in content:
            if IP.strip() and is_valid_IP(IP):
                try:
                    UDP_IP = IP
                    UDP_PORT = super_server_port
                    peer_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    #peer_client_sock.setblocking(0)
                    peer_client_sock.settimeout(2)
                    peer_client_sock.bind((peer_client_ip,peer_request_port))
                    print("Peer Client sent peers")
                    peer_client_sock.sendto(peer.encode(),(UDP_IP, UDP_PORT))
                    peer_data, addr = peer_client_sock.recvfrom(1024)
                    recv_peer_data = peer_data.decode().split(';')

                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()

                    print("Peer Client got peers as " + str(recv_peer_data) )
                    for peer_ip in recv_peer_data:
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
                    #time.sleep(2)
                except:
                    pass
                    #e = sys.exc_info()[0]
                    #print(str(e) + "in peer_client.py in update_peer_conf")

    def add(self):
        with open(super_peer_file,"r") as f:
            content = f.readlines()
        f.close()

        content = list(set(content))
        for IP in content:
            if IP.strip() and is_valid_IP(IP):
                try:
                    UDP_IP = IP
                    UDP_PORT = super_server_port
                    peer_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    print("Peer Client Added itself to Super Peer " + str(IP))
                    peer_client_sock.sendto(add_peer.encode(),(UDP_IP, UDP_PORT))
                except:
                    pass
        

    def remove(self):
        with open(super_peer_file,"r") as f:
            content = f.readlines()
        f.close()

        content = list(set(content))
        for IP in content:
            if IP.strip() and is_valid_IP(IP):
                try:
                    UDP_IP = IP
                    UDP_PORT = super_server_port
                    peer_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    print("Peer Client Removed itself from Super Peer " + str(IP))
                    peer_client_sock.sendto(remove_peer.encode(),(UDP_IP, UDP_PORT))
                except:
                    pass
        

    def run(self):
        while self.keepRunning:
            self.add()
            self.update_super_conf()
            time.sleep(self.interval)
            self.update_peer_conf()
            #time.sleep(120)
            #open(peer_file,"w").close()
        self.remove()