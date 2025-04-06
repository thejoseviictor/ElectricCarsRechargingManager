# Será Armazenada no Arquivo de Reservas do Postos de Recarga:

import json
import os
import datetime

class Reservation:
    # Inicializando a Classe e seus Atributos:
    def __init__(self, id, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID, actualBatteryPercentage, batteryCapacity):
        self.id = id    # ID da Reserva.
        self.chargingStationID = chargingStationID  # ID do Posto de Recarga.
        self.chargingPointID = chargingPointID  # ID do Ponto de Carregamento.
        self.chargingPointPower = chargingPointPower # Potência do Ponto de Carregamento em Watt.
        self.kWhPrice = kWhPrice    # Preço do kWh do Ponto de Carregamento.
        self.vehicleID = vehicleID  # ID do Veículo.
        self.startDateTime = self.calculateStartDateTime()    # Formato ISO: 0000-00-00T00:00:00 (Ano, Mês, Dia, T(Separador Entre Data e Hora), Hora, Minutos, Segundos)
        self.finishDateTime = self.calculateFinishDateTime()    # Formato ISO: 0000-00-00T00:00:00 (Ano, Mês, Dia, T(Separador Entre Data e Hora), Hora, Minutos, Segundos)
        self.duration = self.calculeDuration(actualBatteryPercentage, batteryCapacity)  # Duração da Recarga em Horas.
        self.price = self.calculatePrice()  # Preço da Recarga.

    # Calculando o Preço da Recarga:
    # kWh = (Potência do Carregador (Watt) * Tempo (Horas)) / 1000
    def calculatePrice(self):
        kWh = (self.chargingPointPower * self.duration) / 1000
        return kWh * self.kWhPrice

    # Calculando o Tempo para Completar a Carga de Bateria do Veículo:
    # Tempo (Horas) = ((Carga Desejada - Carga Atual) * Capacidade da Bateria (kWh)) / Potência do Carregador (kW)
    def calculateDuration(self, actualBatteryPercentage, batteryCapacity):
        return ((100 - actualBatteryPercentage) * batteryCapacity) / (self.chargingPointPower / 1000)

    # NÃO FINALIZADO!
    # Novas Reservas São Feitas para 5 Minutos Após a Última Reserva Cadastrada no Ponto de Carregamento:
    def calculateStartDateTime(self):
        pass
    
    # Calcula a Data Que o Veículo Irá Terminar de Usar o Ponto de Carregamento, de Acordo com a Duração da Recarga em Horas:
    # Data de Finalização = Data de Ínicio + Duração de Carregamento em Horas
    def calculateFinishDateTime(self):
        start = datetime.datetime.fromisoformat(self.startDateTime) # Decodificando a Data de Ínicio do Formato ISO para DateTime.
        finish = start + datetime.timedelta(hours=self.duration) # Calculando a Data de Finalização.
        return finish.isoformat() # Codificando a Data de Finalização do DateTime para Formato ISO.

# Salvando as Reservas em um Arquivo ".json":
class ReservationsFile: 
    # Inicializando a Classe e seus Atributos:
    def __init__(self, json_file="reservations.json"):
        self.json_file = json_file
        self.reservationsList = [] # Lista de Reservas.
    
    # Lendo as Reservas no Arquivo ".json":
    def readReservations(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                self.reservationsList = json.load(file) # Salvando os Dados do Arquivo ".json" na Lista.
    
    # Procurando uma Reserva para um Veículo Específico:
    def findReservation(self, id, vehicleID):
        # Percorrendo a Lista de Reservas:
        for reservation in self.reservationsList:
            if reservation["id"] == id and reservation["vehicleID"] == vehicleID:
                return reservation
        else:
            print(f"\nReserva com ID '{id}', Para o Veículo com ID '{vehicleID}', Não Foi Encontrada!\n")
            return None

    # Listando Todas as Reservas Cadastradas para os Pontos de Carregamento, em um Posto de Recarga Específico:
    def listReservations(self, chargingStationID):
        searchList = [] # Onde Serão Salvas as Reservas Encontradas.
        for reservation in self.reservationsList:
            if reservation["chargingStationID"] == chargingStationID:
                searchList.append(reservation)
        return searchList # Retornando as Reservas Encontradas.

    # Salvando a Lista de Reservas no Arquivo .json:
    def saveReservations(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.reservationsList, file, indent=4)
    
    # NÃO FINALIZADO!
    # Criando uma Reserva no Arquivo .json:
    def createReservation(self, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID, actualBatteryPercentage, batteryCapacity):
        object = Reservation(id, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID, actualBatteryPercentage, batteryCapacity)
        # Verificando se já existe um posto de recarga com mesmo ID cadastrado:
        if any(cs["id"] == id for cs in self.chargingStationsList): # Se Achar Pelo Menos um Com o Mesmo ID.
            print(f"\nJá Existe um Posto de Recarga com ID '{id}'!\n")
        # Salvando o novo posto de recarga, se não existir:
        else:
            self.chargingStationsList.append({"id": id, "x_position": x_position, "y_position": y_position}) # Salvando na Lista.
            self.saveChargingStations() # Salvando no Arquivo .json.
            print(f"\nPosto de Recarga com ID '{id}' Foi Salvo com Sucesso!\n")
    
    # Removendo uma Reserva de um Veículo Específico:
    def deleteReservation(self, id, vehicleID):
        newReservationsList = [] # Lista de Backup das Reservas.
        foundStatus = False # Salva o Status de Reserva Encontrada.
        for reservation in self.reservationsList:
            # Atualizando o Status, Se a Reserva a Ser Removida For Encontrada:
            if reservation["id"] == id and reservation["vehicleID"] == vehicleID:
                foundStatus = True
            # Copiando as Reservas com ID e "VehicleID" Diferentes para uma Nova Lista:
            else:
                newReservationsList.append(reservation)
        self.reservationsList = newReservationsList # Restaurando a Lista de Reservas, Sem a Removida.
        self.saveReservations() # Salvando no Arquivo ".json".
        # Exibindo as Mensagens de Status:
        if foundStatus:
            print(f"\nReserva com ID '{id}', Para o Veículo com ID '{vehicleID}', Foi Removida com Sucesso!\n")
        else:
            print(f"\nReserva com ID '{id}', Para o Veículo com ID '{vehicleID}', Não Foi Encontrada!\n")
            return None
    
    # NÃO FINALIZADO (Verificar se tem espaço entre reservas)
    # Encontrando a Data de Finalização da Última Reserva Cadastrada em um Ponto de Carregamento Específico:
    # Resumindo, Descobrir Quando o Último Veículo Vai Terminar de Usar o Ponto de Carregamento.
    def getLastReservationDateTime(self, reservationObject, chargingPointID):
        found = False # Indicará Se um Data Posterior For Encontrada.
        lastDateTime = datetime.datetime(1999, 12, 31, 0, 0, 0) # Data de Base para Comparação Inicial.
        # Percorrendo a Lista de Reservas:
        for reservation in self.reservationsList:
            if reservation["chargingPointID"] == chargingPointID:
                dateTimeInFile = datetime.datetime.fromisoformat(reservation["finishDateTime"]) # Decodificando a Data na Lista para DateTime.
                # Salvando, Se a Data na Lista For Posterior:
                if lastDateTime < dateTimeInFile:
                    found = True # Alterando o Status de Data Posterior Encontrada.
                    lastDateTime = dateTimeInFile 
        if found:
            return lastDateTime.isoformat() # Retornando a Data Encontrada Codificada em ISO.
        # Retorna "None", Se Não Houver Nenhuma Reserva no Ponto de Carregamento:
        else:
            return None