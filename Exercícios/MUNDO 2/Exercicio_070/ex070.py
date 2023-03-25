total = caro = probarato = cont = barato = 0
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    final = ' '
    while final not in 'SN':
        cont += 1
        final = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    total += preço
    if preço >= 1000:
            caro += 1
    if cont == 1 or preço < barato:
        barato = preço
        probarato = produto
    if final == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'''O total da compra foi R${total:.2f}
Temos {caro} produtos custando mais de R$1000.00
O produto mais barato foi {probarato} que custa R${barato:.2f}''')
