sexo = int(input('Digite seu sexo: (1) Para homem (2) Para mulher: '))
peso = float(input('Digite sua altura: '))
if sexo == 1:
    homens = (72.7 * peso) - 58
    print(f'Seu peso ideal é {homens}')
elif sexo == 2:
    mulheres = (62.1 * peso) - 44.7
    print(f'Seu peso ideal é {mulheres}')
