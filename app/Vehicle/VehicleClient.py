# Classe responsável pela comunicação entre cliente (Veículo) e servidor (Nuvem)

from dataclasses import dataclass

from app.Vehicle import Vehicle

import socket
import json

@dataclass
class VehicleClient:

    server_host: str
    server_host: int

    def __init__(self, server_host: str, server_port: int):
        
        # Endereço e porta do servidor (Nuvem) ao qual conectar.
        self.host = server_host # O mesmo IP do servidor.
        self.port = server_port # A porta usada pelo servidor.
        
        # Criação do socket para a entidade vehicle.
        self.vehicle_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # INET (baseado em IPv4).
        # STREAM (baseado no protocolo TCP).

    def sendRequest(self, vehicle: Vehicle): # Envia uma requisição e dados do client (Veículo) para o servidor (Nuvem).

        # Conecta client(Veículo) com servidor (Nuvem)
        self.vehicle_socket.connect((self.host, self.port))

        # Cria um json baseado no objeto (vehicle) e envia as informações para o servidor (Nuvem).
        request = json.dumps(vehicle).encode()
        self.vehicle_socket.sendall(request)

        # Recebe confirmação de recebimento do servidor, print só ocorrerá após isso.
        confirmation = self.vehicle_socket.recv(1024)
        print(" Resposta do servidor: {}".format(confirmation.decode()))

        # Fecha a conexão entre cliente/servidor
        self.vehicle_socket.close()
