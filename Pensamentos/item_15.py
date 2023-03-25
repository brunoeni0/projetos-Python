total = []
for n, c in enumerate(range(0, 5)):
    num = int(input(f'Digite um valor para posição {n}: '))
    total.append(num)
    if n == 0:
        maior = num
        menor = num
        pos1 = pos2 = pos3 = pos4 = r1 = r2 = n
    if num > maior:
        maior = num
        pos1 = n
    elif maior == num and n != 0:
        r1 = num
        pos3 = n
    if num < menor:
        menor = num
        pos2 = n
    elif menor == num and n != 0:
        r2 = num
        pos4 = n
print('=-=-=' * 15)
print(f'Você digitou os valores {total}')
if maior == r1:
    print(f'O maior valor digitado foi {maior} nas posições {pos1}...{pos3}...')
else:
    print(f'O maior valor digitado foi {maior} na posição {pos1}...')
if menor == r2:
    print(f'O menor valor digitado foi {menor} nas posições {pos2}...{pos4}...')
else:
    print(f'O menor valor digitado foi {menor} na posição {pos2}...')
