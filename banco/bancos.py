from abc import ABC, abstractmethod


class Banco(ABC):
    _agencia = None
    _conta = None
    _saldo = 0

    @abstractmethod
    def agencia(self):
        pass

    @abstractmethod
    def conta(self):
        pass

    @abstractmethod
    def saldo(self):
        pass
        
