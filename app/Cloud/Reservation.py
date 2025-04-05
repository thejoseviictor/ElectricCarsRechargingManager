# Será Armazenada nos Arquivos de Reservas do Posto de Recarga:

class Reservation:
    def __init__(self, chargingStationID, chargingPointID, chargingPointPower, kWhPrice, vehicleID, datetime, duration):
        self.chargingStationID = chargingStationID  # ID do Posto de Recarga.
        self.chargingPointID = chargingPointID  # ID do Ponto de Carregamento.
        self.chargingPointPower = chargingPointPower # Potência do Ponto de Carregamento em Watts.
        self.kWhPrice = kWhPrice    # Preço do kWh do Ponto de Carregamento.
        self.vehicleID = vehicleID  # ID do Veículo.
        self.datetime = datetime    # Formato da Data: DD/MM/AAAA-HH:MM (Dia, Mês, Ano, Hora, Minutos)
        self.duration = duration    # Duração da Recarga em Minutos.
        self.price = self.calculatePrice()  # Preço da Recarga.

    # Calculando o Preço da Recarga:
    # kWh = (Potência do Carregador (Watts) * Tempo (Horas)) / 1000
    def calculatePrice(self):
        kWh = (self.chargingPointPower * (self.duration / 60)) / 1000
        return kWh * self.kWhPrice
