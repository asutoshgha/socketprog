import socket

Header=64
FORMAT='utf-8'
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MESSAGE="#"

def recieve(conn,addr):
    print(f"[new connection] whose addr={addr}")
    connected=True
    while connected:
        msg_length=conn.recv(Header).decode(FORMAT)
        if msg_length: 
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")
            msg1=input(f"Enter message to send {addr}")
            a=f"{len(msg1):<{Header}}"
            conn.send(a.encode(FORMAT)+msg1.encode(FORMAT))
        else:
            msg1=input(f"Enter message to send {addr}")
            a=f"{len(msg1):<{Header}}"
            conn.send(a.encode(FORMAT)+msg1.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"server listening on {SERVER}")
    conn,addr=server.accept()
    recieve(conn,addr)

start()