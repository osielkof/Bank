import unittest


from models.cliente import Cliente
from models.conta import Conta
from models.agencia import Agencia

class ContaTest(unittest.TestCase):
    
    def setUp(self: object) -> None:
        self.cliente: Cliente = Cliente('João Silva', 'joao@gmail.com', '123.456.789-01', '17/05/2000')
        self.cliente2: Cliente = Cliente('Marcelo Santos', 'marcelo@gmail.com', '741.258.963-98', '18/01/1995')
        self.conta: Conta = Conta(self.cliente)
        self.conta2: Conta = Conta(self.cliente2)
        self.agencia: Agencia = Agencia('Tatuape')
        self.agencia2: Agencia = Agencia('Carrao')
        
        
    def test_depositar(self: object) -> None:
        self.conta.depositar(130.00)
        self.assertEqual(self.conta.saldo, 130.00)
        
    def test_sacar(self: object) -> None:
        self.conta.sacar(30.00)
        self.assertEqual(self.conta.saldo, 0.0)
        self.assertEqual(self.conta.limite, 70.00)
        self.assertEqual(self.conta.sacar(110.00), None)
    
    def test_transferir(self: object) -> None:
        self.conta.depositar(130.00)
        self.conta.transferir(self.conta2, 100)
        self.assertEqual(self.conta2.saldo, 100)
        
    def tearDown(self) -> None:
        None
        
    
if __name__ == "__main__":
    unittest.main()
