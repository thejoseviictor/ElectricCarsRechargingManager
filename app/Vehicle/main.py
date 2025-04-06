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

    print(" O que deseja fazer? \n")
    reply = input(" Digite: \n 1. Iniciar sistema \n 2. Ver histórico de reservas \n 3. Sair ")
    utility.clearTerminal()

    if reply == "1" :
        utility.simulation(vehicle)
    
    elif reply == "2" :
        utility.showreservations(vehicle)

        reply = input("\n O que deseja agora: \n 1. Voltar para o início. \n 2. Fechar programa.")

        if reply == "1" :
            close = True
            utility.clearTerminal()

        else:
            close = False

            loadPoints = ["...", "..", ".", ""]

            for p in range (loadPoints):
                print(f"Encerando o programa {p} ")
                time.sleep(1)
                utility.clearTerminal()

