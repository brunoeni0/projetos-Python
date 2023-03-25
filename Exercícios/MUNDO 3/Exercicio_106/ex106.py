def comado(x):
    from time import sleep
    sleep(0.5)
    if x.lower() in 'fim':
        print('\033[30;41m', end='')
        print('~' * 15)
        print(f'{"ATÉ LOGO!":^15}')
        print('~' * 15)
        global pare
        pare = 0
    else:
        print('\033[30;44m', end='')
        print('~~' * 20)
        print(f'    Acessando o manual do comando \'{x}\'')
        print('~~' * 20)
        print('\033[m', end='')
        sleep(1)
        print('\033[1;37;40m', end='')
        help(x)
        print('\033[m', end='')
        sleep(2)


pare = 1
while pare == 1:
    print('\033[30;42m', end='')
    print('--' * 15)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('--' * 15)
    print('\033[m', end='')
    comado(input('Função ou Biblioteca > '))
