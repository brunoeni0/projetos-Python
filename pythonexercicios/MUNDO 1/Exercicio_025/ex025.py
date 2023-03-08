from cores import branco, vermelho, azul
a = input('{}Qual é seu nome completo? '.format(branco))
b = 'silva' in a.lower()
print('{}Seu nome tem Silva? {}{}'.format(vermelho, azul, b))
