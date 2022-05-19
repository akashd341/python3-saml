import socket
import sys
# server to send data to client
x=sys.argv[1]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
clientsocket,address=s.accept()
clientsocket.send(bytes(x,"utf-8"))
