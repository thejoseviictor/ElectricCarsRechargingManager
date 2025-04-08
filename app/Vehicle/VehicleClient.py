# Classe responsável pela comunicação entre cliente (Veículo) e servidor (Nuvem)

from dataclasses import dataclass
from Vehicle import Vehicle

import os
import socket
import json

@dataclass
class VehicleClient:

    path = os.path.join(os.path.dirname(__file__), "date.json") # Define o caminho do arquivo "date.json"

    with open(path, "r") as file: 
        date = json.load(file) # Importa o arquivo json com os dados de usuário, veículo e comunicação com o servidor


    server_host: str
    server_port: int

    server_host = str(date["host"])
    server_port = int(date["port"])

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
        confirmation = vehicle_socket.recv(4096)
        confirmationDecoded = confirmationDecoded.decode()

        reservation = {
            "reservationID" : "" , 
            "chargingStationID" : "" , 
            "chargingPointID" : "" , 
            "chargingPointPower" : "", 
            "kWhPrice" : "" , 
            "vehicleID" : "" , 
            "startDateTime" : "", 
            "finishDateTime" : "", 
            "duration" : "" , 
            "price" : ""
        }

        try:
            dates = json.loads(confirmationDecoded)  # transforma JSON string em dict
            reservation.update(dates)

            print("Reserva efetuada: \n")
            print(f" ID da reserva: {reservation['reservationID']} \n")
            print(f" ID do posto: {reservation['chargingStationID']} \n")
            print(f" ID do ponto de recarga: {reservation['chargingPointID']} \n")
            print(f" Potência do ponto de carregamento: {reservation['chargingPointPower']} \n")
            print(f" Preço por kWh: {reservation['kWhPrice']} \n")
            print(f" ID do veículo: {reservation['vehicleID']} \n")
            print(f" Início da recarga: {reservation['startDateTime']} \n")
            print(f" Fim da recarga: {reservation['finishDateTime']} \n")
            print(f" Duração : {reservation['duration']} \n")
            print(f" Preço : {reservation['price']} \n")

        except json.JSONDecodeError:
            print("Erro ao decodificar JSON")

        vehicle.archiveReservation(reservation)

        # Fecha a conexão entre cliente/servidor
        vehicle_socket.close()


    
