media = 0
velho = 0
cont = 0
idoso = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if idade:
        media += idade / 4
    if sexo in 'Mm':
        velho = idade
        idoso = nome
        if velho < idade:
            velho = idade
            idoso = nome
    if sexo in 'Ff':
        if idade <= 20:
            cont += 1
print('''A média de idade do grupo é de {} anos
O homem mais velho tem {} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos'''.format(media, velho, idoso, cont))
