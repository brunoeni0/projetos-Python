casa = float(input('valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
a = salário - (salário * 70/100)
b = a * 12 * tempo
x = casa / tempo
z = x / 12
print('Para pagar uma casa de R${:.2f} em  anos {} a prestação será de R${:.2f}'.format(casa, tempo, z))
if b > casa:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
