from dataclasses import dataclass

from app.Vehicle.User import User

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
    reservationHistory = [] #Histórico de reservas realizadas pela conta/veículo.

    
    '''
    def __init__ (self, id, owner, licensePlate, energy, criticalEnergy, payment, location):
        self.id = id
        self.owner = owner
        self.licensePlate = licensePlate

        self.currentEnergy = currentEnergy
        self.criticalEnergy = criticalEnergy
        self.distanceFromDestination = distanceFromDestination
        self.diastanceFromChargingStation = distanceFromChargingStation

    '''

    def definePosition(self,x: int, y: int): # Método que define o localização do veículo
        self.coordinates.append(x)
        self.coordinates.append(y)
