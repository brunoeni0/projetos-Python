from cores import azulclaro,branco
d =int(input('{}Quantos dias alugados? '.format(branco)))
k = float(input('{}Quantos Km rodados? '.format(branco)))
p1 = d * 60
p2 = k * 0.15
t = p1 + p2
print('{}O total a pagar é de {}'.format(azulclaro, t))