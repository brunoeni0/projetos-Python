print('===== Desafio 091 =====')
from operator import itemgetter
from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')
print('-=' * 20)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for p, v in enumerate(rank):
        sleep(0.5)
        print(f'{p+1:>3}º lugar: {v[0]} com {v[1]}.')
