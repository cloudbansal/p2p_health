import socket

def is_valid_IP(address):
    try:
        socket.inet_aton(address)
        ip = True
    except:
        ip = False

    return ip