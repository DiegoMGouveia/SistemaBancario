from abc import ABC, abstractmethod
import os


class Pessoa(ABC):
    @abstractmethod
    def __init__(self):
        self._nome = str
        self._idade = int
        self._conta_poupanca = None
        self._conta_corrente = None

    @property
    def conta_poupanca(self):
        return self._conta_poupanca


class Cliente(Pessoa):
    def __init__(self):
        super().__init__()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor.isnumeric():
            self._idade = valor
        else:
            clear()
            print('A idade precisa ser numérica!')

    @property
    def conta_poupanca(self):
        return self._conta_poupanca

    @conta_poupanca.setter
    def conta_poupanca(self, valor):
        self._conta_poupanca = valor

    @property
    def conta_corrente(self):
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, valor):
        self._conta_corrente = valor

    def criar_cliente(self, nome, idade):
        self.nome = nome
        self.idade = idade


