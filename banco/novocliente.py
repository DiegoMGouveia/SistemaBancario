from pessoa import Cliente
from conta import ContaPoupanca
from random import randint


def criar_cliente():
    novo_cliente = Cliente()
    novo_cliente.criar_cliente(input("Digite seu nome: "), input("Digite sua idade: "))
    print(novo_cliente.nome)
    novo_cliente.contabancaria = ContaPoupanca()
    novo_cliente.contabancaria.agencia = 1494
    novo_cliente.contabancaria.conta = randint(1000, 9999)
    return novo_cliente


novo = criar_cliente()
print(f'nome: {novo.nome}, idade: {novo.idade}, Agencia: {novo.contabancaria.agencia}, Conta: {novo.contabancaria.conta}'
      f'saldo: {novo.contabancaria.saldo}')
