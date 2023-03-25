from cores import limpa,branco,azul,roxo,verde
p = float(input('{}Coloque sua nota: '.format(verde)))
t = float(input('{}Coloque sua nota: '.format(roxo)))
n = p + t
r = n / 2
print('{}Sua média entre {}{}{} e {}{}{} é igual a {}{:.2}'.format(branco, azul, t, limpa, verde,p, branco, roxo, r))