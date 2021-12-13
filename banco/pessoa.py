from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self):
        self._nome = None
        self._idade = None
        self._contabancaria = None


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
            print('A idade precisa ser numérica!')

    @property
    def contabancaria(self):
        return self._contabancaria

    @contabancaria.setter
    def contabancaria(self, valor):
        self._contabancaria = valor

    def criar_cliente(self, nome, idade):
        self.nome = nome
        self.idade = idade


# novo = Cliente()
# novo.criar_cliente(nome='Diego', idade='31')
# novo.contabancaria = a
# print(novo.nome)
# print(novo.contabancaria.conta, novo.contabancaria.agencia, novo.contabancaria.saldo)

