#!/usr/bin/python
#Super Peer Client side code
from __future__ import print_function
import socket
import time
import re
#import sys
from threading import Thread
from p2p.validate import is_valid_IP
from conf.params import *

class super_client(Thread):
        
    def __init__(self,sec):
        super(super_client, self).__init__()
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
                    super_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    #super_client_sock.setblocking(0)
                    super_client_sock.settimeout(2)
                    super_client_sock.bind((super_client_ip,super_request_port))
                    super_client_sock.sendto(get_super_peer.encode(),(UDP_IP, UDP_PORT))
                    if debug:
                        print("Super Client sent get_super_peer")
                    super_peer_data, addr = super_client_sock.recvfrom(1024)
                    recv_super_peer_data = super_peer_data.decode().split(';')
                    if debug:    
                        print("Super Client got super peers as " + str(recv_super_peer_data) )
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
                                print(super_peer_ip,file=f)
                    f.close()
                    with open(super_peer_file,"r") as f:
                        super_peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    super_peers = list(set(super_peers))
                    with open(super_peer_file,"w") as f:
                        for super_peer_ip in super_peers:
                            print(super_peer_ip,file=f)

                    f.close()
                    time.sleep(2)
                except:
                    pass
                    #e = sys.exc_info()[0]
                    #print(str(e) + "in super_client.py in update_super_conf")
                
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
                    super_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    #super_client_sock.setblocking(0)
                    super_client_sock.settimeout(2)
                    super_client_sock.bind((super_client_ip,peer_request_port))
                    super_client_sock.sendto(get_peer.encode(),(UDP_IP, UDP_PORT))
                    if debug:
                        print("Super Client sent get_peer")
                    peer_data, addr = super_client_sock.recvfrom(1024)
                    recv_peer_data = peer_data.decode().split(';')

                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()

                    if debug:
                        print("Super Client got peers as " + str(recv_peer_data) )
                    for peer_ip in recv_peer_data:
                        if peer_ip not in peers:
                            peers.append(peer_ip)
                    peers = list(set(peers))
                    with open(peer_file,"a") as f:
                        for peer_ip in peers:
                            re.sub(r'\W+','',peer_ip)
                            if peer_ip.strip():
                                print(peer_ip,file=f)
                    f.close()
                    with open(peer_file,"r") as f:
                        peers = list(line for line in (l.strip() for l in f) if line)
                    f.close()
                    peers = list(set(peers))
                    with open(peer_file,"w") as f:
                        for peer_ip in peers:
                            print(peer_ip,file=f)
                    f.close()
                    #time.sleep(2)
                except:
                    pass
                    #e = sys.exc_info()[0]
                    #print(str(e) + "in super_client.py in update_peer_conf")

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
                    super_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    super_client_sock.sendto(add_super_peer.encode(),(UDP_IP, UDP_PORT))
                    if debug:
                        print("Super Peer Added itself to Super Peer " + str(IP).strip() + " as Super Peer")
                    if peer_enable:
                        super_client_sock.sendto(add_peer.encode(),(UDP_IP, UDP_PORT))
                        if debug:
                            print("Super Peer Added itself to Super Peer " + str(IP).strip() + " as peer")
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
                    super_client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    super_client_sock.sendto(remove_super_peer.encode(),(UDP_IP, UDP_PORT))
                    if debug:
                        print("Super Peer Removed itself from Super Peer " + str(IP).strip() + " as Super Peer")
                    if peer_enable:
                        super_client_sock.sendto(remove_peer.encode(),(UDP_IP, UDP_PORT))
                        if debug:
                            print("Super Peer Removed itself from Super Peer " + str(IP).strip() + " as peer")
                except:
                    pass

    def run(self):
        while self.keepRunning:
            self.add()
            self.update_super_conf()
            self.update_peer_conf()
            time.sleep(self.interval)
        self.remove()
