from datetime import date


def voto(ano=date.today().year):
    idade = date.today().year - ano
    if 65 > idade >= 18:
        votar = 'VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or 65 <= idade:
        votar = 'VOTO OPCIONAL'
    else:
        votar = 'NÃO VOTA.'

    return idade, votar


print()
print('--' * 15)
n = int(input('Em que ano você nasceu? '))
sit = voto(n)
print(f'Com {sit[0]} anos: {sit[1]}')
