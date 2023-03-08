lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    p = 'pare'
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).upper()
    if p in 'N':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) == 1:
    print(f'O valor 5 faz parte da lista! Na posição', end=' ')
elif lista.count(5) > 1:
    print(f'O valor 5 faz parte da lista! Nas posições', end=' ')
else:
    print('O valor 5 não foi encontrado na lista!')
for c in range(0, len(lista)):
    if lista[c] == 5:
        print(f'{c}...', end=' ')
