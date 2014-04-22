#!/usr/bin/python
#Client side code
from p2p.client import client
from p2p.server import server
from threading import Thread
import time
import signal
def signal_handler(signal, frame):
        client_thread.keepRunning = False
        server_thread.keepRunning = False
if __name__ == "__main__":
        client_thread = client(1)
        server_thread = server()
        client_thread.start()
        server_thread.start()

        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    
