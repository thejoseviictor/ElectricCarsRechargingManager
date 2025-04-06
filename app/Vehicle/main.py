''' Classe main do veiculo'''

import os
import time

from app.Vehicle.Vehicle import Vehicle
from app.Vehicle.VehicleClient import VehicleClient
from app.Vehicle.VehicleUtility import VehicleUtility

close = True

client : VehicleClient
vehicle : Vehicle
utility : VehicleUtility

while(close):

    print(" ---------- ReVehicle : Sistema de recarga para veículos elétricos ----------\n")
    
    time.sleep(2)
    utility.clearTerminal()

    print(" Bem vindo(a)! \n")

    print(" Deseja iniciar o sistema? \n")
    reply = input(" Digite: \n 1. Para sim \n 2. Para não ")
    utility.clearTerminal()

    if(reply == "1"):
        