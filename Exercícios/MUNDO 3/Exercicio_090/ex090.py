aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual {v}')
print('Situação é igual a', end=' ')
if aluno['Média'] >= 7:
    print('Aprovado')
elif aluno['Média'] >= 5:
    print('Recuperação')
else:
    print('Reprovado')
