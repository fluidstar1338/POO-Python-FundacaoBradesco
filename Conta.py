class Conta:
    def __init__(self, titular, saldo, numero):
        self.saldo = 0
        self._titular = titular
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo nao pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self._saldo>=valor):
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print("Cliente: ",self._titular, "Saldo Atual",self._saldo)