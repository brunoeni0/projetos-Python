peixes = int(input('Digito o numero de peixes pescados: '))
if peixes >= 50:
    taxa = (peixes - 50) * 4
    print(f'Você exedeu {peixes - 50} do numero permitido de peixes\nO valor de sua multa é de R${taxa}')
else:
    print('Você não exedeu o limite de peixes pescados')
