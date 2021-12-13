class Menu:
    def __init__(self):
        self._botao0 = None
        self._botao1 = None
        self._botao2 = None

    @property
    def botao0(self):
        return self._botao0

    @botao0.setter
    def botao0(self, valor):
        if valor.isnumeric() and len(valor) == 1:
            self._botao0 = int(valor)
        else:
            print('digite uma opção válida.')

    @property
    def botao1(self):
        return self._botao1

    @botao1.setter
    def botao1(self, valor):
        if valor.isnumeric() and len(valor) == 1:
            self._botao1 = int(valor)
        else:
            print('digite uma opção válida.')

    @property
    def botao2(self):
        return self._botao1

    @botao1.setter
    def botao2(self, valor):
        if valor.isnumeric() and len(valor) == 1:
            self._botao2 = int(valor)
        else:
            print('digite uma opção válida.')

