#!/usr/bin/python
#Client side code

from p2p.client import client
from p2p.super_client import super_client
from p2p.server import server
from p2p.super_server import super_server
from p2p.peer_client import peer_client
from threading import Thread
import time
import signal
import os

client_interval = 10
super_client_interval = 30
peer_client_interval = 30
super_file = "conf/.super"
peer_file = "conf/.peer"

def signal_handler(signal, frame):
	
    print(" ")
    print("Wait for some time as system is shutting down...")

    
    if os.path.isfile(super_file):
        super_client_thread.keepRunning = False
        super_server_thread.keepRunning = False
        
        if os.path.isfile(peer_file):
            server_thread.keepRunning = False
            client_thread.keepRunning = False
    else:
        peer_client_thread.keepRunning = False
        server_thread.keepRunning = False
        client_thread.keepRunning = False
    
if __name__ == "__main__":
    
    print("Server Health Monitorig System")
    print("02220 - Distributed Systems")
    print("s135552 - Andrew Habib s135551 - Dheeraj Kumar Bansal")
    
    if os.path.isfile(super_file):
        print("This is a super peer")
        if os.path.isfile(peer_file):
            print("This is a also a normal peer")
    else:
        print("This is a normal peer")
    
    

    if os.path.isfile(super_file):
        super_server_thread = super_server()
        super_server_thread.start()
        super_client_thread = super_client(super_client_interval)
        super_client_thread.start()
        if os.path.isfile(peer_file):
            client_thread = client(client_interval)
            server_thread = server()
            server_thread.start()
            client_thread.start()
    else:
        peer_client_thread = peer_client(peer_client_interval)
        peer_client_thread.start()
        client_thread = client(client_interval)
        server_thread = server()
        server_thread.start()
        client_thread.start()
        
    
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
