from cores import amarelo, azul, verde
from time import sleep
nome = input('{}Qual é seu nome? '.format(amarelo)).strip()
ma = nome.upper()
mi = nome.lower()
l = len(nome) - nome.count(' ')
a = nome.split()
b = len(a[0])
print('{}Analizando seu nome...'.format(verde))
sleep(2)
print('{}Seu nome em maiúsculas é {} \n{}Seu nome em minúsculas é {}'.format(azul, ma, amarelo, mi))
print('{}Seu nome tem ao todo {} letras'.format(verde, l))
print('{}Seu primeiro nome é {} e ele tem {} letras'.format(azul, a[0], b))
