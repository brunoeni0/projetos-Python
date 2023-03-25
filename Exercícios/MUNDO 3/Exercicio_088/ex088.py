from random import randint
from time import sleep
bolada = []
jogo = []
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=- SORTEANDO {num} JOGOS -=-=-=')
for c in range(num):
    while len(jogo) != 6:
        sorte = (randint(1, 60))
        if sorte not in jogo:
            jogo.append(sorte)
    jogo.sort()
    sleep(0.5)
    bolada.append(jogo[:])
    jogo.clear()
    print(f'jogo {c+1}: {bolada[c]}')
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
