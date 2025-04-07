''' Classe main do veiculo'''

import time
import random
import sys
import json
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Vehicle import Vehicle
from VehicleUtility import VehicleUtility
from User import User

repeat = True

# Definindo os objetos e as suas informações:

path = os.path.join(os.path.dirname(__file__), "date.json") # Define o caminho do arquivo "date.json"

with open(path, "r") as file: 
    date = json.load(file) # Importa o arquivo json com os dados de usuário, veículo e comunicação com o servidor

# User ----------------------------------------------------------------------------------------------------------------

cpf = date["cpf_user"]
name = date["name_user"]
email = date["email_user"]
password = date["password_user"]

user = User(cpf = cpf, name = name, email = email , password = password)

# Vehicle -------------------------------------------------------------------------------------------------------------

genericID = random.randint(1,99999) # Gera um ID aleatório de 5 dígitos para o veículo
vid = str(genericID).zfill(5)

owner = user
licensePlate = date["license_plate_vehicle"]
moneyCredit = date["money_credit_vehicle"]
currentEnergy = date["current_energy_vehicle"]
criticalEnergy = date["critical_energy_vehicle"]

maximumBattery = random.randint(30,50)

vehicle = Vehicle(vid = vid, owner = owner, licensePlate = licensePlate, moneyCredit = moneyCredit, currentEnergy = currentEnergy, criticalEnergy = criticalEnergy, distanceFromDestination = 0, distanceFromChargingStation = 0, maximumBattery = maximumBattery)

# Client ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

server_host = date["host"]
server_port = date["port"]

# Métodos utilitários --------------------------------------------------------------------------

utility = VehicleUtility()

# ---------------------------------------------------------------------------------------------


while(repeat):

    utility.clearTerminal()

    print(" ---------- veHI : Sistema de recarga para veículos elétricos ----------\n")
    
    time.sleep(3)
    utility.clearTerminal()

    print(" Bem vindo(a)! \n")

    
    wrongDate = True  # Váriavel usada para permitir ou não a entrada no sistema de acordo com os dados de login e senha
    
    while(wrongDate):

        login = input("LOGIN: \t ") # Login com cpf ou email do usuário
        utility.clearTerminal()
        password = input("SENHA: \t ") # Senha de úsuario
        utility.clearTerminal()


        if (login == vehicle.owner.cpf or login == vehicle.owner.email) and password == vehicle.owner.password:
            print (" Login realizado com sucesso ! ")
            time.sleep(3)
            utility.clearTerminal()
            wrongDate = False

        else :
            print(" Login ou senha incorreta. Tente novamente !")
            time.sleep(3)
            utility.clearTerminal()
            wrongDate = True
 

    print(" O que deseja fazer? \n")
    reply = input(" Digite: \n 1. Iniciar sistema \n 2. Ver histórico de reservas \n 3. Sair \n\n -> ")
    utility.clearTerminal()

    if reply == "1" :
        utility.simulation(vehicle, server_host, server_port)
    
    elif reply == "2" :
        utility.showReservations(vehicle, server_host, server_port)

        reply = input("\n O que deseja agora: \n 1. Voltar para o início. \n 2. Fechar programa.")

        if reply == "1" :
            repeat = True
            utility.clearTerminal()

        else:
            repeat = False

        loadPoints = ["...", "..", ".", ""]

        for p in range (loadPoints):
            print(f"Encerando o programa {p} ")
            time.sleep(1)
            utility.clearTerminal()

    else:
        repeat = False

        loadPoints = ["...", "..", ".", ""]

        for p in loadPoints:
            print(f"Encerando o programa {p} ")
            time.sleep(1)
            utility.clearTerminal()