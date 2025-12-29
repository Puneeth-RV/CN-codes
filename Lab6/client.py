import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

message = input("Enter message: ")
client_socket.send(message.encode())

echo = client_socket.recv(1024).decode()
print("Echo from server:", echo)

client_socket.close()
