from models.agencia import Agencia
from models.cliente import Cliente
from models.conta import Conta

from typing import List

contas: List[Conta] = []
agencias: List[Agencia] = []


def criar_agencia() -> None:
    nome: str = input('Informe o nome da nova agência: ')
    agencia: Agencia = Agencia(nome)
    agencias.append(agencia)
    print('Agência criada com sucesso!')
    
    

def listar_agencias() -> None:
    if len(agencias) > 0:
        print('Lista de agências')
        for agencia in agencias:
            print('-------------------------')
            print(agencia)
        print('-------------------------')
    else:
        print('Não existem agências cadastradas.')
    

def criar_conta() -> None:
    pass

def listar_contas() -> None:
    pass





