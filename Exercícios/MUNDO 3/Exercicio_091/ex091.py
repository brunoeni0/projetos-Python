from random import randint
from time import sleep
dado = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
num = []
nome = []
for k, v in dado.items():
    num.append(v)
    sleep(0.75)
    print(f'O {k} tirou {v}')
print('-=' * 30)
num.sort(reverse=True)
print('  == RANKING DOS JOGADORES ==')
for c in range(0, len(num)):
    sleep(0.75)
    print(f'{c+1}ª lugar:', end=' ')
    for k, v in dado.items():
        if num[c] == v and k not in nome:
            print(k, end=' ')
            nome.append(k)
            break
    print(f'com {num[c]}.')
