import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ChargingPoint.ChargingPoint import ChargingPoint
from app.Vehicle.Vehicle import Vehicle
from app.Vehicle.User import User

print(" Sistema de recarga de veículos. \n Bem-vinde ;) \n")


#Pontos de recarga predefinidos
p1 = ChargingPoint(cid = "1")
p2 = ChargingPoint(cid = "2")
p3 = ChargingPoint(cid = "3")

#Veículo(s) predefinidos

u1 = User(cpf = "000.000.000-00", name = "João Victor Macedo", email = "joao@gmail.com", password = "123Joao@")

v1 = Vehicle(vid = "1", owner = u1, licensePlate = "ABC1234", moneyCredit = 100.00, currentEnergy = 100, criticalEnergy = 20, distanceFromDestination = 10, distanceFromChargingStation = 5)
v1.definePosition(2,5)

print(p1.cid)
print(p2.cid)
print(p3.cid)
print(v1.vid, v1.owner, v1.licensePlate,v1.coordinates)
