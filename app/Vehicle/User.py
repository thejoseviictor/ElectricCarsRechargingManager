from dataclasses import dataclass

@dataclass
class User:

    cpf: str
    name: str
    email: str
    password: str
