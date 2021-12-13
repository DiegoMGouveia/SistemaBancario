from banco.botoes import *
from banco.novocliente import criar_cliente

"""_ é uma variavel para usar em laços infinitos"""
_ = True
clear = lambda: os.system('clear')

clear()

botao_menu = Menu()
while _:
    """Inicio do programa"""
    print('Seja bem-vindo caro cliente, em que posso ser util?')
    botao_menu.botao0 = input("""
[1] Login
[2] Criar conta
[3] Sair

Digite sua [opção]: """)
    if botao_menu.botao0 == 1:
        pass
    elif botao_menu.botao0 == 2:
        while _:
            botao_menu.botao1 = input("""
[1] Conta Poupança
[2] Conta Corrente
[3] Sair

Digite sua [opção]: """)
            if botao_menu.botao1 == 1:

                nova_conta = criar_cliente()

    elif botao_menu.botao0 == 3:
        print('\n'*150)
        clear()
        print('Saindo...')
        break

    else:
        clear()
        print('!!!ATENÇÃO!!!\n\ndigite uma opção válida.\n\n')

