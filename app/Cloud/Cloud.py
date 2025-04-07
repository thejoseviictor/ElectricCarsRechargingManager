# Nuvem Que Será Responsável por Reservar Recargas Para os Carros:

import socket
import json
from ChargingStationsFile import ChargingStationsFile
from ReservationsFile import ReservationsFile

# Definindo o Host e Post da Nuvem:
HOST = "0.0.0.0" # Aceita Conexões de Qualquer Dispositivo na Rede.
PORT = 65432

# Garantindo Que o JSON Completo Seja Recebido:
def receiveFullJson(conn):
    buffer = b"" # Variável de Bytes Vazia, Onde os Dados, em Pedaços, Serão Salvos.
    # Loop de Recebimento do JSON Completo:
    while True:
        chunk = conn.recv(1024) # Recebendo os Dados em Partes de 1024 Bytes.
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

# Definindo o Socket da Nuvem:
cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Conexão TCP IPv4.
cloud.bind((HOST, PORT)) # Definindo o IP e porta do socket.

# Inicia uma Conexão, Lê Seus Dados, Fecha a Conexão e Aguarda uma Nova Conexão:
while True:
    # Ativando o Modo de Escuta da Nuvem:
    cloud.listen(1) # Escutando Com uma Fila de Tamanho "1".
    print(f"\nOuvindo na Porta '{PORT}'...\n")

    # Aceitando uma Conexão:
    conn, addr = cloud.accept()
    print(f"\nConectado a '{addr}'\n")

    # Mantendo no Loop Enquanto Dados do Dispositivo São Recebidos:
    while True:
        data = receiveFullJson(conn) # Recebendo os Dados do JSON Completos.
        if data:
            print(f"\nDados Recebidos de '{addr}': {data}\n")
            # Processamento de Mensagem Recebida de Veículo:
            # A Chave "vid" Identifica Mensagem Vinda de Veículo.
            if "vid" in data: # vid = Vehicle ID.
                # Criando uma Nova Reserva Para o Veículo:
                # Chaves Esperadas: "vid", "x", "y", "actualBatteryPercentage" e "batteryCapacity"
                if "actualBatteryPercentage" in data:
                    pass # Falta Fazer Ainda.
                # Retornando as Reservas do Veículo:
                # Chaves Esperadas: Apenas "vid"
                else:
                    reservations = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservations = reservations.findReservation(data["vehicleID"]) # Procurando a Reserva do Veículo.
                    if reservations:
                        # Respondendo Com a Reserva em JSON:
                        # Chaves Enviadas: "reservationID", "chargingStationID", 
                        # "chargingPointID", "chargingPointPower", "kWhPrice", 
                        # "vehicleID", "startDateTime", "finishDateTime", "duration" e "price"
                        reply = json.dumps(reservations, indent=4).encode('utf-8')
                        conn.sendall(reply)
                    # Respondendo Com o Texto "None" em uma String, Se Não Houverem Reservas Para o Veículo:
                    else:
                        conn.sendall(b"None")
                # Excluindo a Reserva do Veículo:
                # Chaves Esperadas: "reservationID", "vehicleID" e "deleteReservation".
                if "deleteReservation" in data:
                    reservations = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservations = reservations.deleteReservation(data["reservationID"], data["vehicleID"]) # Excluindo a Reserva.
                    # Reserva Excluida Com Sucesso:
                    if reservations:
                        conn.sendall(b"Sucesso")
                    # Reserva Não Encontrada:
                    else:
                        conn.sendall(b"None")
        # Finalizando, Se Não Houverem Dados:
        else:
            break

    # Fechando a Conexão com o Dispositivo:
    conn.close()
