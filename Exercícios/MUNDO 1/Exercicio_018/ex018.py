from math import cos, sin, tan, radians
from cores import azul, amarelo, vermelho,branco
an = float(input('{}Digite o ângulo que você desejá: '.format(branco)))
co = cos(radians(an))
se = sin(radians(an))
ta = tan(radians(an))
print('{}O ângulo de {} tem o SENO de {:.2f}'.format( amarelo,an, se))
print('{}O ângulo de {} tem o COSSENO de {:.2f}'.format( azul,an, co))
print('{}O ângulo de {} tem a TANGENTE de {:.2f}'.format( vermelho,an, ta))
