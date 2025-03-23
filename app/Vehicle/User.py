from dataclasses import dataclass

@dataclass
class User:

    cpf: str
    name: str
    email: str
    password: str
    
    '''
    def __init__ (self, id, owner, licensePlate, energy, criticalEnergy, payment, location):
        self.id: id
        self.name: name
        self.email: email
        self.password: passsword
    '''
