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
    
    def createChargingStation(self):
        pass
