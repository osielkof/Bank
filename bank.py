from datetime import date
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
     

    

def criar_conta() -> None:
    print('Informe os dados do cliente')
    nome: str = input('Nome do cliente: ')
    cpf: str = input('CPF do cliente')
    email: str = input('E-mail do cliente: ')
    data_nascimento: date = input('Data de nascimento do cliente: ')
    
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    
    contas.append(conta)
    

def efetuar_saque(valor: float) -> None:
    pass

def efetuar_deposito(valor: float) -> None:
    pass

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')
        for conta in contas:
            print('----------------------')
            print(conta)
        print('----------------------')
    else:
        print('Não existem contas cadastradas')

def listar_agencias() -> None:
    if len(agencias) > 0:
        print('Lista de agências')
        for agencia in agencias:
            print('-------------------------')
            print(agencia)
        print('-------------------------')
    else:
        print('Não existem agências cadastradas.')
