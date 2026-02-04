import socket

c = socket.socket()
c.connect(("localhost", 12346))

window = 5
base = 0

while base < 20:
    for i in range(base, min(base + window, 20)):
        c.send(str(i).encode())

    ack = int(c.recv(1024).decode())
    if ack >= base:
        base = ack + 1

c.close()