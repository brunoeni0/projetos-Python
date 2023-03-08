contM = cont = contF = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    fim = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while fim not in 'SN':
        fim = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if sexo == 'M':
        contM += 1
    if idade > 18:
        cont += 1
    if sexo == 'F':
        if idade < 20:
            contF += 1
    if fim == 'N':
            break
print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {cont}
Ao todo temos {contM} homens cadastrados
E temos {contF} mulheres com menos de 20 anos''')
