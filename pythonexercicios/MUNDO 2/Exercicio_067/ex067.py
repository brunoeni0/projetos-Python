tab = int(input('Digite um valor para ver a tabuada: '))
cont = 0
soma = 0
print('-' * 30)
while True:
    if tab < 0:
        break
    cont += 1
    soma = tab * cont
    print(f'{tab} x {cont} = {soma}')
    if cont == 10:
        cont -= 10
        print('-' * 30)
        tab = int(input('Digite um valor para ver a tabuada: '))
        print('-' * 30)
print('PPOGRAMA TABUADA ENCERRADO. Volte sempre!')
