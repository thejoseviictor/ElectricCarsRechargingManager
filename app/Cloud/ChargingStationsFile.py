# Esta Classe é Responsável por Armazenar os Dados dos Postos de Recarga em um Arquivo ".json" na Nuvem:

import json
import os
from ReservationsFile import Reservation

class ChargingStationsFile:
    # Inicializando a Classe e seus Atributos:
    def __init__(self, json_file="charging_stations.json"):
        self.json_file = json_file
        self.chargingStationsList = [] # Lista dos Postos de Recarga.

    # Lendo os Pontos de Recarga no Arquivo ".json":
    def readChargingStations(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                self.chargingStationsList = json.load(file) # Salvando os Dados do Arquivo ".json" na Lista.
    
    # Procurando um Posto de Recarga Específico:
    def findChargingStation(self, id):
        # Percorrendo a Lista:
        for cs in self.chargingStationsList:
            if cs["id"] == id:
                return cs
        else:
            print(f"\nPosto de Recarga com ID '{id}' Não Foi Encontrado!\n")
            return None

    # Listando os Postos de Recarga Cadastrados no Arquivo ".json":
    def listChargingStations(self):
        return self.chargingStationsList

    # Salvando a Lista no Arquivo ".json":
    def saveChargingStations(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.chargingStationsList, file, indent=4)

    # Atualizando os Dados de um Posto de Recarga Específico:
    def updateChargingStation(self, id, x_position, y_position):
        updateStatus = False # Vai Salvar o Status da Atualização.
        for cs in self.chargingStationsList: # cs = Charging Station.
            if cs["id"] == id:
                cs["x_position"] = x_position
                cs["y_position"] = y_position
                updateStatus = True
        if updateStatus:
            self.saveChargingStations() # Salvando no Arquivo ".json".
            print(f"\nPosto de Recarga com ID '{id}' Foi Atualizado com Sucesso!\n")
        else:
            print(f"\nPosto de Recarga com ID '{id}' Não Foi Encontrado!\n")
    
    # Criando um Novo Posto de Recarga no Arquivo ".json":
    def createChargingStation(self, id, x_position, y_position):
        # Verificando Se Já Existe um Posto de Recarga Com Mesmo ID Cadastrado:
        if any(cs["id"] == id for cs in self.chargingStationsList): # Se Achar Pelo Menos um Com o Mesmo ID.
            print(f"\nJá Existe um Posto de Recarga com ID '{id}'!\n")
        # Salvando o Novo Posto de Recarga, Se Não Existir:
        else:
            self.chargingStationsList.append({"id": id, "x_position": x_position, "y_position": y_position}) # Salvando na Lista.
            self.saveChargingStations() # Salvando no Arquivo ".json".
            print(f"\nPosto de Recarga com ID '{id}' Foi Salvo com Sucesso!\n")
