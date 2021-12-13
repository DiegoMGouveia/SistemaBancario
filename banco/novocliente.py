from banco.pessoa import *
from banco.conta import *
from random import randint


def criar_poupanca():
    novo_cliente = Cliente()
    clear()
    print('CADASTRANDO CLIENTE: (Nome e Idade)')
    novo_cliente.criar_cliente(nome=input("Digite seu nome: "), idade=input("Digite sua idade: "))
    clear()
    novo_cliente.conta_poupanca = ContaPoupanca()
    novo_cliente.conta_poupanca.agencia = 1494
    novo_cliente.conta_poupanca.conta = randint(1000, 9999)
    clear()
    print('-'*len(novo_cliente.nome))
    print(f'''Tu agora tens uma conta Poupança!
---------------------------------
ANOTE SEUS DADOS!
-----------------
Titular: {novo_cliente.nome}
Idade: {novo_cliente.idade}
Agencia: {novo_cliente.conta_poupanca.agencia}
Conta Poupança: {novo_cliente.conta_poupanca.conta}
Saldo: {novo_cliente.conta_poupanca.saldo}
--------------
''')
    o = input('Aperte ENTER depois de copiar os dados')
    return novo_cliente


def criar_corrente():
    novo_cliente = Cliente()
    clear()
    print('CADASTRANDO CLIENTE: (Nome e Idade)')
    novo_cliente.criar_cliente(nome=input("Digite seu nome: "), idade=input("Digite sua idade: "))
    clear()
    novo_cliente.conta_corrente = ContaCorrente()
    novo_cliente.conta_corrente.agencia = 1494
    novo_cliente.conta_corrente.conta = randint(1000, 9999)
    clear()
    print('-'*len(novo_cliente.nome))
    print(f'''Tu agora tens uma conta Corrente!
---------------------------------
ANOTE SEUS DADOS!
-----------------
Titular: {novo_cliente.nome}
Idade: {novo_cliente.idade}
Agencia: {novo_cliente.conta_corrente.agencia}
Conta Corrente: {novo_cliente.conta_corrente.conta}
Saldo: {novo_cliente.conta_corrente.saldo}
--------------
''')
    o = input('Aperte ENTER depois de copiar os dados')
    return novo_cliente


