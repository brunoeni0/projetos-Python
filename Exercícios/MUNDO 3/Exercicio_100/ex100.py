numeros = list()


def sorteia():
    from random import randint
    from time import sleep
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        sleep(0.5)
        print(numeros[c], end=' ')
    print('PRONTO!')


def somapar():
    par = 0
    for k in numeros:
        if k % 2 == 0:
            par += k
    print(f'Somando os valores pares de {numeros}, temos {par}')


sorteia()
somapar()
