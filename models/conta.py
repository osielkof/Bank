from models.cliente import Cliente

class Conta:
    codigo = 000
    def __init__(self: object, cliente: Cliente) -> None:
        self.__cliente: Cliente = Cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total:float = self._calcula_saldo_total
        self.__codigo: int = int(Conta.codigo)
        Conta.codigo += 1
        
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
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite
    
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    
    def depositar(self: object, valor: float) -> None:
        pass
    
    def sacar(self: object, valor: float) -> None:
        pass
    
    def transferir(self: object, destino: object, valor: float) -> None:
        pass
    
    
    def __str__(self: object) -> str:
        return f'Nome: {Cliente.nome} \nConta: {self.codigo} \nSaldo: {self.saldo} Limite: {self.limite}'
 