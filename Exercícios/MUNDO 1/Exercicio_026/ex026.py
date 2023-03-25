from cores import azul, amarelo, branco, verde
a = input('{}Digite uma frase '.format(amarelo)).strip().lower()
b = a.count('a')
c = a.split()
d = c[0].capitalize()
e = a.rfind('a') + 1
print('{}A letra A aparece {} vezes na frase.'.format(branco, b))
print('{}A primeira letra A apareceu na posição {}'.format(azul, d.count('A')))
print('{}A última letra A apareceu na posição {}'.format(verde, e))
