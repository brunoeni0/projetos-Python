from random import shuffle
from cores import branco
n1 = input('{}Primeiro aluno: '.format(branco))
n2 = input('{}Segundo aluno: '.format(branco))
n3 = input('{}Terceiro aluno: '.format(branco))
n4 = input('{}Quarto aluno: '.format(branco))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('\033[33m', nomes)
