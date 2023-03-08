total = list()
for c in range(0, 5):
    total.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=' * 30)
print(f'Você digitou os valores {total}')
valor = total[:]
valor.sort()
maior = valor[-1]
menor = valor[0]
if total.count(maior) >= 2:
    print(f'O maior valor digitado foi {maior} nas posições', end=' ')
else:
    print(f'O maior valor digitado foi {maior} na posição', end=' ')
for k in range(0, 5):
    if total[k] == maior and total.count(maior) >= 2:
        print(f'{k}...', end=' ')
    elif total[k] == maior:
        print(f'{k}', end=' ')
print()
if total.count(menor) >= 2:
    print(f'O menor valor digitado foi {menor} nas posições', end=' ')
else:
    print(f'O menor valor digitado foi {menor} na posição', end=' ')
for x in range(0, 5):
    if total[x] == menor and total.count(menor) >= 2:
        print(f'{x}...', end=' ')
    elif total[x] == menor:
        print(f'{x}', end=' ')
