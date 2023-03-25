print('{} Mercadinho do lar {}'.format('-+-' * 10, '-+-' * 10))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
paga = int(input('Qual é a opção? '))
if paga == 4:
    parcelas = int(input('Quantas parcelas? '))
if paga == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - preço * 10 / 100))
elif paga == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - preço * 5 / 100))
elif paga == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preço / 2))
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preço, preço))
elif paga == 4:
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, ((preço + preço * 20 / 100) / parcelas)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço + preço * 20 / 100))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
