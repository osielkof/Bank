from models.cliente import Cliente
from models.agencia import Agencia

class Conta:
    
    numero: int = 1010
    
    def __init__(self: object, cliente: Cliente) -> None:
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total:float = self._calcula_saldo_total
        self.__codigo: int = int(Conta.numero)
        Conta.numero += 1
    
    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self: object, valor:float) -> None:
        self.__saldo = valor
         
    @property
    def limite(self: object) -> float:
        return self.__limite
    
    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor
    
    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total
    
    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor
        
    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente
    
    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite
    
    @property
    def codigo(self: object) -> int:
        return self.__codigo    
    
    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')
        
    
    def sacar(self: object, valor: float) -> None:
        pass
    
    def transferir(self: object, destino: object, valor: float) -> None:
        pass
    
    
    def __str__(self: object) -> str:
        return f'Nome: {self.cliente.nome} \nConta: {self.__codigo} \nSaldo: {self.saldo} \nLimite: {self.limite}'
 