from datetime import date
hoje = date.today().year
nasc = int(input('Ano de Nascimento: '))
n = hoje - nasc
print('O atleta tem {} anos.'.format(n))
if n <= 9:
    print('Classificação: MIRIM')
elif n <= 14:
    print('Classificação: INFANTIL')
elif n <= 19:
    print('Classificação: JUNIOR')
elif n <= 25:
    print('Classificação: SÊNIO')
else:
    print('Classificação: MASTER')
