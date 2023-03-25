campeonato = list()
jogador = dict()
gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, partidas):
    campeonato.append(int(input(f'Quantos gols na partida {g+1}? ')))
    gols += campeonato[g]
jogador['gols'] = campeonato
jogador['total'] = gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campo gols tem o valor {jogador["gols"]}.')
print(f'O campo total tem o valor {jogador["total"]}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'=> Na partida {p+1} fez {campeonato[p]} gols.')
print(f'Foi um total de {gols} gols.')
