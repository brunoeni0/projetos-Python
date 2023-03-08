from cores import branco, amarelo, verde, roxo
nome = input('{}Digite seu nome completo '.format(branco))
letra = nome.split()
p = letra[0]
u = letra[len(letra) - 1]
print('{}Muito prazer em te conhecer!\n{} Seu primeiro nome é {} \n{} Seu último nome é {}'.format(verde, amarelo, p, roxo, u))
