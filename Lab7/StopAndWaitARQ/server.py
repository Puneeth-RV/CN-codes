import socket

s = socket.socket()
s.bind(("localhost", 12345))
s.listen(1)

conn, addr = s.accept()
expected = 0
count = 0

while count < 20:
    frame = int(conn.recv(1024).decode())

    if frame == expected:
        print("Received frame:", frame)
        conn.send(str(expected).encode())
        expected = 1 - expected   
        count += 1
    else:
        conn.send(str(1 - expected).encode())

conn.close()
s.close()



