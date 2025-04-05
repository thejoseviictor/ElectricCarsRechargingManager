# Nuvem Que Será Responsável por Reservar Recargas Para os Carros:

import socket
from ChargingStationsFile import ChargingStationsFile
from ReservationsFile import ReservationsFile

# Definindo o Host e Post da Nuvem:
HOST = "0.0.0.0" # Aceita Conexões de Qualquer Dispositivo na Rede.
PORT = 65432

# Definindo o Socket da Nuvem:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Conexão TCP IPv4.
server.bind((HOST, PORT)) # Definindo o IP e porta do socket.

# Inicia uma Conexão, Lê Seus Dados, Fecha a Conexão e Aguarda uma Nova Conexão:
while True:
    # Ativando o Modo de Escuta da Nuvem:
    server.listen(1) # Escutando Com uma Fila de Tamanho "1".
    print(f"\nOuvindo na Porta '{PORT}'...\n")

    # Aceitando uma Conexão:
    conn, addr = server.accept()
    print(f"\nConectado a '{addr}'\n")

    # Mantendo no Loop Enquanto Dados do Dispositivo São Recebidos:
    while True:
        data = conn.recv(1024) # Dados de até 1024 bytes.
        if not data:
            break
        print(f"\nReceived: {data.decode()}\n")
        conn.sendall(b"Data Received Successfully") # Enviando confirmação ao cliente.

    # Fechando a Conexão com o Dispositivo:
    conn.close()
