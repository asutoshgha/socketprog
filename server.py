import socket

HEADERSIZE=2
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket,address=s.accept()
    print(f"connect from {address} has been established")

    msg="welcome to the server!"
    msg=f"{len(msg):<{HEADERSIZE}}"+msg 
    print(msg)
    clientsocket.send(bytes(msg,"utf-8")) 
    clientsocket.close()