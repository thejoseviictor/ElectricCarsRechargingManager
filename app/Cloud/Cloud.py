# Nuvem Que Será Responsável por Reservar Recargas Para os Carros:

import socket
import json
from ChargingStationsFile import ChargingStationsFile
from ReservationsFile import ReservationsFile

# Definindo o Host e Post da Nuvem:
HOST = "0.0.0.0" # Aceita Conexões de Qualquer Dispositivo na Rede.
PORT = 65432

# Garantindo Que o Json Completo Seja Recebido:
def receiveFullJson(server):
    buffer = b"" # Variável de Bytes Vazia, Onde os Dados, em Pedaços, Serão Salvos.
    # Loop de Recebimento do Json Completo:
    while True:
        chunk = server.recv(1024) # Recebendo os Dados em Partes de 1024 Bytes.
        # Finalizando, Se Não Houverem Mais Dados a Receber:
        if not chunk:
            break
        buffer += chunk # Somando os Dados no Buffer.
        # Testando Se o Json Já Está Completo:
        try:
            return json.loads(buffer.decode()) # Decodificando os Dados em Dicionário (utf-8)
        # Erro de Dados Incompletos:
        except json.JSONDecodeError:
            continue

# Definindo o Socket da Nuvem:
cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Conexão TCP IPv4.
cloud.bind((HOST, PORT)) # Definindo o IP e porta do socket.

# Inicia uma Conexão, Lê Seus Dados, Fecha a Conexão e Aguarda uma Nova Conexão:
while True:
    # Ativando o Modo de Escuta da Nuvem:
    cloud.listen(1) # Escutando Com uma Fila de Tamanho "1".
    print(f"\nOuvindo na Porta '{PORT}'...\n")

    # Aceitando uma Conexão:
    conn, addr = cloud.accept()
    print(f"\nConectado a '{addr}'\n")

    # Mantendo no Loop Enquanto Dados do Dispositivo São Recebidos:
    while True:
        data = receiveFullJson(cloud)
        if not data:
            break
        print(f"\nReceived: {data.decode()}\n")
        conn.sendall(b"Data Received Successfully") # Enviando confirmação ao cliente.

    # Fechando a Conexão com o Dispositivo:
    conn.close()
