count = 0
list = []
while True:
    num = int(input('Digite um valor: '))
    count += 1
    list.append(num)
    if num == 5:
        pos = count
    p = 'pare'
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).upper()
    if p in 'N':
        break
list.sort(reverse=True)
print(f'Você digitou {count} elementos.')
print(f'Os valores em ordem decrescente são {list}')
if list.count(5):
    print(f'O valor 5 faz parte da lista! Na posição {pos}')
else:
    print('O valor 5 não foi encontrado na lista!')
