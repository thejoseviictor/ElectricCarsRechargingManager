# Data Access Object for Charging Stations on Cloud:

import json
import os

class ChargingStationDAO:
    def __init__(self, json_file="charging_stations.json"):
        self.json_file = json_file
        self.chargingStations = self.readChargingStations()
        pass

    def readChargingStations(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return None
    
    def findChargingStation(self, id):
        return next((cs for cs in self.chargingStations if cs["id"] == id), None)

    def listChargingStations(self):
        return self.chargingStations

    def saveChargingStations(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.chargingStations, file, indent=4)
    
    def createChargingStation(self, id, host, port):
        if any(cs["id"] == id for cs in self.chargingStations):
            print(f"\nThere is already a Charging Station with the ID {id}!\n")
            return None
        self.chargingStations.append({"id": id, "host": host, "port": port})
        self.saveChargingStations
