novo = list()
while True:
    num = int(input("Digite um valor: "))
    if num not in novo:
        novo.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    p = 'pare'
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).upper()
    if p in 'N':
        break
novo.sort()
print('-=' * 30)
print(f'Você digitou os valores {novo}')
