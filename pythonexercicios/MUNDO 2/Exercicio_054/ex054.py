from datetime import date
date = date.today().year
cont = 0
x = 0
for c in range(0, 7):
    cont += 1
    a = int(input('Em que ano {}ª pessoa nasceu? '.format(cont)))
    if (date - a) <= 21:
        x += 1
    if (date - a) >= 21:
        z = cont - x
print('Ao todo tivemos {} pessoas maiores de idade'.format(z))
print('E também tivemos {} pessoas menores de idade'.format(x))
