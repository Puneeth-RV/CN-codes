import socket

s = socket.socket()
s.bind(("localhost", 12346))
s.listen(1)

conn, addr = s.accept()
expected = 0

while expected < 20:
    frame = int(conn.recv(1024).decode())
    if frame == expected:
        print("Received:", frame)
        expected += 1
    conn.send(str(expected - 1).encode())

conn.close()
s.close()

