jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['total'] = 0
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if jogador['partidas'] > 0:
        for g in range(0, jogador['partidas']):
            gols.append(int(input(f'Quantos gols na partida {g+1}? ')))
            jogador['total'] += gols[g]
    jogador['gols'] = (gols[:])
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    pare = str(input('Quer continuar? [S/N] ')).upper()
    if pare not in 'SN':
        while pare not in 'SN':
            pare = str(input('Quer continuar? [S/N] ')).upper()
    elif pare in 'N':
        break
    print('--' * 25)
print('-=' * 30)
print(f'{"cod nome":<15} {"gols":^15} {"total":>15}')
print('--' * 25)
for c in range(0, len(jogadores)):
    print(f' {c + 1:<3}{jogadores[c]["nome"]:<17}{str(jogadores[c]["gols"]):<22} {jogadores[c]["total"]}')
while True:
    print('--' * 30)
    p = int(input('Mostrar dados de qual jogador? (0 para parar) '))
    if p > 0 and p <= len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[p-1]["nome"]}')
        for c in range(0, len(jogadores[p-1]["gols"])):
            print(f'No jogo {c+1} fez {jogadores[p-1]["gols"][c]} gols.')
    elif p == 0:
        break
    else:
        print(f'ERRO! Não existe jogador com o código {p}')
