print('===== Desafio 091 =====')
from random import randint
from time import sleep
jogadores = dict()
rank = list()
for c in range(0, 4):
    rank.append(randint(1, 6))
    jogadores[f"jogador{c+1}"] = rank[c]
print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')
rank.sort(reverse=True)
print('-=' * 20)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for c in range(0, 4):
    for k, v in jogadores.items():
        if rank[c] == v:
            sleep(0.5)
            print(f'{c+1:>3}º lugar: {k} com {v}.')
            jogadores[k] = 0
            break
