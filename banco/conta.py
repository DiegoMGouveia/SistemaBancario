from funcoes import get_num
from bancos import Banco


class ContaPoupanca(Banco):
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        self._agencia = valor

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, valor):
        self._conta = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def depositar(self, valor):
        """Metodo que receberá o valor(str), tratará para que seja um valor inteiro ou flutuante e somará como total"""
        deposito = get_num(valor)
        self._saldo += deposito

    @saldo.setter
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        elif valor <= self.saldo:
            self.saldo -= valor



# a = ContaPupanca()
# a.criar_conta(agencia=1494, conta=randint(10000, 99999))
# a.depositar = '50'
# print(a.conta, a.agencia, a.saldo)
