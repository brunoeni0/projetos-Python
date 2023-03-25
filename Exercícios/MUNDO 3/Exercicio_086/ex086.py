matriz = list()
for c in range(0, 3):
    for k in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{c}, {k}]: ')))
print('-=' * 30)
for x in range(0, 9):
    if x == 3 or x == 6:
        print()
    print(f'[{matriz[x]:^5}]', end='')
