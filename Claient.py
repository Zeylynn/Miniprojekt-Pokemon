import socket

s = socket.socket()
ip = str(input("IP-Adresse eingeben:"))
s.connect((ip, 12345))
s.send("Something".encode())
x = s.recv(30)
print(x.decode())
s.close()