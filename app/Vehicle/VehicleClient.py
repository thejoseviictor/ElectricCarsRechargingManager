from dataclasses import dataclass

import socket
import json

class Vehicle_Client: 
    
    ''' Coisas a ajustar: 
    1. host e port;
    2. divisão das operações em métodos;
    3. enviar objeto vehicle para nuvem utilizando json (conversão entre objeto e json)

    '''

    # Criação do socket para a entidade vehicle.
    vehicle_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # INET (baseado em IPv4).
    # STREAM (baseado no protocolo TCP).

    # Endereço e porta do servidor ao qual conectar.
    host = '127.0.0.1'  # O mesmo IP do servidor (localhost).
    port = 65432  # A porta usada pelo servidor.

    # Conecta-se ao servidor/host
    vehicle_socket.connect((host, port))

    # Envia uma mensagem para o servidor.
    vehicle_socket.sendall("Olá, servidor!".encode())

    # Recebe a resposta do servidor, print só ocorrerá com a resposta afirmativa do servidor host.
    data = vehicle_socket.recv(1024)
    print(f"Resposta do servidor: {data.decode()}")

    # Fecha a conexão entre a o servidor host/nuvem
    vehicle_socket.close()
