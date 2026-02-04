import socket

c = socket.socket()
c.connect(("localhost", 12345))

seq = 0
count = 0

while count < 20:
    c.send(str(seq).encode())
    ack = int(c.recv(1024).decode())

    if ack == seq:
        seq = 1 - seq  
        count += 1

c.close()


