def contador(i, f, p):
    from time import sleep
    print('-=' * 20)
    if c < 0:
        print(f'Contagem de {a} até {b} de {-c} em {-c}')
    else:
        print(f'Contagem de {a} até {b} de {c} em {c}')
    for k in range(i, f, p):
        sleep(0.25)
        print(k, end=' ')
    print('Fim!')


a = 1
b = 10
c = 1
contador(a, b+1, c)
a = 10
b = 0
c = -2
contador(a, b-1, c)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c == 0:
    c = 1
if c > 0:
    if a > b:
        contador(a, b-1, -c)
    else:
        contador(a, b+1, c)
else:
    if a < b:
        contador(a, b+1, -c)
    else:
        contador(a, b-1, c)
