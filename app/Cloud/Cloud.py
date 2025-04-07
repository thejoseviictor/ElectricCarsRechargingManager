# Nuvem Que Será Responsável por Reservar Recargas Para os Carros:

# O Tratamento de Concorrência é Feito por Threads, Pois Além de Serem Fáceis de Criar
# e Encerrar, Permitem Que o Programa Atenda a Várias Requisições ao Mesmo Tempo.

import socket
import json
import threading # Para Tratar a Concorrência de Requests.
import datetime
import math # Para Calcular a Distância Entre o Veículo e o Posto de Recarga.
from ChargingStationsFile import ChargingStationsFile
from ChargingPointsFile import ChargingPointsFile
from ReservationsFile import ReservationsFile

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

# Atende ao Cliente, Lê os Dados Recebidos, Faz as Manipulações Necessárias no Banco de Dados, Envia a Resposta e Fecha a Conexão:
def handleClient(conn, addr):
    print(f"\nConectado a '{addr}'\n")
    # "try" e "finally" Para Garantir Que a Conexão Seja Encerrada ao Final, Mesmo Se Houverem Problemas:
    try:
        # Mantendo no Loop Enquanto Dados do Dispositivo São Recebidos:
        while True:
            data = receiveFullJson(conn) # Recebendo os Dados do JSON Completos.
            if data:
                print(f"\nDados Recebidos de '{addr}': {data}\n")
                # Processando Mensagem de Salvar Posto de Recarga no Banco de Dados, Recebida do Cliente "Posto de Recarga":
                if all(key in data for key in ["newChargingStation", "x_position", "y_position"]): # Verificando Se Todas as Chaves Estão Presentes.
                    cs = ChargingStationsFile() # Recuperando os Dados do Arquivo ".json".
                    cs.createChargingStation(data["x_position"], data["y_position"]) # Criando Posto de Recarga no Banco de Dados.

                # Processando Mensagem de Criar uma Reserva, Recebida do Cliente "Veículo":
                # Chaves Esperadas: "vid", "x", "y", "actualBatteryPercentage", "batteryCapacity" e "scheduleReservation".
                if all(key in data for key in ["vid", "x", "y", "actualBatteryPercentage", "batteryCapacity", "scheduleReservation"]): # vid = Vehicle ID.
                    # Calculando o Posto de Recarga Mais Próximo:
                    # Equação de Distância Entre Dois Pontos em um Plano Cartesiano:
                    # distância = sqrt((xP - xV​)² + (yP - yV​)²), Onde "xV" e "yV" São Coordenadas do Veículo e "xP" e "yP" São Coordenadas do Posto.
                    cs = ChargingStationsFile()
                    # Iniciando as Variáveis de Distância e ID do Posto de Recarga Encontrado:
                    shorterDistance = None
                    chargingStationID = None
                    # Comparando a Distância Entre os Posto de Recarga, Para Achar o Mais Próximo:
                    for station in cs.chargingStationsList:
                        distanceFromVehicle = math.sqrt((station["x_position"] - data["x"])**2 + (station["y_position"] - data["y"])**2)
                        if shorterDistance is None or distanceFromVehicle < shorterDistance:
                            shorterDistance = distanceFromVehicle # Atualizando a Distância do Mais Próximo.
                            chargingStationID = station["chargingStationID"] # Salvando o ID do Posto de Recarga Encontrado.

                    # AINDA FALTA FAZER:
                    # Calcular o Ponto de Carregamento Com Reserva Mais Cedo:
                    """ reservationList = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservationList = reservationList.listReservations(chargingStationID) # Lendo Reservas do Posto de Recarga Escolhido.
                    latestDateTime = datetime.datetime(2100, 12, 31, 0, 0, 0) # Data Base Mais Recente para Comparação.
                    found = False # Indicará Se um Data Anterior For Encontrada.
                    for reservation in reservationList:
                        dateTimeInFile = datetime.datetime.fromisoformat(reservation["finishDateTime"]) # Decodificando a Data na Lista para DateTime.
                        if dateTimeInFile < latestDateTime:
                            found = True # Alterando o Status de Data Posterior Encontrada.
                            latestDateTime = dateTimeInFile
                    chargingPointID = """


                    reservation = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservation.createReservation(chargingStationID, chargingPointID, data["vid"], data["actualBatteryPercentage"], data["batteryCapacity"])
                    # Respondendo Com a Reserva em JSON:
                    # Chaves Enviadas: "reservationID", "chargingStationID", 
                    # "chargingPointID", "chargingPointPower", "kWhPrice", 
                    # "vehicleID", "startDateTime", "finishDateTime", "duration" e "price"
                    reply = json.dumps(reservation, indent=4).encode('utf-8')
                    conn.sendall(reply)
                # Processando Mensagem de Procurar uma Reserva, Recebida do Cliente "Veículo":
                # Chaves Esperadas: "vid" e "findReservation"
                elif all(key in data for key in ["vid", "findReservation"]): # vid = Vehicle ID.
                    reservationsFile = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservation = reservationsFile.findReservation(data["vid"]) # Procurando a Reserva do Veículo.
                    if reservation:
                        # Respondendo Com a Reserva em JSON:
                        # Chaves Enviadas: "reservationID", "chargingStationID", 
                        # "chargingPointID", "chargingPointPower", "kWhPrice", 
                        # "vehicleID", "startDateTime", "finishDateTime", "duration" e "price"
                        reply = json.dumps(reservation, indent=4).encode('utf-8')
                        conn.sendall(reply)
                    # Respondendo Com o Texto "None" em uma String, Se Não Houverem Reservas Para o Veículo:
                    else:
                        conn.sendall(b"None")
                # Processando Mensagem de Excluir uma Reserva, Recebida do Cliente "Veículo":
                # Chaves Esperadas: "reservationID", "vehicleID" e "deleteReservation".
                elif all(key in data for key in ["reservationID", "vehicleID", "deleteReservation"]): # Verificando Se Todas as Chaves Estão Presentes.
                    reservationsFile = ReservationsFile() # Lendo as Reservas do Banco de Dados no Arquivo ".json"
                    reservationDeleted = reservationsFile.deleteReservation(data["reservationID"], data["vehicleID"]) # Excluindo a Reserva.
                    # Reserva Excluida Com Sucesso:
                    if reservationDeleted:
                        conn.sendall(b"Sucesso")
                    # Reserva Não Encontrada:
                    else:
                        conn.sendall(b"None")
                # Retornando a String "None" Se o Cliente Não Pediu Nada ou Faltaram Chaves no JSON:
                else:
                    conn.sendall(b"None")
            # Finalizando o Loop, Se Não Houverem Dados:
            else:
                break
    finally:
        # Fechando a Conexão com o Dispositivo:
        conn.close()
        print(f"\n{addr} Desconectado!\n")

# Inicia uma Conexão e Aguarda uma Nova Conexão:
def startCloud():
    # Definindo o Host e Post da Nuvem:
    HOST = "0.0.0.0" # Aceita Conexões de Qualquer Dispositivo na Rede.
    PORT = 65432

    # Definindo o Socket da Nuvem:
    cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Conexão TCP IPv4.
    cloud.bind((HOST, PORT)) # Definindo o IP e porta do socket.

    # Ativando o Modo de Escuta da Nuvem:
    cloud.listen(5) # Escutando Com uma Fila de Tamanho "5".
    print(f"\nOuvindo na Porta '{PORT}'...\n")
    
    # Aceitando as Conexões dos Clientes:
    while True:
        conn, addr = cloud.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        # Exibindo a Quantidade de Clientes Conectados:
        # "threading.active_count() - 1" Pois o Método Retorna a Thread Principal Também.
        print(f"'{threading.active_count() - 1}' Clientes Conectados no Momento.")

# Iniciando a Nuvem:
startCloud()