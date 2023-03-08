c = 1
s = 0
while c != 0:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
        c -= 1
        print('Sexo F registrado com sucesso')
    elif sexo == 'M':
        c -= 1
        print('Sexo M registrado com sucesso')
    else:
        print('Dados inválidos. Por favor,', end=' ')
