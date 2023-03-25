from random import choice
from cores import azulclaro
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
aluno = choice([n1, n2, n3, n4])
print('{}O aluno escolhido foi {}'.format(azulclaro, aluno))
