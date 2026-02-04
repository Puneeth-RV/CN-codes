import socket
import time

c = socket.socket()
c.connect(("localhost", 12347))

sent = [False] * 20
base = 0
window = 5

while base < 20:
    for i in range(base, min(base + window, 20)):
        if not sent[i]:
            print("Sending frame:", i)
            c.send(str(i).encode())
            sent[i] = True
            time.sleep(0.3)   # delay added for visibility

    ack = int(c.recv(1024).decode())
    print("ACK received for frame:", ack)
    base = ack + 1

print("All frames sent")
c.close()

