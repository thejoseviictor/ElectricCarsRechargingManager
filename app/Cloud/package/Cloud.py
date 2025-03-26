import socket
import os
from ChargingStationDAO import ChargingStationDAO

class Cloud:
    def __init__(self, host, port, chargingStations):
        self.host = int(os.getenv("CLOUD_HOST")) # Recebendo "host" através da variável de ambiente no "Dockerfile".
        self.port = int(os.getenv("CLOUD_PORT")) # Recebendo "port" através da variável de ambiente no "Dockerfile".
        self.chargingStations = ChargingStationDAO.readChargingStations()
        pass

    def registerChargingStation(host, port, id, brand):
        status = ChargingStationDAO.createChargingStation(host, port, id, brand)
        if status == 0:
            print("Charging Station Registered Successfully!")
        else:
            print("Charging Station Registration Was Terminated Unsuccessfully!")

    def requestDistanceFromNearestChargingStation(self):
        pass

    def requestChargingStationAvailability(self):
        pass

    def requestReservation(self):
        pass
