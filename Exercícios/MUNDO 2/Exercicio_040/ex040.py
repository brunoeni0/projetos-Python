n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
s = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, s))
if s >= 7.0:
    print('O aluno está Aprovado.')
elif s >= 5.0 and s < 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')
