pessoas = list()
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    for p in range(0, len(pessoas)):
        if p % 2 == 1:
            if p == 1:
                maior = menor = pessoas[p]
            elif menor > pessoas[p]:
                menor = pessoas[p]
            elif maior < pessoas[p]:
                maior = pessoas[p]
    pare = str(input('Quer continuar? [S/N] ')).upper()
    while pare not in 'SN':
        pare = str(input('Quer continuar? [S/N] ')).upper()
    if pare in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {int(len(pessoas) / 2)} pessoas.')
if len(pessoas) / 2 == 1:
    print(f'Ao todo, você cadastrou {int(len(pessoas) / 2)} pessoa.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for n in range(0, len(pessoas)):
    if pessoas[n] == maior:
        print(f'[{pessoas[n-1]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg.Peso de', end=' ')
for n in range(0, len(pessoas)):
    if pessoas[n] == menor:
        print(f'[{pessoas[n-1]}]', end=' ')
