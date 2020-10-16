import socket

Header=64
FORMAT='utf-8'
PORT=5050
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER="192.168.56.1"
ADDR=(SERVER,PORT)
client=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    
