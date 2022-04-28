from datetime import date
from utils.helper import date_para_str

class Cliente:
    codigo: int = 100
    
    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: str = data_nascimento
        self.__codigo: int = int(Cliente.codigo)
        self.__cadastro: date = date.today()
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
    def cadastro(self: object) -> date:
        return date_para_str(self.__cadastro)
    
    
    def __str__(self: object) -> str:
        return f'Nome: {self.nome} \nE-mail: {self.email} \nData de nascimento: {self.data_nascimento} \nCadastro: {self.cadastro}'
    