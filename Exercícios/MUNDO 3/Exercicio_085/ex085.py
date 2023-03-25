lista = list()
for c in range(0, 7):
    lista.append(int(input(f'Digite o {c+1}o. Valor: ')))
lista.sort()
print('-=' * 30)
print('Os valores pares digitados foram:', end=' ')
for n in range(0, 7):
    if lista[n] % 2 == 0:
        print(lista[n], end=' ')
print()
print('Os valores ímpares digitados foram:', end=' ')
for n in range(0, 7):
    if lista[n] % 2 == 1:
        print(lista[n], end=' ')
