from dataclasses import dataclass

from app.Vehicle.Vehicle import Vehicle
from app.ChargingPoint.Reservation import Reservation

@dataclass
class ChargingPoint:

    cid: str
    chargingBays = [] # Baias de recarga em cada posto.
    
    coordinates = [] #Coordenadas/localização do ponto de recarga.
    reservationHistory = [] # Lista de reservas feitas no ponto de recarga.

    '''def __init__ (self, uid, status, location, time):
        
        self.cid = cid

    '''

    def occupyBay(self, vehicle : Vehicle): # Método para ocupar alguma das baías de recarga disponíveis.
        self.chargingBays.append(vehicle)
    
    def freeBay(self, vid: str): # Método para liberar baía após o encerramento do carregamento.
        
        i = 0

        for v in self.chargingBays:
            
            if v.vid == vid:  
                del self.chargingBays[i]
            
            i += 1

    def definePosition(self, x: int, y: int): # Método para definir as coordenadas/localização do ponto de recarga.
        self.coordinates.append(x)
        self.coordinates.append(y)

    def registerReservation(self, reservation: Reservation): # Método para registrar um carregamento finalizado.
        self.reservationHistory.append(reservation)
