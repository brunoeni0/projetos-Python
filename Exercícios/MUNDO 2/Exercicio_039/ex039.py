from datetime import date
ano = int(input('Qual é o ano de nascimento: '))
ok = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, ok, date.today().year))
if ok == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif ok > 18:
    print('Você já deveria ter se alistado há {} anos'.format(ok - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))
elif ok < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - ok))
    print('Seu alistamento será em {}'.format(ano + 18))
