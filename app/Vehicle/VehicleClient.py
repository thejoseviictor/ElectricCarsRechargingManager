# Classe responsável pela comunicação entre cliente (Veículo) e servidor (Nuvem)

from dataclasses import dataclass
from Vehicle import Vehicle

import os
import socket
import json

@dataclass
class VehicleClient:

    server_host: str
    server_port: int

    def sendRequest(self, vehicle: Vehicle): # Envia uma requisição e dados do client (Veículo) para o servidor (Nuvem).
        
        # Criação do socket para a entidade vehicle.
        vehicle_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # INET (baseado em IPv4).
        # STREAM (baseado no protocolo TCP).
        # Conecta client(Veículo) com servidor (Nuvem)

        vehicle_socket.connect((self.server_host, self.server_port))

        # Dicionário utilizado para selecionar os dados pertinentes para a nuvem ao pedir uma reserva
        vData = {
            "vid": vehicle.vid ,
            "x": vehicle.coordinates(0) ,
            "y": vehicle.coordinates(1) ,
            "actualBatteryPercentage": vehicle.currentEnergy ,
            "batteryCapacity" : vehicle.maximumBattery ,
            "scheduleReservation" : True
        }

        # Cria um json baseado no dicionário "vData" e envia as informações para o servidor (Nuvem).
        request = json.dumps(vData, indent=4).encode('utf-8')
        vehicle_socket.sendall(request)

        # Recebe confirmação de recebimento do servidor, print só ocorrerá após isso.
        confirmation = self.vehicle_socket.recv(1024)
        print(" Posto selecionado: {}".format(confirmation.decode('utf-8')))

        # Fecha a conexão entre cliente/servidor
        vehicle_socket.close()

    def requestReservation(self, vehicle:Vehicle):

        vehicle_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        vehicle_socket.connect((self.server_host, self.server_port))

        # Dicionário utilizado para selecionar os dados pertinentes para a nuvem ao pedir uma reserva
        vData = {
            "vid": vehicle.vid ,
            "findReservation": True
        }

        # Cria um json baseado no dicionário "vData" e envia as informações para o servidor (Nuvem).
        request = json.dumps(vData, indent=4).encode('utf-8')
        self.vehicle_socket.sendall(request)

        # Recebe confirmação de recebimento do servidor, print só ocorrerá após isso.
        confirmation = vehicle_socket.recv(1024)
        print(" Reservas: {}".format(confirmation.decode('utf-8')))

        # Fecha a conexão entre cliente/servidor
        vehicle_socket.close()

    
