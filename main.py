from banco.botoes import *

"""_ é uma variavel para usar em laços infinitos"""
_ = True

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
        pass
    elif botao_menu.botao0 == 3:
        print('\n'*150)
        print('Saindo...')
        break
