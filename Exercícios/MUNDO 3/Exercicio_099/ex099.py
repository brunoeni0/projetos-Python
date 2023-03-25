from random import randint
numeros = list()


def maior(n):
    from time import sleep
    for c in range(0, n):
        print('-=' * 25)
        print('Analizando os valores passados...')
        a = randint(0, 10)
        for k in range(0, a):
            numeros.append(randint(1, 10))
            sleep(0.1)
            print(numeros[k], end=' ')
        print(f'Foram informados {len(numeros)} valores ao todo.')
        if a > 0:
            print(f'O maior valor informado foi {max(numeros)}')
        else:
            print(f'O maior valor informado foi 0')
            break
        numeros.clear()


maior(randint(1, 10))
