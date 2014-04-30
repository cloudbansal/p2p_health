import socket

peer_client_ip = socket.gethostbyname(socket.getfqdn())
#peer_client_ip = "127.0.0.1"
super_server_ip = socket.gethostbyname(socket.getfqdn())
#super_server_ip = "127.0.0.1"
peer_server_ip = socket.gethostbyname(socket.getfqdn())
#peer_server_ip = "127.0.0.1"
super_client_ip = socket.gethostbyname(socket.getfqdn())
#super_client_ip = "127.0.0.1"

debug = True  #Print all activity on screen
peer_server_port = 2220  #Receiveing port for statistics data
super_request_port = 2221 #Receiving port for Super peer list
peer_request_port =  2222 #Receiving port for peer list
super_server_port = 2223  #Super peer Server port

super_peer_enable = "conf/.super" #Enable Super peer function
peer_enable = "conf/.peer" #Enable peer function for Super peer

peer_file = "conf/peers.conf" #List of peers
super_peer_file = "conf/super_peers.conf" #List of Super peers

log_file = "logs/peers.log"  #Log file for system statistics
max_log_size = 3*1024*1024 #3MB #Maximum log file size

client_interval = 1 #Time interval for the client to send stats to other peers 
super_client_interval = 2000 #Time interval for Super Peer to update peers and super peer lists
peer_client_interval = 1000 #Time interval for client to update  peers and super peer lists

get_peer = "get_peer" #Get list of peers
get_super_peer = "get_super_peer" #Get list of Super peers
add_peer = "add_peer" #Add peer to Super peer
add_super_peer = "add_super_peer" #Add Super peer to Super peer
remove_peer = "remove_peer" #Remove peer from super peer
remove_super_peer = "remove_super_peer" #Remove Super peer from Super peer
