from dataclasses import dataclass

from User import User

@dataclass
class Vehicle:

    vid: str
    owner: User
    licensePlate: str
    moneyCredit: float

    currentEnergy: int
    criticalEnergy: int
    distanceFromDestination: int
    distanceFromChargingStation: int
    maximumBattery : int

    coordinates = [] # Coordenadas de longitude e latitude do veículo.
    reservations = [] # Guarda as reservas

    def definePosition(self,x: int, y: int): # Método que define o localização do veículo
        self.coordinates.append(x)
        self.coordinates.append(y)
    
    def archiveReservation(self, reservation: dict):
        self.reservations.append(reservation)

    def showReservation(self):

        if self.reservations :
            
            print("Reservas efetuadas: \n")

            for r in self.reservations:
                
                print(" ---------------------------------------------- ")
                print(f" ID da reserva: {r['reservationID']} \n")
                print(f" ID do posto: {r['chargingStationID']} \n")
                print(f" ID do ponto de recarga: {r['chargingPointID']} \n")
                print(f" Potência do ponto de carregamento: {r['chargingPointPower']} \n")
                print(f" Preço por kWh: {r['kWhPrice']} \n")
                print(f" ID do veículo: {r['vehicleID']} \n")
                print(f" Início da recarga: {r['startDateTime']} \n")
                print(f" Fim da recarga: {r['finishDateTime']} \n")
                print(f" Duração : {r['duration']} \n")
                print(f" Preço : {r['price']} \n")
                print(" ---------------------------------------------- ")
        
        else:

            print("Não há reservas mo momento !")
