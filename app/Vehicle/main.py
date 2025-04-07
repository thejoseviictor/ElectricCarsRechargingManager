''' Classe main do veiculo'''

import time
import random
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Vehicle import Vehicle
from VehicleClient import VehicleClient
from VehicleUtility import VehicleUtility
from User import User

close = True

# Definindo classes principais
user = User()
vehicle = Vehicle()
client = VehicleClient()
utility = VehicleUtility()

# Definindo as informações dos objetos:

# User
user.cpf = os.environ.get("CPF_USER")
user.name = os.environ.get("NAME_USER")
user.email = os.environ.get("EMAIL_USER")
user.password = os.environ.get("PASSWORD_USER")

# Vehicle
vehicle.vid = random.randint(0,99999)
vehicle.owner = user
vehicle.licensePlate = os.environ.get("LICENSE_PLATE_VEHICLE")
vehicle.moneyCredit = int( os.environ.get("MONEY_CREDIT_VEHICLE") )
vehicle.currentEnergy = int( os.environ.get("CURRENT_ENERGY_VEHICLE") )
vehicle.criticalEnergy = int( os.environ.get("CRITICAL_ENERGY_VEHICLE") )

while(close):

    print(" ---------- veHI : Sistema de recarga para veículos elétricos ----------\n")
    
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

