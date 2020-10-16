import socket
import pickle
HEADERSIZE=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:

    fullmsg=b''
    newmsg=True

    while True:
        msg=s.recv(16)
        if newmsg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen=int(msg[:HEADERSIZE])
            print("!!")
            print(msglen)
            print("!!")
            newmsg=False
        fullmsg+=msg

        if len(fullmsg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(pickle.loads(fullmsg[HEADERSIZE:]))
            new_msg=True
            fullmsg=b''
    print(fullmsg)
    