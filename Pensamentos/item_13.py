numeros = list()


def maior():
    from random import randint
    for c in range(0, randint(1, 10)):
        print('-=' * 25)
        print('Analizando os valores passados...')
        for k in range(0, randint(1, 10)):
            numeros.append(randint(0, 10))
            print(numeros[k], end=' ')
        print(f'Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior valor informado foi {max(numeros)}')
        numeros.clear()

maior()
