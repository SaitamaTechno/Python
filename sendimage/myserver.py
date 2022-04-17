import socket
import threading
import time

HOST = socket.gethostbyname(socket.gethostname())   # Symbolic name meaning all available interfaces
PORT = 50000              # Arbitrary non-privileged port
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn1, addr1 = s.accept()
print(addr1)

b=20000            #kb
a=b*1000

data1 = conn1.recv(a)#1024

f=open("savedimage.jpg", "wb")
f.write(data1)
f.close()
