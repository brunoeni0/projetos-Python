def ficha(n, g):
    if len(n.strip()) == 0:
        n = '<desconhecido>'
    if len(g.strip()) == 0 or g.isalnum() and not g.isnumeric():
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Nome do Jogador: ')
gols = input('Números de Gols: ')
ficha(nome, gols)
