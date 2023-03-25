c = 'S'
media = cont = maior = 0
menor = 999999999999999
while c == 'S':
    num = int(input('Digite um número: '))
    media += num
    cont += 1
    c = str(input('Quer continaur? [S/N] ')).upper().strip()
    if num > maior:
        maior = num
        if maior < num:
            maior = num
    if num < menor:
        menor = num
        if menor > num:
            menor = num
print('''Você digitou {} números e a média foi {}
O maior valor foi {} e o menor foi {}'''.format(cont, (media / cont), maior, menor))
