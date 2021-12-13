import os

clear = lambda: os.system('clear')


def get_num(valor):
    """recebe uma string e filtra todos numeros e transforma em um float"""
    y = ''
    for x in valor:
        if x.isnumeric() or x in '.':
            y += x
    if y == '':
        clear = lambda: os.system('clear')
        clear()
        print('Precisa digitar números para deposito.')
        return 0
    else:
        return float(y)


