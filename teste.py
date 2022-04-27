from re import A
from models.cliente import Cliente
from models.agencia import Agencia
from bank import criar_agencia
from bank import listar_agencias

#criar_agencia()
#listar_agencias()



agencia1: Agencia = Agencia('Tatuapé')

cli1: Cliente = Cliente('João da Silva', 'joaosilva@gmail.com', '123.456.789-01', '25/04/1994')

#print(agencia1)
print(cli1)

