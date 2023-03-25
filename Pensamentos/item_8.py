from datetime import date


def voto(ano=date.today().year):
    i = date.today().year - ano
    if i >= 18:
        votar = 'OBRIGATÓRIO.'
    elif i < 18 and i >= 16:
        votar = 'OPCIONAL'
    else:
        votar = 'NEGADO.'

    return i, votar


n = int(input('Em que ano você nasceu? '))
idade, sit = voto(n)
print(f'Com {idade} anos: VOTO {sit}')
