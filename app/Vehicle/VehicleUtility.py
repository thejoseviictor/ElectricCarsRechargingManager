''' Classe responsável por manter métodos de definição de informações e simulações do veículo '''
from dataclasses import dataclass
from VehicleClient import VehicleClient
from Vehicle import Vehicle


import random
import time
import os
@dataclass
class VehicleUtility:
    
    # Método que cria 2 coordenadas aleatórias dentro do intervalo determinado.
    def defineCoordinates(self, vehicle: Vehicle):
        
        x = random.randint(0,100) # Área de localização representada por matriz de 0 a 100.
        y = random.randint(0,100)
        ''' 
        obs:
        - Para decimais aleatórios: random.uniform(a,b)
        - Para inteiros aleatórios: random.randint(a,b)
        '''
        vehicle.definePosition(x,y)

    # Método que realiza a simulação de consumo de bateria
    def simulation(self, vehicle : Vehicle):
        realized = False
        situation = True

        while(situation):
            
            if vehicle.currentEnergy <= vehicle.criticalEnergy: # Quando a bateria chega ao nível crítico:

                # Pergunta se o proprietario deseja ou não fazer uma reserva
                reply = input(f" Bateria em ponto crítico: {vehicle.currentEnergy}% \n \n Deseja fazer uma reserva? \n \n 1.Sim \n 2.Não \n \n -> ")
                
                if reply == "1":
                    self.defineCoordinates(vehicle)

                    request = VehicleClient()
                    request.sendRequest(vehicle)
                    
                    situation = False

                    realized = True
                
                else:
                    self.clearTerminal()
                    situation = False

            elif vehicle.currentEnergy >= vehicle.criticalEnergy :
                decrement = random.randint(0,20) # Variavel utilizada para decremento aleatório da bateria, para simulação 
                vehicle.currentEnergy -= decrement
                
                print(f"\n Bateria: {vehicle.currentEnergy}") # Mostra a bateria na tela constantemente
                time.sleep(2)
                self.clearTerminal()
        
        return realized
    '''
    Nesse método há a simulação de viagem de um veículo:
    A cada 2 segundos, o veículo perde uma % aleatoria da bateria.
    2 segundos = 1 hora no mundo real
    Ao chegar na energia critica, ele inicia o processo de requisição de reserva, para a nuvem, para realizar a recarga em um posto.
    '''

    @staticmethod
    def clearTerminal():
       os.system('cls' if os.name == 'nt' else 'clear')
    
    def endAnimation(self):

        loadPoints = ["...", "..", ".", ""]

        for p in loadPoints:
            print(f"Encerando o programa {p} ")
            time.sleep(1)
            self.clearTerminal()
