import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor):
        ...
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"deposito {valor:.2f} realizado com sucesso")

    def detalhes(self, msg=""):
        print(f"o seu saldo é {self.saldo:.2f} {msg}")
        

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"saque de {valor:.2f} realizado com sucesso")
            return self.saldo
    
        print("saldo insuficiente para saque")
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        
        
if __name__ == "__main__":
    cp1 = ContaPoupanca("0001", "12345-6", 1000)
    cp1.sacar(500)
    cp1.depositar(200)
    
        