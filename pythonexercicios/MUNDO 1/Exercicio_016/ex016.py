from cores import branco,azulclaro
'''from math import floor,trunc,ceil
num = float(input('Digite um número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,floor(num)))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,ceil(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))'''

num = float(input('{}Digite um número: '.format(azulclaro)))
print('{}O valor digitado foi {} e a sua porção inteira é {}'.format(branco, num, int(num)))