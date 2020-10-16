import socket

Header=64
FORMAT='utf-8'
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MESSAGE="d"

def isPalindrome(s):
    return s == s[::-1]
 
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
            if(isPalindrome(msg)):
                ans="true"
                a=f"{len(ans):<{Header}}"
                conn.send(a.encode(FORMAT)+ans.upper().encode(FORMAT))
            else:
                ans="false"
                a=f"{len(ans):<{Header}}"
                conn.send(a.encode(FORMAT)+ans.upper().encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"server listening on {SERVER}")
    conn,addr=server.accept()
    recieve(conn,addr)

start()
    
        
