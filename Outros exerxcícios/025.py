num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    print('\033[30m', end=' ')
    if num % c == 0:
        cont += 1
        print('\033[34m', end='')
    print(c, end='')
if cont == 2:
    print('\033[m \n O número {} foi divisível {} vezes \n E por isso ele É PRIMO!'.format(num, cont))
else:
    print('\033[m \n O número {} foi divisível {} vezes \n E por isso ele Não É PRIMO!'.format(num, cont))
