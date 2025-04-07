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

    coordinates = [] #Coordenadas de longitude e latitude do veículo.

    def definePosition(self,x: int, y: int): # Método que define o localização do veículo
        self.coordinates.append(x)
        self.coordinates.append(y)
