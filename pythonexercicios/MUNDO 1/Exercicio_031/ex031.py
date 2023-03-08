from cores import verde,vermelho,amarelo
d = int(input('{}quantos km e a distancia da sua viagem? '.format(amarelo)))
p1 = 0.50 * d
p2 = 0.45 * d
if d < 200:
    print('{}Você vai paga {}'.format(verde, p1))
else:
    print('{}Você vai paga {}'.format(vermelho, p2))
