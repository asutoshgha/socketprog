import socket
Header=200
FORMAT='utf-8'
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
while True:
    a=input("enter a num to cheak even odd:[press d to disconnect from server]")
    k=a
    ha=f"{len(a):<{Header}}".encode(FORMAT)
    a=ha+a.encode(FORMAT)
    client.send(a)
    if k == "d":
        print("disconnected..")
        break
    msg_length=client.recv(Header).decode(FORMAT)
    if msg_length: 
        msg_length=int(msg_length)
        msg=client.recv(msg_length).decode(FORMAT)
        print(msg)
        