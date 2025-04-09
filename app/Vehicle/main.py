'''
Grupo: João Macedo, José Vitor e Thiago 

Componente Curricular: TEC502 - MI - Concorrência e conectividade 

Concluido em: 07/04/2025;

Declaro que este código foi elaborado por mim e pelo meu grupo de forma individualmnte 
e não contém nenhum trecho de código de outro colega ou de outro autor, tais como provindos 
de livros e  apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de 
código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte 
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''

''' Classe main do veiculo'''

import time # Biblioteca usada para fluxos e simulações de tempo
import random # Biblioteca usada para gerar dados e valores aleatórios

'''
Bibliotecas usadas para trabalhar com o fluxo entre diretórios e entradas 
e saidas diretamente com o sistema/terminal

'''
import sys 
import os 

import json # Biblioteca usada para trabalhar com arquivos .json e importar dados fictícios para o sistema

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Importação de classes base para o funcionamnto do sisteema
from Vehicle import Vehicle
from VehicleUtility import VehicleUtility
from User import User

repeat = True # Variavel usada para lidar com o fluxo de repetição do programa

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

# Métodos utilitários --------------------------------------------------------------------------

''' Classe de utilidades, nela há a chamada para processos de comunicação,
    processos de exibição amigável ao úsuario e entre outro processos
'''
utility = VehicleUtility() 

# ---------------------------------------------------------------------------------------------

# Início do sistema

firstLogin = True # Variavel para indicar que apenas um login é preciso.

while(repeat):

    utility.clearTerminal()

    print(" ---------- veHI : Sistema de recarga para veículos elétricos ----------\n")
    
    time.sleep(3)
    utility.clearTerminal()

    print(" Bem vindo(a)! \n")
    time.sleep(2)

    wrongDate = True  # Váriavel usada para permitir ou não a entrada no sistema de acordo com os dados de login e senha
    utility.clearTerminal()

    if(firstLogin):
    
        while(wrongDate):

            login = input("LOGIN (CPF ou Email): \t ") # Pede o login com cpf ou email do usuário (jjt@gmail.com ou 12345678910)
            utility.clearTerminal()
            password = input("SENHA: \t ") # Pede a senha de úsuario (123456car)
            utility.clearTerminal()


            if (login == vehicle.owner.cpf or login == vehicle.owner.email) and password == vehicle.owner.password:
                print (" Login realizado com sucesso ! ")
                time.sleep(3)
                utility.clearTerminal()
                wrongDate = False
                firstLogin = False

            else :
                print(" Login ou senha incorreta. Tente novamente !")
                time.sleep(3)
                utility.clearTerminal()
                wrongDate = True
 

    print(" O que deseja fazer? \n")
    reply = input(" Digite: \n 1. Iniciar sistema \n 2. Ver histórico de reservas \n 3. Sair \n\n -> ")
    utility.clearTerminal()

    '''
    Apresenta 3 opções de execução do programa:
    
    1. A opção 1 é para entrar na simulação onde o sistema do carro é iniciado e 
    consome a bateria a medida que se locomove

    obs:    .A bateria é decrementada de forma aleatória para simular um carro em 
            movimento ou parado

            .O decremento ocorre a cada 2 segundos (2 segundos é o correspondente a cada 
            1 hora de uso do veículo )

            .

    2. A opção 2 é usada para ver a reserva do veículo
    
    obs:    .Dentro da opção 2, após ver a reserva, há a opção de voltar para o início o encerrar o programa definitivamente

    3. A opção 3 é para encerrar o sistema completamente. 

    '''

    if reply == "1" :
        realized = utility.simulation(vehicle)

        if realized == True:
            print("Reserva realizada !")
            repeat = True

        else:
            print("Reserva não realizada! Tenha cuidado para não ficar sem carga!")
            repeat = True
            time.sleep(3)

    
    elif reply == "2" :
        vehicle.showReservation()

        reply = input("\n O que deseja agora: \n 1. Voltar para o início. \n 2. Fechar programa. \n ->")

        if reply == "1" :
            repeat = True
            utility.clearTerminal()

        else:
            repeat = False
            utility.endAnimation()

    else:
        repeat = False
        utility.endAnimation()