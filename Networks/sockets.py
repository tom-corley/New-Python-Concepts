#Network Programming

# A socket is the endpoint of a communication channel
# sockets can be used for the internet or for local network
# python we have lower levels of networking
# TCP vs UTP
# higher levels include HTTP (internet)

import socket
# 1) internet or unix socket
# 2) what protocol will we use
# - TCP connection oriented, good for sending data, - UTP risk of losing data, but faster
# 3) which IP will we use
# 4) which port will we use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # choose protocol
s.bind(('127.0.0.1', 55555)) # pass tuple of ip (host) and port this is the host
s.listen()

while True:
    client, address = s.accept() # client and address
    print(f"Connected to {address}")
    client.send("You are connected".encode()) # sends message to client encoded to utf-8
    client.close()
