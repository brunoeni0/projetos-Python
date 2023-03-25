from datetime import date
ano = int(input('Digite o ano [ 0 ] para ver o atual '))
atual = date.today().year
bis = ano or atual
if bis % 4 == 0 and bis % 100 != 0 or bis % 400 == 0:
    print('O ano {} é BISSEXTO'.format(bis))
else:
    print('O ano {} não é BISSEXTO'.format(bis))
