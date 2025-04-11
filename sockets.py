#SERVER

import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = ''  # unspecified ip - all interfaces on host
port = 12345  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port
s.listen(1)  # Now wait for client connection.
connection, client_address = s.accept()  # Establish / get one connection with client.

byte_data = connection.recv(30)     # read maximum of 30 bytes from connection
data = byte_data.decode()   # convert byte data to string
print(f"received {data}")
connection.sendall("got-it".encode()) # send reply to connection
connection.close()      # clean up the connection
s.close()               # clean up listenng socket