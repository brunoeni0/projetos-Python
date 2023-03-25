#n = s = 0
#while True:
#    n = int(input('Digite um número: '))
#    if n == 999:
#        break
#    s += n
#print(s)
#print('Acabou')
nome = 'jose'
idade = 33
# print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
# print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
# print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
salario = 987.35
print(f'O {nome:-<20} tem {idade} anos e ganhar R${salario:.2f}')
