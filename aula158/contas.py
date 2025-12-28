import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f"deposito {valor:.2f} realizado com sucesso")
        return self.saldo

    def detalhes(self, msg: str = "") -> None:
        print(f"o seu saldo é {self.saldo:.2f} {msg}")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"saque de {valor:.2f} realizado com sucesso")
            return self.saldo

        print("saldo insuficiente para saque")
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: int = 0, limite: int = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"saque de {valor:.2f} realizado com sucesso")
            return self.saldo
    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'{self.agencia!r}, {self.conta!r}, {self.saldo!r},'
                 f' {self.limite!r}')
        return f'{class_name}{attrs}'

        print("saldo insuficiente para saque")
        print(f'seu limite é {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        return self.saldo


if __name__ == "__main__":
    # cp1 = ContaPoupanca("0001", "12345-6", 1000)
    # cp1.sacar(500)
    # cp1.depositar(200)
    # print("*************************")
    cc1 = ContaCorrente(100, 123456, 100, 100)

    print(cc1.saldo)
    cc1.sacar(250)

    # cc1.depositar(200)
