#!/usr/bin/python
#Client side code
from p2p.client import client
from p2p.server import server
from threading import Thread
import time
if __name__ == "__main__":
     client_thread = client(1)
     server_thread = server()
     client_thread.start()
     server_thread.start()
     time.sleep(10) # and let the 2 threads to their work
     client_thread.keepRunning = False
     server_thread.keepRunning = False