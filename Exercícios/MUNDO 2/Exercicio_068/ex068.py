from random import randint
cont = 0
total = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    jogador = int(input('qual a sua jogada?'))
    computador = randint(0, 10)
    total = jogador + computador
    if escolha == 'P':
        if total % 2 == 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU PAR')
            print('Você VENCEU!\nVamos jogar novamenti')
            cont += 1
        elif total % 2 == 1:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU ÌMPAR')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU ÍMPAR')
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        elif total % 2 == 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU PAR')
            break
print(f'GAMER OVER! Você venceu {cont} vezes.')
