from datetime import date
atual = date.today().year
cont = 0
for c in range(1, 8):
    nas = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if atual - nas >= 21:
        cont += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade'.format(cont, c-cont))
