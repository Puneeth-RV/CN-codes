import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    conn.send(data.encode())

conn.close()
server_socket.close()
