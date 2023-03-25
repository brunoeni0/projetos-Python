listagem = ('leite', 3, 'arroz', 2.50, 'carne', 20, 'feijao', 8)
for k, c in enumerate(listagem):
    if k % 2 == 0:
        print(f'{c:.<30}', end='')
    else:
        print(f'{float(c):.2f}')
