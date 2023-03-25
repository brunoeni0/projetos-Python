num = int(input('Digite um número para ver sua tabuada: '))
for x in range(num, num * 11, num):
    print('{} x {} = {}  '.format(num, x // num, x))
