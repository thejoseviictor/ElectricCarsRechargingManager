import socket
import json
import time

# Endereço da Nuvem:
SERVER_IP = 'cloud_server'
SERVER_PORT = 64352

# Garantindo Que o JSON Completo Seja Recebido:
def receiveFullJson(client):
    buffer = b"" # Variável de Bytes Vazia, Onde os Dados, em Pedaços, Serão Salvos.
    # Loop de Recebimento do JSON Completo:
    while True:
        chunk = client.recv(8192) # Recebendo os Dados em Partes de 1024 Bytes.
        # Finalizando, Se Não Houverem Mais Dados a Receber:
        if not chunk:
            break
        buffer += chunk # Somando os Dados no Buffer.
        # Testando Se o JSON Já Está Completo:
        try:
            return json.loads(buffer.decode()) # Decodificando os Dados em Dicionário (utf-8)
        # Erro de Dados Incompletos:
        except json.JSONDecodeError:
            continue

# Iniciando o Cliente e Conectando a Nuvem:
def send_request(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_IP, SERVER_PORT))
        message = json.dumps(data)
        client.sendall(message.encode())
        response = receiveFullJson(client)
        print("Resposta da Nuvem:", json.dumps(response, indent=4))

# Exemplo de Mensagens de Teste:
def saveChargingStation(x, y):
    data = {
        "newChargingStation": True,
        "x_position": x,
        "y_position": y
    }
    send_request(data)

def saveChargingPoint(chargingStationID, power, price, availability):
    data = {
        "newChargingPoint": True,
        "chargingStationID": chargingStationID,
        "power": power,
        "kWhPrice": price,
        "availability": availability
    }
    send_request(data)

def receiveChargingPoints(chargingStationID):
    data = {
        "receiveAllChargingPoints": True,
        "chargingStationID": chargingStationID
    }
    send_request(data)

def receiveReservations(chargingStationID):
    data = {
        "receiveAllReservations": True,
        "chargingStationID": chargingStationID
    }
    send_request(data)

def updateChargingStationLocation(chargingStationID, x, y):
    data = {
        "updateChargingStation": True,
        "chargingStationID": chargingStationID,
        "x_position": x,
        "y_position": y
    }
    send_request(data)

def deleteChargingStation(chargingStationID):
    data = {
        "deleteChargingStation": True,
        "chargingStationID": chargingStationID
    }
    send_request(data)

def updateChargingPoint(chargingPointID, chargingStationID, power, price, availability):
    data = {
        "updateChargingPoint": True,
        "chargingPointID": chargingPointID,
        "chargingStationID": chargingStationID,
        "power": power,
        "kWhPrice": price,
        "availability": availability
    }
    send_request(data)

def deleteChargingPoint(chargingPointID, chargingStationID):
    data = {
        "deleteChargingPoint": True,
        "chargingPointID": chargingPointID,
        "chargingStationID": chargingStationID
    }
    send_request(data)

# Execução dos Testes:
if __name__ == "__main__":
    print("\nCadastrando um Posto de Recarga, no Banco de Dados da Nuvem, na Posição (5, 10):\n")
    saveChargingStation(5, 10)
    time.sleep(1)

    print("\nCadastrando um Posto de Recarga, no Banco de Dados da Nuvem, na Posição (10, 20):\n")
    saveChargingStation(10, 20)
    time.sleep(1)

    print("\nCadastrando um Ponto de Carregamento Para o Posto com ID '1':\n")
    saveChargingPoint(1, 30, 10, "livre")
    time.sleep(1)

    print("\nCadastrando um Ponto de Carregamento Para o Posto com ID '2':\n")
    saveChargingPoint(2, 60, 90, "livre")
    time.sleep(1)

    print("\nRecebendo Todos os Pontos de Carregamento do Posto com ID '1':\n")
    receiveChargingPoints(1)
    time.sleep(1)

    print("\nRecebendo Todos os Pontos de Carregamento do Posto com ID '2':\n")
    receiveChargingPoints(2)
    time.sleep(1)

    print("\nRecebendo Todos as Reservas Para o Posto com ID '1':\n")
    receiveReservations(1)
    time.sleep(1)

    print("\nRecebendo Todos as Reservas Para o Posto com ID '2':\n")
    receiveReservations(2)
    time.sleep(1)

    """ print("\nAtualizando a Localização do Posto com ID '1' para (40, 50):\n")
    updateChargingStationLocation(1, 40, 50)
    time.sleep(1)

    print("\nExcluindo o Posto com ID '2':\n")
    deleteChargingStation(2)
    time.sleep(1)

    print("\nAtualizando o Ponto de Carregamento '1' do Posto com ID '1':\n")
    updateChargingPoint(1, 1, 80, 40, "ocupado")
    time.sleep(1)

    print("\nExcluindo o Ponto de Carregamento '1' do Posto com ID '1':\n")
    deleteChargingPoint(1, 1)
    time.sleep(1) """
