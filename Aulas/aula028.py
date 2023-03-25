n = int(input('Digite um número: '))
f = 1
print('calculado o fatorial de {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(n), end='')
    f *= n
    n -= 1
    print(' x'if c > 1 else ' =', end=' ')
print(f)
