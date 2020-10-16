import socket
import threading 
Header=64
FORMAT='utf-8'
PORT=5050
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleclient(conn,addr):
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
    conn.close()
    
def start():
    server.listen()
    print(f"server listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handleclient,args=(conn,addr))
        thread.start()
        print(f"[Active connections {threading.activeCount()-1}")
    

print("starting the server ......")
start()

