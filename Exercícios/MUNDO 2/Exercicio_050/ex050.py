soma = 0
cont = 0
for k in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(k)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))