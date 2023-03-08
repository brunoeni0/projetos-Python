from cores import branco, azul
c = float(input('{}Informe a temperatura em °C: '.format(azul)))
a = 9 * c / 5 + 32
print('{}A temperatura de {}{:.2f}{}°C coresponde a {}{:.2f}{}°f'.format(branco, azul, c, branco, azul, a, branco))