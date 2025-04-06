# Esta Classe é Responsável por Armazenar os Dados dos Postos de Recarga em um Arquivo ".json" na Nuvem.
# "Charging Station" é o Estabelecimento, Mais Conhecido com Posto.

import json
import os

class ChargingStationsFile:
    # Inicializando a Classe e seus Atributos:
    def __init__(self, json_file="charging_stations.json"):
        self.json_file = json_file
        self.chargingStationsList = [] # Lista dos Postos de Recarga.
        self.readChargingStations() # Recuperando os Dados do Arquivo ".json"

    # Lendo os Pontos de Recarga no Arquivo ".json":
    def readChargingStations(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                self.chargingStationsList = json.load(file) # Salvando os Dados do Arquivo ".json" na Lista.
    
    # Procurando um Posto de Recarga Específico:
    def findChargingStation(self, chargingStationID):
        # Percorrendo a Lista:
        for cs in self.chargingStationsList:
            if cs["chargingStationID"] == chargingStationID:
                return cs
        else:
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Não Foi Encontrado!\n")
            return None

    # Listando os Postos de Recarga Cadastrados no Arquivo ".json":
    def listChargingStations(self):
        return self.chargingStationsList

    # Salvando a Lista no Arquivo ".json":
    def saveChargingStations(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.chargingStationsList, file, indent=4)

    # Atualizando os Dados de um Posto de Recarga Específico:
    def updateChargingStation(self, chargingStationID, x_position, y_position):
        updateStatus = False # Vai Salvar o Status da Atualização.
        cs = self.findChargingStation(chargingStationID) # Chamando a Função de Procurar na Lista.
        if cs: # cs = Charging Station.
            cs["x_position"] = x_position
            cs["y_position"] = y_position
            updateStatus = True
        # Exibindo as Mensagens de Status:
        if updateStatus:
            self.saveChargingStations() # Salvando no Arquivo ".json".
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Foi Atualizado com Sucesso!\n")
        else:
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Não Foi Encontrado!\n")
    
    # Criando um Novo Posto de Recarga e Salvando no Arquivo ".json":
    def createChargingStation(self, chargingStationID, x_position, y_position):
        # Verificando Se Já Existe um Posto de Recarga Com Mesmo ID Cadastrado:
        cs = self.findChargingStation(chargingStationID) # Chamando a Função de Procurar na Lista.
        if cs: # Se Achar Pelo Menos um Com o Mesmo ID.
            print(f"\nJá Existe um Posto de Recarga com ID '{chargingStationID}'!\n")
        # Salvando o Novo Posto de Recarga, Se Não Existir:
        else:
            self.chargingStationsList.append({"chargingStationID": chargingStationID, "x_position": x_position, "y_position": y_position}) # Salvando na Lista.
            self.saveChargingStations() # Salvando no Arquivo ".json".
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Foi Salvo com Sucesso!\n")
    
    # Removendo um Posto do Arquivo ".json":
    def deleteChargingStation(self, chargingStationID):
        newChargingStationsList = [] # Lista de Backup dos Postos.
        foundStatus = False # Salva o Status de Posto de Recarga Encontrado.
        for cs in self.chargingStationsList:
            # Copiando os Postos de Recarga com ID Diferente para uma Nova Lista:
            if cs["chargingStationID"] != chargingStationID:
                newChargingStationsList.append(cs)
            # Atualizando o Status, Se o Posto a Ser Removido For Encontrado na Lista:
            else:
                foundStatus = True
        self.chargingStationsList = newChargingStationsList # Restaurando a Lista de Postos.
        self.saveChargingStations() # Salvando no Arquivo ".json".
        # Exibindo as Mensagens de Status:
        if foundStatus:
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Foi Removido com Sucesso!\n")
        else:
            print(f"\nPosto de Recarga com ID '{chargingStationID}' Não Foi Encontrado!\n")
