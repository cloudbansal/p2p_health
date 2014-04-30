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
import sys
from conf.params import *

def signal_handler(signal, frame):
	
    print(" ")
    print("Wait for some time as system is shutting down...")

    
    if os.path.isfile(super_peer_enable):
        super_client_thread.keepRunning = False
        super_server_thread.keepRunning = False
        
        if os.path.isfile(peer_enable):
            server_thread.keepRunning = False
            client_thread.keepRunning = False
    else:
        peer_client_thread.keepRunning = False
        server_thread.keepRunning = False
        client_thread.keepRunning = False
    
    time.sleep(10)
    sys.exit(0)

if __name__ == "__main__":
    
    print("------------------------------")
    print("Server Health Monitorig System")
    print("02220 - Distributed Systems")
    print("Project By:")
    print("s135552 - Andrew Habib")
    print("s135551 - Dheeraj Kumar Bansal")
    print("------------------------------")
    if os.path.isfile(super_peer_enable):
        print("Running as a Super Peer")
        if os.path.isfile(peer_enable):
            print("Also Running as a Normal Peer")
    else:
        print("Running as a Normal Peer")
    
    

    if os.path.isfile(super_peer_enable):
        super_server_thread = super_server()
        super_server_thread.start()
        super_client_thread = super_client(super_client_interval)
        super_client_thread.start()
        if os.path.isfile(peer_enable):
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
    
    while True:
        time.sleep(1)

    #signal.pause()
