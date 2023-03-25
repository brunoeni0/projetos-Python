from datetime import date

frase = 'Curso em Video Python'
frase[9:14]
frase[9:21]
frase[9:21:2]
frase[:5]
print(frase)

atual = date.today().year
a = (input('Digite algo: '))
print('olá {} o ano atual é {}'.format(a, atual))