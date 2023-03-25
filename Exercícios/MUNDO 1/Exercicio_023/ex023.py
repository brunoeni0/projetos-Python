from cores import azul, amarelo ,azulclaro , vermelho, branco, verde
num =int(input('{}Imforme um número: '.format(branco)))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{}Analizando {}'.format(vermelho, num))
print('{}Unidade: {}'.format(azul, u))
print('{}Dezena: {}'.format(amarelo, d))
print('{}Centena: {}'.format(verde, c))
print('{}Milhar: {}'.format(azulclaro, m))
