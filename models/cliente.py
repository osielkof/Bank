from datetime import date
from datetime import datetime

class Cliente:
    codigo: int = 100
    
    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: str = data_nascimento
        self.__codigo: int = Cliente.codigo
        self.__cadastro: date = datetime.today()
        Cliente.codigo += 1
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def email(self: object) -> str:
        return self.__email
    
    @property
    def cpf(self: object) -> str:
        return self.__cpf
    
    @property
    def data_nascimento(self: object) -> str:
        return self.__data_nascimento
    
    @property
    def cadastro(self: object) -> datetime:
        return self.__cadastro
    
    def __str__(self: object) -> str:
        return f'Código: {self.__codigo} \nNome: {self.nome} \nE-mail: {self.email} \nCPF: {self.cpf} \n'\
            f'Data de nascimento: {self.data_nascimento} \nCadastro: {self.cadastro}'
