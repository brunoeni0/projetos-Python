lista = list()
par = list()
impa = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impa.append(num)
    p = 'pare'
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).upper()
    if p in 'N':
        break
lista.sort()
par.sort()
impa.sort()
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impa}')
