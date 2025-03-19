from chargepoint import ChargePoint
from vehicle import Vehicle

print(" Sistema de recarga de veículos. \n Bem-vinde ;) \n")


#Pontos de recarga predefinidos
p1 = ChargePoint(uid = "1", status = False, location = "coordenada qualquer", distance = 0, time = 00.00)
p2 = ChargePoint(uid = "2", status = False, location = "coordenada qualquer", distance = 0, time = 00.00)
p3 = ChargePoint(uid = "3", status = False, location = "coordenada qualquer", distance = 0, time = 00.00)

#Veículo(s) predefinidos
v1 = Vehicle(id = "1", owner = "João", licensePlate = "ABC1234", energy = 100, criticalEnergy = 20, payment = 00.00, location = "coordenada qualquer")

print(p1.uid)
print(p2.uid)
print(p3.uid)
print(v1.id, v1.owner, v1.licensePlate)