import socket

client = socket.socket()
client.connect(("localhost", 12348))

password = input("Enter password: ")
client.send(password.encode())

response = client.recv(1024).decode()
print(response)

if response == "AUTH SUCCESS":
    message = input("Enter message: ")
    client.send(message.encode())

    print(client.recv(1024).decode())

    client.send("GET".encode())
    decrypted = client.recv(1024).decode()
    print("Decrypted message:", decrypted)

client.close()


