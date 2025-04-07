import socket
import json
import time

# Endereço da Nuvem:
SERVER_IP = 'cloud_server'
SERVER_PORT = 64352

# Iniciando o Cliente e Conectando a Nuvem:
def send_request(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_IP, SERVER_PORT))
        message = json.dumps(data)
        client.sendall(message.encode())
        response = client.recv(8192)
        print("Resposta da Nuvem:", response.decode())

# Exemplo de Mensagens de Teste:
def testCreateReservation():
    data = {
        "vid": 1,
        "x": 2,
        "y": 2,
        "actualBatteryPercentage": 20,
        "batteryCapacity": 40,
        "scheduleReservation": True
    }
    send_request(data)

def testDeleteReservation():
    data = {
        "reservationID": 1,
        "vehicleID": 1,
        "deleteReservation": True
    }
    send_request(data)

def testFindReservations():
    data = {
        "vid": 1,
        "findReservation": True
    }
    send_request(data)

# Execução dos Testes:
if __name__ == "__main__":
    print("\nTentando Criar uma Reserva:\n")
    testCreateReservation()
    time.sleep(1)

    print("\nTentando Encontrar uma Reserva:\n")
    testFindReservations()
    time.sleep(1)

    print("\nTentando Excluir uma Reserva:\n")
    testDeleteReservation()
    time.sleep(1)

    print("\nTentando Encontrar uma Reserva:\n")
    testFindReservations()
