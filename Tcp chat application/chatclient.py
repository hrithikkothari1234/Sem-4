#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234                # Reserve a port for your service.

s.connect((host, port))
while(True):
    str=input("Enter your message")
    if not str :
        break
    s.send(str.encode())
    print("Receiving.....")
    str=s.recv(1024)
    print(str)
    if str==b"Bye":
        print("Client Breaking connection\n")
        break
s.send(b"Bye")
s.close                     # Close the socket when done
