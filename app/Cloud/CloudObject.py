import socket
import os
from ChargingStationDAO import ChargingStationDAO

class Cloud:
    def __init__(self):
        self.host = str(os.getenv("CLOUD_HOST")) # Recebendo "host" através da variável de ambiente no "Dockerfile".
        #self.host = "0.0.0.0" # Recebendo "host" através da variável de ambiente no "Dockerfile".
        self.port = int(os.getenv("CLOUD_PORT")) # Recebendo "port" através da variável de ambiente no "Dockerfile".
        #self.port = 64352 # Recebendo "port" através da variável de ambiente no "Dockerfile".
        self.chargingStations = ChargingStationDAO()
        pass
    
    # Criando e ativando o modo de escuta do socket:
    def startSocket(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP IPv4.
        server.bind((self.host, self.port)) # Definindo o IP e porta do socket.
        server.listen(1) # Escutando com uma fila de tamanho "1".
        print("\nWaiting for Connections...\n")
        self.acceptConnection(server)

    # Aceitando conexões e recebendo os dados:
    def acceptConnection(self, server):
        conn, addr = server.accept()
        print(f"\nConnected to {addr}\n")
        while True:
            data = conn.recv(1024) # Dados de até 1024 bytes.
            if not data:
                break
            print(f"\nReceived: {data.decode()}\n")
            # Enviando confirmação ao cliente:
            conn.sendall(b"Data Received Successfully")
        self.closeSocket(server)
    
    # Fechando o socket e servidor:
    def closeSocket(server):
        server.close()

    def registerChargingStation(id, host, port):
        status = ChargingStationDAO.createChargingStation(host, port, id)
        if status == None:
            print("\nCharging Station Registered Successfully!\n")
        else:
            print("\nCharging Station Registration Was Terminated Unsuccessfully!\n")
    
    def requestDistanceFromNearestChargingStation(self):
        pass

    def requestChargingStationAvailability(self):
        pass

    def requestReservation(self):
        pass
