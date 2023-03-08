from cores import vermelho, verde, azul, roxo
p = float(input('{}Qual é o preço do produto? R$ '.format(vermelho)))
s =p - (p * 5 / 100)
print('{}O produto custava R${}{:.2f}{},na promoção com desconto de 5% vai custar {}{:.2f}'.format(verde, roxo, p, verde, azul, s))