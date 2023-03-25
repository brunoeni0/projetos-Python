from datetime import date


def voto(i=date.today().year):
    ano = date.today().year - i
    return ano


n = int(input('Em que ano você nasceu? '))
idade = voto(n)
if idade >= 18:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
elif idade < 18 and idade >= 16:
    print(f'Com {idade} anos: VOTO OPCIONAL.')
else:
    print(f'Com {idade} anos: VOTO NEGADO.')
