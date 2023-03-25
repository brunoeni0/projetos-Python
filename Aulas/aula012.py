nome = str(input('Qual é seu nome? '))
if nome == 'bruno':
    print('Que nome bonito')
elif nome == 'maria' or nome == 'paula' or nome == 'maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana jessica juliana paulo':
    print('Belo nome feminino')
print('Tenha um bom dia, {}!'.format(nome))
