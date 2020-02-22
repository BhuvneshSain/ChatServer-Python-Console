#!/usr/bin/python
import socket
serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
serv.bind((host,port))
serv.listen(5)
clientsocket,addr=serv.accept()
print('Connected successfully from %s'%str(addr))
while True:
    msg=clientsocket.recv(1024)
    print(msg.decode('ascii'))
    ss=input("Server->")
    clientsocket.send(ss.encode('ascii'))   
clientsocket.close()
