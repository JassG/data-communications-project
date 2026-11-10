#needed to use sockets.
import socket

#Server setting up a listening socket.

HOST = "127.0.0.1" #this is so it only connects to this device. if the quotes are empty, it can connect to any computer.

PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #binds the socket to the host and port you want to listen to.
    s.listen() #this listens to a request to the server, from this specific socket.
    conn, addr = s.accept()

    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)