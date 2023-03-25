from cores import branco, vermelho, amarelo, roxo
n1 = int(input('{}Digite um número: '.format(amarelo)))
n2 = int(input('{}Digite outro: '.format(roxo)))
s = n1 + n2
print('{}A soma entre {}{}{} e {}{}{} é igual a {}{}{}!'.format(branco, amarelo, n1, branco, vermelho, n2, branco, roxo, s, branco))
