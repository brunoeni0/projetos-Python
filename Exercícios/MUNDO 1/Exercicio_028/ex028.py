from random import randint
from time import sleep
from cores import branco, vermelho, amarelo, limpa, azul, verde
print('{} advinha qual número eu estou pensado de 0 a 5'.format(amarelo))
b = int(input('{}Digite o número:'.format(verde)))
print('{}PROCESANDO...'.format(branco))
sleep(2)
a = randint(0, 5)
if b == a:
    print(azul, 'Vençeu')
else:
    print(vermelho, 'Perdeu')
print('\033[7;30m---------------------------FIM------------------------------', limpa)
