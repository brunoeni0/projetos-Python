from math import hypot
from cores import verde, amarelo, branco
co = float(input('{}Comprimento do cateto oposto: '.format(branco)))
ca = float(input('{}Comprimento do cateto adjacente: '.format(branco)))
hi = hypot(co,ca)
print('{}A hipotenusa vai medir {}{:.2f}'.format(verde, amarelo, hi))