from dataclasses import dataclass

@dataclass
class ChargePoint:

    uid: str
    status: bool
    location: str
    distance: int
    time: float
    reservations = ["fruta", "legumes"]

    '''def __init__ (self, uid, status, location, time):
        
        self.uid = uid
        self.status = status
        self.location = location
        self.time = time
    '''

    def addCar(self, object):
        self.reservations.append(object)
    
    def freeCar():
        reservations.remove(0)