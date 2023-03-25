from datetime import date
from cores import azul, vermelho, verde, amarelo
ano = int(input('{}Que ano quer analisar?{} Coloque 0 para analisar o ano atual: '.format(azul, vermelho)))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano {} é BISSEXTO'.format(verde, ano))
else:
    print('{}O ano {} NÃO é BISSEXTO'.format(amarelo, ano))
