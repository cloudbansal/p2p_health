#!/usr/bin/python
#Client side code

from p2p.client import client
from p2p.super_client import super_client
from p2p.server import server
from p2p.super_server import super_server
from threading import Thread
import time
import signal
import os

client_interval = 10
super_client_interval = 3
super_file = "conf/.super"

def signal_handler(signal, frame):
	print(" ")
	print("wait for some time as system is shutting down...")
	client_thread.keepRunning = False
	super_server_thread.keepRunning = False
	super_client_thread.keepRunning = False
	server_thread.keepRunning = False

if __name__ == "__main__":
    print("Server Health Monitorig System")
    print("02220 - Distributed Systems")
    print("s135552 - Andrew Habib s135551 - Dheeraj Kumar Bansal")
    if os.path.isfile(super_file):
        print("This is a super peer")
    else
        print("This is a normal peer")
    client_thread = client(client_interval)
    super_client_thread = super_client(super_client_interval)
        
    server_thread = server()
    super_server_thread = super_server()
        
    super_client_thread.start()
    client_thread.start()
    
    super_server_thread.start()
    server_thread.start()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
