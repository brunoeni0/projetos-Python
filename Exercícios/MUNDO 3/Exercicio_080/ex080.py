lista = list()
count = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or lista[-1] <= num:
        print('Adicionado ao final da lista...')
        lista.append(num)
    else:
        while True:
            count += 1
            if lista[0] > num:
                lista.insert(0, num)
                print('Adicionado na posição 0 da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
