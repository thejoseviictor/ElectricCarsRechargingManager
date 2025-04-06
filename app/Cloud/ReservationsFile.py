# Será Armazenada no Arquivo de Reservas do Postos de Recarga:

import json
import os

class Reservation:
    # Inicializando a Classe e seus Atributos:
    def __init__(self, ID, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID):
        self.ID = ID    # ID da Reserva.
        self.chargingStationID = chargingStationID  # ID do Posto de Recarga.
        self.chargingPointID = chargingPointID  # ID do Ponto de Carregamento.
        self.chargingPointPower = chargingPointPower # Potência do Ponto de Carregamento em Watts.
        self.kWhPrice = kWhPrice    # Preço do kWh do Ponto de Carregamento.
        self.vehicleID = vehicleID  # ID do Veículo.
        self.startDateTime = self.calculateStartDateTime()    # Formato da Data: DD/MM/AAAA-HH:MM (Dia, Mês, Ano, Hora, Minutos)
        self.finishDateTime = self.calculateFinishDateTime()    # Formato da Data: DD/MM/AAAA-HH:MM (Dia, Mês, Ano, Hora, Minutos)
        self.duration = self.calculeDuration()  # Duração da Recarga em Horas.
        self.price = self.calculatePrice()  # Preço da Recarga.

    # Calculando o Preço da Recarga:
    # kWh = (Potência do Carregador (Watts) * Tempo (Horas)) / 1000
    def calculatePrice(self):
        kWh = (self.chargingPointPower * self.duration) / 1000
        return kWh * self.kWhPrice

    # NÃO FINALIZADO!
    def calculateDuration(self):
        pass

    # NÃO FINALIZADO!
    def calculateStartDateTime(self):
        pass
    
    # NÃO FINALIZADO!
    # Novas Reservas São Feitas para 5 Minutos Após a Última Reserva Cadastrada:
    def calculateFinishDateTime(self):
        pass

class ReservationsFile: 
    # Inicializando a Classe e seus Atributos:
    def __init__(self, json_file="reservations.json"):
        self.json_file = json_file
        self.reservationsList = [] # Lista de Reservas.
    
    # NÃO FINALIZADO!
    # Lendo as Reservas no Arquivo ".json":
    def readReservation(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                self.reservationsList = json.load(file) # Salvando os Dados do Arquivo ".json" na Lista.
    
    # NÃO FINALIZADO!
    # Procurando uma Reserva Específica:
    def findReservation(self, id):
        # Percorrendo a Lista:
        for reservation in self.reservationsList:
            if reservation["id"] == id:
                return reservation
        else:
            print(f"\nReserva com ID '{id}' Não Foi Encontrada!\n")
            return None

    # NÃO FINALIZADO!
    # Listando as Reservas Cadastradas no Arquivo .json:
    def listReservation(self, chargingStationID):
        for reservation in self.reservationsList:
            if reservation["chargingStationID"]
        return self.chargingStationsList

    # NÃO FINALIZADO!
    # Salvando a Lista no Arquivo .json:
    def saveChargingStations(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.chargingStationsList, file, indent=4)

    # NÃO FINALIZADO!
    # Atualizando os Dados de um Posto de Recarga Específico:
    def updateChargingStation(self, id, x_position, y_position):
        updateStatus = False # Vai Salvar o Status da Atualização.
        for cs in self.chargingStationsList: # cs = Charging Station.
            if cs["id"] == id:
                cs["x_position"] = x_position
                cs["y_position"] = y_position
                updateStatus = True
        if updateStatus:
            self.saveChargingStations() # Salvando no Arquivo .json.
            print(f"\nPosto de Recarga com ID '{id}' Foi Atualizado com Sucesso!\n")
        else:
            print(f"\nPosto de Recarga com ID '{id}' Não Foi Encontrado!\n")
    
    # NÃO FINALIZADO!
    # Criando uma Reserva no Arquivo .json:
    def createReservation(self, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID):
        object = Reservation(id, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID)
        # Verificando se já existe um posto de recarga com mesmo ID cadastrado:
        if any(cs["id"] == id for cs in self.chargingStationsList): # Se Achar Pelo Menos um Com o Mesmo ID.
            print(f"\nJá Existe um Posto de Recarga com ID '{id}'!\n")
        # Salvando o novo posto de recarga, se não existir:
        else:
            self.chargingStationsList.append({"id": id, "x_position": x_position, "y_position": y_position}) # Salvando na Lista.
            self.saveChargingStations() # Salvando no Arquivo .json.
            print(f"\nPosto de Recarga com ID '{id}' Foi Salvo com Sucesso!\n")