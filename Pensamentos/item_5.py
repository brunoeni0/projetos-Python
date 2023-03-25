lista = list()
lista1 = list()
lista2 = list()
for c in range(0, 9):
    if 3 > c >= 0:
        lista.append(int(input(f'Digite um valor para [0, {c}]: ')))
    elif 6 > c >= 3:
        lista1.append(int(input(f'Digite um valor para [1, {c-3}]: ')))
    else:
        lista2.append(int(input(f'Digite um valor para [2, {c-6}]: ')))
print('-=' * 30)
for k in range(0, 3):
    print(f'[{lista[k]:^5}]', end=' ')
print()
for k in range(0, 3):
    print(f'[{lista1[k]:^5}]', end=' ')
print()
for k in range(0, 3):
    print(f'[{lista2[k]:^5}]', end=' ')
