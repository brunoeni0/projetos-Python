from cores import branco , amarelo
a = float(input('{}quantos metros de altura da parede?  '.format(amarelo)))
l = float(input('{}Quantos metros de largura da parede? '.format(amarelo)))
s = a * l
t = s / 2
print('{}Sua parede tem a dimensão  de {}x{} e sua área é de {}m².'.format(branco, a, l, s))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))