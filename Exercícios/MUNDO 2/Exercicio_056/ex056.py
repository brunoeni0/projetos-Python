idade = 0
velho = 0
cont = 0
media = 0
for c in range(0, 4):
    print('XXXXX {}ª PESSOA XXXXX'.format(c + 1))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()
    media += i / 4
    if c == 0 and s == 'M':
        idade = i
        velho = n
    if s == 'M' and i > idade:
        velho = n
        idade = i
    if s == 'F' and i < 20:
        cont += 1
print(f'''A média de idade do grupo é de {media} anos
O homem mais velho tem {idade} anos e se chama {velho}.
Ao todo são {cont} mulheres com menos de 20 anos''')
