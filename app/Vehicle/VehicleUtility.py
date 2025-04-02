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
        
        x = random.uniform(0,100) # Área de localização representada por matriz de 0 a 100.
        y = random.uniform(0,100)
        ''' 
        obs:
        - Para decimais aleatórios: random.uniforme(a,b)
        - Para inteiros aleatórios: random.randint(a,b)
        '''
        vehicle.definePosition(x,y)
    
    # Método que calcula a distância entre 2 pontos.
    def defineDistance(xV:int, yV:int, xP:int, yP:int):

        distance = math.sqrt( ((xP - xV)**2) + ((yP - yV)**2) )

        return distance

    # Método que realiza a simulação de consumo de bateria
    def simulation(vehicle: Vehicle):
        
        if vehicle.currentEnergy == vehicle.criticalEnergy:
            request = VehicleClient("0.0.0.0", 600000)
            request.sendRequest(vehicle)

        else:
            vehicle.currentEnergy -= 10 
            time.sleep(1)
        
        time = 10  # Tempo da contagem em segundos
        thread = threading.Thread(target=contador, args=(temp,))
        thread.start()