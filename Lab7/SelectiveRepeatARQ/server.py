import socket

s = socket.socket()
s.bind(("localhost", 12347))
s.listen(1)

print("Server waiting for client...")
conn, addr = s.accept()
print("Client connected")

received = [False] * 20
base = 0
window = 5

while base < 20:
    frame = int(conn.recv(1024).decode())
    print("Frame arrived:", frame)

    if base <= frame < base + window:
        if not received[frame]:
            received[frame] = True
            print("Accepted frame:", frame)
        else:
            print("Duplicate frame:", frame)

        conn.send(str(frame).encode())
        print("ACK sent for frame:", frame)
    else:
        print("Frame outside window:", frame)

    while base < 20 and received[base]:
        base += 1

print("All frames received")
conn.close()
s.close()

