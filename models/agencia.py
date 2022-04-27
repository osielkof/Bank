class Agencia:
    
    codigo: int = 1000
    
    def __init__(self: object, nome: str) -> None:
        self.__numero: int = int(Agencia.codigo)
        self.__nome: str = nome
        Agencia.codigo += 1
    
    def __str__(self: object) -> str:
        return f'Número da Agencia: {self.numero} \nNome da Agência: {self.nome}'
        
    @property
    def numero(self: object) -> int:
        return Agencia.codigo
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self: object, nome: str) -> None:
        self.__nome: str = nome
 
                
    