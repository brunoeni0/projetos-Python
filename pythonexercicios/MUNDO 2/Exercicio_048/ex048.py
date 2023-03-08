soma = 0
cont = 0
for r in range(1, 501, 2):
    if r % 3 == 0:
        soma = soma + r
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
