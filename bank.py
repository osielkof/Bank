from models.agencia import Agencia
from models.cliente import Cliente
from models.conta import Conta

from datetime import date
from typing import List
from time import sleep

contas: List[Conta] = []
agencias: List[Agencia] = []


def main() -> None:
    menu()
    
def menu() -> None:
    print('================================')
    print('============  BANK  ============')
    print('================================')
    print('Informe a opção desejada')
    print('1 - Criar Agencia')
    print('2 - Criar Conta')
    print('3 - Saque')
    print('4 - Depósito')
    print('5 - Transferência')
    print('6 - Listar Contas')
    print('7 - Listar Agencias')
    print('8 - Sair do Programa')
    opcao = int(input())
    
    if opcao == 1:
        criar_agencia()
    elif opcao == 2:
        criar_conta()
    elif opcao == 3:
        efetuar_saque()
    elif opcao == 4:
        efetuar_deposito()
    elif opcao == 5:
        efetuar_transferencia()
    elif opcao == 6:
        listar_contas()
    elif opcao == 7:
        listar_agencias()
    elif opcao == 8:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida. Tente novamente.')
        sleep(2)
        menu()

def criar_agencia() -> None:
    nome: str = input('Informe o nome da nova agência: ')
    agencia: Agencia = Agencia(nome)
    agencias.append(agencia)
    print('Agência criada com sucesso!')
    print(agencia)
    sleep(3)
    menu()

def criar_conta() -> None:
    if len(agencias) > 0:
        print('Informe os dados do cliente ')
        print('----------------------------')
        
        nome: str = input('Nome do cliente: ')
        cpf: str = input('CPF do cliente: ')
        email: str = input('E-mail do cliente: ')
        data_nascimento: date = input('Data de nascimento do cliente: ')
        agencia : Agencia.nome = input('Informe o nome da agência: ')
        
        
        for agencia in agencias:
            if agencia in agencias:
                cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
                conta: Conta = Conta(cliente)
                contas.append(conta)
                print('Conta criada com sucesso!')
                print('Dados da conta')
                print('------------------------')
                print(conta)
                print('------------------------')
                break
                
            else:
               print(f'A agência {agencia} não está cadastrada.')   
    else:
        print('Não existem agências cadastradas')
        print('Cadastre uma agencia para abrir uma conta')
    sleep(5)
    menu()

def efetuar_saque() -> None:
    if len(agencias) >0:
        print('------------------------------')
        codigo: int = int(input('Número da agencia: '))
        agencia: Agencia = buscar_agencia_por_numero(codigo)
        
        if agencia:
            if len(contas) > 0:
                print('------------------------------')
                codigo: int = int(input('Número da conta: '))
                conta: Conta = buscar_conta_por_numero(codigo)
                
                if conta:
                    valor: int = int(input('Valor do saque: '))
                    print('------------------------------')
                    conta.sacar(valor)
                else:
                    print('Conta não encontrada')
                
            else:
                print('Não existem contas cadastradas')
        else:
            print('Agência não encontrada')
            
    else:
        print('Não existem agencias cadastradas')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(agencias) > 0:
        codigo: int = int(input('Código da agência: '))
        agencia: Agencia = buscar_agencia_por_numero(codigo)
    
        if agencia:
            if len(contas) > 0:
                codigo: int = int(input('Número da conta: '))
                conta: Conta = buscar_conta_por_numero(codigo)
                
                if conta:
                    valor: float = float(input('Valor do depósito: '))
                    conta.depositar(valor)
                else:
                    print('Conta não encontrada')   
            else:
                print('Não há contas cadastradas')        
        else:
            print('Agencia não encontrada')
      
    else:
        print('Não há agencias cadastradas')
    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    if len(agencias) > 0:
        cod_origem: int = int(input('Informe o código da sua agência: '))
        ag_origem: Agencia = buscar_agencia_por_numero(cod_origem)
        
        cod_destino: int = int(input('Informe o código da agencia destino: '))
        ag_destino: Agencia = buscar_agencia_por_numero(cod_destino)
        
        if ag_origem:
            if ag_destino:
                cont_origem: int = int(input('Informe o número da sua conta: '))
                conta_origem: Conta = buscar_conta_por_numero(cont_origem)
                
                cont_destino: int = int(input('Informe o número da conta destino: '))
                conta_destino: Conta = buscar_conta_por_numero(cont_destino)
                
                if conta_origem:
                    if conta_destino:
                        valor: float = float(input('Informe o valor da transferência: '))
                        conta_origem.transferir(conta_destino, valor)
                    else:
                        print('Conta destino não encontrada')
                else:
                    print('Sua conta não foi encontrada')
            else:
                print('Agênca de destino não encontrada')
        else:
            print('Sua agência não foi encontrada')
    else:
        print('Nenhuma agência cadastrada')
    sleep(2)
    menu()
    

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')
        for conta in contas:
            print('----------------------')
            print(conta)
        print('----------------------')
    else:
        print('Não existem contas cadastradas')
    sleep(2)
    menu()

def listar_agencias() -> None:
    if len(agencias) > 0:
        print('Lista de agências')
        for agencia in agencias:
            sleep(1)
            print('-------------------------')
            print(agencia)
        print('-------------------------')
    else:
        print('Não existem agências cadastradas.')
    sleep(2)
    menu()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    
    if len(contas) > 0:
        for conta in contas:
            if conta.codigo == numero:
                c = conta
    return c

def buscar_agencia_por_numero(numero: int) -> Agencia:
    a: Agencia = None
    
    if len(agencias) > 0:
        for agencia in agencias:
            if agencia.numero == numero:
                a = agencia
    return a 
    

if __name__ == "__main__":
    main()
