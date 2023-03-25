produto = ('pães', '1.50', 'feijão', '8.00', 'salgadinho', '2.25', 'detegente', '1.25', 'arroz', '2.00', 'carne', '25.00', 'miojo', '0.50', 'leite', '3.00', 'ovos', '6.00')
print('--' * 20)
print('         LISTAGEM DE PREÇOS')
print('--' * 20)
for c in range(0, 18):
    if c % 2 == 0:
        print(f'{produto[c]:.<30}', end='')
    else:
        print(f'R${produto[c]: >6}')
#print(f'''{produto[0]:.<30}R${produto[1]: >6}
#{produto[2]:.<30}R${produto[3]: >6}
#{produto[4]:.<30}R${produto[5]: >6}
#{produto[6]:.<30}R${produto[7]: >6}
#{produto[8]:.<30}R${produto[9]: >6}
#{produto[10]:.<30}R${produto[11]: >6}
#{produto[12]:.<30}R${produto[13]: >6}
#{produto[14]:.<30}R${produto[15]: >6}
#{produto[16]:.<30}R${produto[17]: >6}''')
print('--' * 20)