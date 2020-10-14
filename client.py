import socket

HEADERSIZE=2
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:

    fullmsg=""
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
        fullmsg+=msg.decode("utf-8")

        if len(fullmsg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(fullmsg[HEADERSIZE:]+"13")
            new_msg=True
            fullmsg=""
    print(fullmsg)
    