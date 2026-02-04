import socket

PASSWORD = "cnlab"

alphabet = "abcdefghijklmnopqrstuvwxyz"
key =      "mnbvcxzlkjhgfdsapoiuytrewq"

encrypt_map = dict(zip(alphabet, key))
decrypt_map = dict(zip(key, alphabet))

def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            result += encrypt_map[ch]
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += decrypt_map[ch]
        else:
            result += ch
    return result

server = socket.socket()
server.bind(("localhost", 12349))
server.listen(1)

conn, addr = server.accept()

password = conn.recv(1024).decode()
if password != PASSWORD:
    conn.send("AUTH FAILED".encode())
    conn.close()
else:
    conn.send("AUTH SUCCESS".encode())

    message = conn.recv(1024).decode()
    encrypted = encrypt(message)

    file = open("mono_data.txt", "w")
    file.write(encrypted)
    file.close()

    conn.send("Message stored".encode())

    request = conn.recv(1024).decode()
    if request == "GET":
        file = open("mono_data.txt", "r")
        enc = file.read()
        file.close()
        decrypted = decrypt(enc)
        conn.send(decrypted.encode())

conn.close()
server.close()

