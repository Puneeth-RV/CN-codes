import socket

PASSWORD = "cnlab"

def encrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch == 'z':
                result += 'a'
            elif ch == 'Z':
                result += 'A'
            else:
                result += chr(ord(ch) + 1)
        elif ch.isdigit():
            if ch == '9':
                result += '0'
            else:
                result += chr(ord(ch) + 1)
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch == 'a':
                result += 'z'
            elif ch == 'A':
                result += 'Z'
            else:
                result += chr(ord(ch) - 1)
        elif ch.isdigit():
            if ch == '0':
                result += '9'
            else:
                result += chr(ord(ch) - 1)
        else:
            result += ch
    return result

server = socket.socket()
server.bind(("localhost", 12348))
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

    file = open("data.txt", "w")
    file.write(encrypted)
    file.close()

    conn.send("Message stored".encode())

    request = conn.recv(1024).decode()
    if request == "GET":
        file = open("data.txt", "r")
        enc = file.read()
        file.close()

        decrypted = decrypt(enc)
        conn.send(decrypted.encode())

conn.close()
server.close()

