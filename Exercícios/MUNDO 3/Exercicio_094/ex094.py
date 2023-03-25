pessoas = list()
mulheres = list()
pessoa = dict()
media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if pessoa['sexo'] not in 'MF':
        while pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
            pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoas.append(pessoa.copy())
    pessoa.clear()
    pare = str(input('Quer continuar? [S/N] ')).upper()
    if pare not in 'SN':
        while pare not in 'SN':
            print('ERRO! Responda apenas S ou N.')
            pare = str(input('Quer continuar? [S/N] ')).upper()
    if pare == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media / len(pessoas)} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for c in range(0, len(mulheres)):
    print(mulheres[c], end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for m in range(0, len(pessoas)):
    if pessoas[m]['idade'] > (media / len(pessoas)):
        print(f'   nome = {pessoas[m]["nome"]}; sexo = {pessoas[m]["sexo"]}; idade = {pessoas[m]["idade"]};')
print('<< ENCERRADO >>')
