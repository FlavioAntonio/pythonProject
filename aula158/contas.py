import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo = 0):
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


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo = 0,  limite = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"saque de {valor:.2f} realizado com sucesso")
            return self.saldo

        print("saldo insuficiente para saque")
        print(f'seu limite é {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        
        
if __name__ == "__main__":
    # cp1 = ContaPoupanca("0001", "12345-6", 1000)
    # cp1.sacar(500)
    # cp1.depositar(200)
    # print("*************************")
    cc1 = ContaCorrente("0001", "12345-6", 100, 100)

    print(cc1.saldo)
    cc1.sacar(250)

    #cc1.depositar(200)
    
        