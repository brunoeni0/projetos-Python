def area(larg, comp):
    valor = larg * comp
    print(f'A área de um terreno é {l}x{c} é de {valor}²m')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
