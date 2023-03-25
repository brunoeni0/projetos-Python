sala = list()
alunos = list()
notas = list()
media = list()
while True:
    alunos.append(str(input('Nome: ')))
    notas.append(float(input('Nota1: ')))
    notas.append(float(input('Nota2: ')))
    media.append((notas[0] + notas[1]) / 2)
    alunos.append(media[:])
    alunos.append(notas[:])
    sala.append(alunos[:])
    alunos.clear()
    notas.clear()
    pare = str(input('Quer continuar? [S/N] ')).upper()
    while pare not in 'SN':
        pare = str(input('Quer continuar? [S/N]')).upper()
    if pare in 'N':
        break
print('-=' * 30)
print('No. {:<10}{:>10}'.format('NOME', 'MÉDIA'))
print('-' * 25)
for p in range(0, len(sala)):
    print('{:<3}{:<10}{:>7}{:.1f}'.format(p+1, sala[p][0], '', sala[p][1][p]))
print('-' * 25)
ver = int(input('Mostrar notas de qual aluno? (0 interrompe): '))
while ver != 0:
    print(f'Notas de {sala[(ver-1)][0]} são {sala[(ver-1)][2]}')
    ver = int(input('Mostrar notas de qual aluno? (0 interrompe): '))
    while ver > (p + 1):
        ver = int(input('mostrar notas de qual aluno? (0 interrompe): '))
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
