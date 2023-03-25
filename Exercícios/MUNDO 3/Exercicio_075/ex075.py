a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
total = (a, b, c, d)
print(f'Você digitou os valores {total}')
print('O valor 9 apareceu {} vezes'.format(total.count(9)))
if total.count(3) >= 1:
    print('O valor 3 apareceu na {}ª posição'.format(total.index(3) + 1))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0 or d % 2 == 0:
    print('Os valores pares digitados foram ', end='')
    if a % 2 == 0:
        print(a, end=' ')
    if b % 2 == 0:
        print(b, end=' ')
    if c % 2 == 0:
        print(c, end=' ')
    if d % 2 == 0:
        print(d)
