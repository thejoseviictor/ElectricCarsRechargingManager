''' Classe responsável por manter métodos de definição de informações e simulações do veículo '''
from dataclasses import dataclass
from app.Vehicle.VehicleClient import VehicleClient
from app.Vehicle.Vehicle import Vehicle


import random
import math
import time
import threading

@dataclass
class VehicleUtility:
    
    # Método que cria 2 coordenadas aleatórias dentro do intervalo determinado.
    def defineCoordinates(vehicle: Vehicle):
        
        x = random.randint(0,100) # Área de localização representada por matriz de 0 a 100.
        y = random.randint(0,100)
        ''' 
        obs:
        - Para decimais aleatórios: random.uniform(a,b)
        - Para inteiros aleatórios: random.randint(a,b)
        '''
        vehicle.definePosition(x,y)
    
    # Método que calcula a distância entre 2 pontos.
    def defineDistance(xV:int, yV:int, xP:int, yP:int):

        distance = math.sqrt( ((xP - xV)**2) + ((yP - yV)**2) )

        return distance

    # Método que realiza a simulação de consumo de bateria
    def simulation(vehicle: Vehicle):
        
        while(True):
            if vehicle.currentEnergy <= vehicle.criticalEnergy:
                
                request = VehicleClient("0.0.0.0", 600000)
                request.sendRequest(vehicle)

            else:
                vehicle.currentEnergy -= 10
                time.sleep(1)
            
            '''
            Vai ser utilizado na main para simular o carro rodando 
            thread = threading.Thread(target = simulation, args=(vehicle,time,))
            thread.start()

            '''
    '''0
    Nesse método há a simulação de viagem de um veículo:

    A cada 2 segundos, o veículo perde 10% da bateria.
    Ao chegar na energia critical, ele inicia o processo de requisição de reserva, para a nuvem, para realizar a recarga em um posto.
    '''