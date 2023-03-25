def contador(i, f, p):
    print('-=' * 15)
    print(f'Contagem de {i} até {f-1} de {p} em {p}')
    for k in range(i, f, p):
        print(k, end=' ')
    print('Fim!')


contador(1, 11, 1)
contador(10, 0, -2)
print('-=' * 15)
print(f'Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input(f'passo: '))
if c > 0:
    if a < b:
        contador(a, b+1, c)
    else:
        contador(a, b-1, -c)
elif c == 0:
    if a < b:
        c = 1
        contador(a, b + 1, c)
    else:
        c = -1
        contador(a, b - 1, c)
else:
    if a < b:
        contador(a, b+1, c)
    else:
        contador(a, b - 1, c)
