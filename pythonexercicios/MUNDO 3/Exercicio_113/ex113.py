def leiaint(t):
    while True:
        try:
            r = int(input(t))
        except KeyboardInterrupt:
            print('\33[31mUsuário preferiu não digitar um número.\33[m')
            return 0
        except:
            print('\33[31mERRO! digite um número inteiro válido.\33[m')

        else:
            return r


def leiafloat(t):
    while True:
        try:
            r = float(input(t))
        except KeyboardInterrupt:
            print('\33[31mUsuário preferiu não digitar um número.\33[m')
            return 0
        except:
            print('\33[31mERRO! digite um número real válido.\33[m')
        else:
            return r


i = leiaint('Digite um número Inteiro: ')
f = leiafloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
