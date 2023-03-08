matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = tsoma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l][c] == matriz[l][-1]:
            tsoma += matriz[l][-1]
        if matriz[l][c] == matriz[1][0] or maior < matriz[1][c]:
            maior = matriz[1][c]
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {tsoma}.')
print(f'O maior valor da segunda linha é {maior}.')
