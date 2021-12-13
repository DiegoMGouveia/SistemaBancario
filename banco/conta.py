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
        clear()
        """Metodo que receberá o valor(str), tratará para que seja um valor inteiro ou flutuante e somará como total"""
        deposito = get_num(valor)
        if deposito > 0:
            self._saldo += deposito
            print(f'Foi depositado R${deposito} na Conta Poupança: {self.conta}, Agencia: {self.agencia}')

    @saldo.setter
    def sacar(self, valor):
        clear()
        saque = get_num(valor)
        if (saque - self.saldo) < 0:
            print('Saldo insuficiente!')
        elif (saque - self.saldo) >= 0:
            self.saldo -= saque
            print(f'Você sacou {sacar}')


class ContaCorrente(Banco):
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
    def deposito(self, valor):
        clear()
        deposito = get_num(valor)
        if deposito > 0:
            self._saldo += deposito
            print(f'Foi depositado na Conta Corrente:{self.conta} da Agencia: {self.agencia} o valor de R${deposito}')
        else:
            print('O valor deve ser positivo para depositar!')

    @saldo.setter
    def sacar(self,valor):
        clear()
        saque = get_num(valor)
        if (self.saldo - saque) >= -300:
            self._saldo -= saque
            print(f'Foi sacado na Conta Corrente:{self.conta} da Agencia: {self.agencia} o valor de R${deposito}')
            if 0 > self.saldo:
                print('Cuidado, tu esta com saldo negativo.')
        else:
            print('A conta ja atingiu o limite de saque!')