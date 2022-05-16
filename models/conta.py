import doctest
from models.cliente import Cliente


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
        """Função que adicionar o valor à conta de destino, caso o valor seja maior que 0.
        Caso contrário retorna erro.

        Returns:
            None: A função não retorna valor.
            Apenas informa se o depósito foi bem sucessido ou não.
        """
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')
        
    
    def sacar(self: object, valor: float) -> None:
        """Função que saca o valor solicitado, mas verifica se o saldo total é suficiente.
        Será utilizado o saldo em conta e o limite caso o saldo em conta não seja 
        suficiente.
        
        Returns:
            None: A função não retorna valor.
            Apenas informa se o saque foi bem sucessido ou não.
        """
        restante = 0
        self.saldo_total = self._calcula_saldo_total
        
        if valor > 0:
            if self.saldo_total >= valor:
                
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saldo_total = self._calcula_saldo_total            
                else:
                    self.saldo -= valor
                    restante = self.saldo
                    self.saldo = 0
                    self.limite += restante
                    self.saldo_total = self._calcula_saldo_total
                print('Saque efetuado com sucesso')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor inválido')
    
    def transferir(self: object, destino: object, valor: float) -> None:
        """Faz a transferência de uma conta para outra, desde que estejam cadastradas.
        A função verifica se a conta de origem possui o valor solicitado, utilizando tanto
        o saldo como o limite, e verifica se o valor é um número válido.
        
        Returns:
            None: A função não retorna valor.
            Apenas informa se a transferência foi bem sucessido ou não.
        """
        restante: float = 0.0
        if valor > 0:
            if self.saldo_total >= valor:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saldo_total = self._calcula_saldo_total
                    destino.saldo += valor
                else:
                    self.saldo -= valor
                    restante = self.saldo
                    self.saldo = 0
                    self.limite += restante
                    destino.saldo += valor
                print('Transferência bem sucedida')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor inválido')
        
    
    
    def __str__(self: object) -> str:
        return f'Nome: {self.cliente.nome} \nConta: {self.__codigo} \nSaldo: {self.saldo} \nLimite: {self.limite}'
 