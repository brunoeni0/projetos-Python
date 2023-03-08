from cores import amarelo,branco
d = float(input('{}Quanto de dinheiro você tem? R$ '.format(branco)))
dolar = d / 3.84
print('{}com {}{}{} você pode comprar US$ {}{:.2f}'.format(branco, amarelo, d, branco, amarelo, dolar))