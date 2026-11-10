import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hello, World!") #the B means that the message is sent in 8-bit units
    data = s.recv(1024)

print(f"Received {data}")