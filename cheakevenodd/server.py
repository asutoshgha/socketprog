import socket

Header=200  
FORMAT='utf-8'
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MESSAGE="d"
def cheakevenodd(num):
    return num%2 == 0
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
                break
            print(f"[{addr}] {msg}")
           # a=f"{len(msg):<{Header}}"
            msg=int(msg)
            if(cheakevenodd(msg)):
                b="yes"
            else:
                b="no"
            
            a=f"{len(b):<{Header}}"
            conn.send(a.encode(FORMAT)+b.encode(FORMAT))
            #conn.send(b.encode(FORMAT)+msg1.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"server listening on {SERVER}")
    conn,addr=server.accept()
    recieve(conn,addr)

start()
