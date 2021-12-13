from banco.funcoes import *
from banco.bancos import *


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
        clear = lambda: os.system('clear')
        if valor > self.saldo:
            clear()
            print('Saldo insuficiente.')
        elif valor <= self.saldo:
            self.saldo -= valor

