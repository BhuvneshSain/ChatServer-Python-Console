#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.connect((host,port))
while True:
    z=input('Client->')
    s.send(z.encode('ascii'))
    msg=s.recv(1024)
    print(msg.decode('ascii'))
s.close()
