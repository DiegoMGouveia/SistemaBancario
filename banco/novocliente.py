from banco.pessoa import *
from banco.conta import *
from random import randint
import os


def criar_cliente():
    clear = lambda: os.system('clear')
    novo_cliente = Cliente()
    clear()
    print('CRIANDO CLIENTE: (Nome e Idade)')
    novo_cliente.criar_cliente(nome=input("Digite seu nome: "), idade=input("Digite sua idade: "))
    clear()
    print(novo_cliente.nome)
    novo_cliente.contabancaria = ContaPoupanca()
    novo_cliente.contabancaria.agencia = 1494
    novo_cliente.contabancaria.conta = randint(1000, 9999)
    print('-'*len(novo_cliente.nome))
    print(f'Agencia: {novo_cliente.contabancaria.agencia}\nConta: {novo_cliente.contabancaria.conta}\nSaldo: {novo_cliente.contabancaria.saldo}')
    print('ANOTE SEUS DADOS!')

    return novo_cliente


