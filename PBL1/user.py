from dataclasses import dataclass

@dataclass
class User:

    uid: int
    name: str
    email: str
    password: str
    
    '''
    def __init__ (self, id, owner, licensePlate, energy, criticalEnergy, payment, location):
        self.id: id
        self.name: name
        self.email: email
        self.password: passsword
        self.moneycredit: moneyCrdit
    '''