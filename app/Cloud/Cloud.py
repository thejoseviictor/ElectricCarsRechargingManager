#!/usr/bin/env python3

import socket

HOST = "0.0.0.0"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP IPv4.
server.bind((HOST, PORT)) # Definindo o IP e porta do socket.
server.listen(1) # Escutando com uma fila de tamanho "1".

print(f"\nListening on Port {PORT}...\n")

conn, addr = server.accept()
print(f"\nConnected to {addr}\n")

while True:
    data = conn.recv(1024) # Dados de até 1024 bytes.
    if not data:
        break
    print(f"\nReceived: {data.decode()}\n")
    conn.sendall(b"Data Received Successfully") # Enviando confirmação ao cliente.

conn.close()
