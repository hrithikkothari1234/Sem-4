#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
#while True:
c, addr = s.accept()     # Establish connection with client.
print('Got connection from', addr)
while(True):
    #print("Receiving.....")
    str=c.recv(1024)
    print("Receiving.....",str)
    if str==b"Bye":
        print("Server Breaking connection\n")
        break
    str=input("enter ur message")
    if not str :
        break
    c.send(str.encode())
    #print("Received from client.....")
    #print("Receiving from client....",c.recv(1024))
c.send(b"Bye")
c.close()                # Close the connection
