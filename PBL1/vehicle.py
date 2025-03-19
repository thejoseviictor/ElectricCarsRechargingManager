from dataclasses import dataclass

from user import User

@dataclass
class Vehicle:

    id: str
    owner: user
    licensePlate: str

    currentEnergy: int
    criticalEnergy: int
    distanceFromDestination: int
    distanceFromChargingStation: int
    
    '''
    def __init__ (self, id, owner, licensePlate, energy, criticalEnergy, payment, location):
        self.id = id
        self.owner = owner
        self.licensePlate = licensePlate

        self.currentEnergy = currentEnergy
        self.criticalEnergy = criticalEnergy
        self.distanceFromDestination = distanceFromDestination
        slf.diastanceFromChargingStation = distanceFromChargingStation
    '''