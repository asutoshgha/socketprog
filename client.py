import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
fullmsg=""
while True:
    msg=s.recv(8)
    if len(msg)<=0:
        break
    fullmsg+=msg.decode("utf-8")

print(fullmsg)
    