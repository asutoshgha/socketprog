import socket
Header=64
FORMAT='utf-8'
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
while True:
    a=input("enter a string to be capitalized:")
    k=a
    ha=f"{len(a):<{Header}}".encode(FORMAT)
    a=ha+a.encode(FORMAT)
    client.send(a)
    if k == "#":
        print("disconnected..")
        break
    msg_length=client.recv(Header).decode(FORMAT)
    if msg_length: 
        msg_length=int(msg_length)
        msg=client.recv(msg_length).decode(FORMAT)
        print(msg)