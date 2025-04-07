# Nuvem Que Será Responsável por Reservar Recargas Para os Carros:

# O Tratamento de Concorrência é Feito por Threads, Pois Além de Serem Fáceis de Criar
# e Encerrar, Permitem Que o Programa Atenda a Várias Requisições ao Mesmo Tempo.

import socket
import json
import threading # Para Tratar a Concorrência de Requests.
from ChargingStationsFile import ChargingStationsFile
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