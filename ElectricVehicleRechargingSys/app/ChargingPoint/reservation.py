from dataclasses import dataclass

from app.Vehicle.user import User

@dataclass
class Reservation:

    rid: str

    # Infos do veículo:
    vidInfo = str
    plateInfo: str
    valueService: float # Valor do serviço de carregamnto;
    finalPercentage: int # Porcentagem de energia ao final do carregamento;
    issueDate: str # Data do serviço;
    timeService: str # Hora do serviço.
    userInfos: User
    '''
    def __init__ (self, rid, vidInfo, plateInfo, valueInfo, finalPercentage):
        self.rid = rid
        self.vidInfo = vidInfo
        self.plateInfo = plateInfo
        self.valueService = valueService
        self.finalPercentage = finalPercentage
        self.issueDate = issueDate
        self.timeService = timeService


        
    '''

    def showReservation(self):
        
        print("\n -------------------- ")
        print("\n ID do veículo: {} ".format(self.vidInfo))
        print("\n Placa do veículo: {} ".format(self.plateInfo))
        print("\n CPF do proprietário: {} ".format(self.userInfos.cpf))
        print("\n Nome do proprietário: {} ".format(self.userInfos.name))
        print("\n Porcentagem final de carregamento: {} ".format(self.finalPercentage))
        print("\n Data do serviço: {} ".format(self.issueDate))
        print("\n Horário do serviço: {} ".format(self.timeService))
        print("\n Valor total do serviço: {} ".format(self.valueService))
        