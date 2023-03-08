cont1 = cont2 = cont3 = cont4 = 0
print('=' * 30)
print('         BANCO FTT         ')
print('=' * 30)
sacado = int(input('Que valor você quer sacar? R$'))
while True:
    if sacado >= 1:
        if sacado >= 50:
            sacado -= 50
            cont1 += 1
        if sacado < 50 and sacado >= 20:
            sacado -= 20
            cont2 += 1
        if sacado < 20 and sacado >= 10:
            sacado -= 10
            cont3 += 1
        if sacado < 10 and sacado >= 1:
            sacado -= 1
            cont4 += 1
    if sacado == 0:
        if cont1 > 0:
            print(f'Total de {cont1} cédulas de R$50')
        if cont2 > 0:
            print(f'Total de {cont2} cédulas de R$20')
        if cont3 > 0:
            print(f'Total de {cont3} cédulas de R$10')
        if cont4 > 0:
            print(f'Total de {cont4} cédulas de R$1')
    if sacado == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO FTT! Tenha um bom dia!')
