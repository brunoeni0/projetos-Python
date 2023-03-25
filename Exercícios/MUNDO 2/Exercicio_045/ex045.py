from random import randint
from time import sleep
print('Suas opções:\n[ 0 ] para PEDRA \n[ 1 ] para PAPEL \n[ 2 ] para TESOURA')
jogador = (int(input('Qual é a sua jogada? ')))
if jogador >= 3:
    exit('Opção inválida, Tente novamente')
computador = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('=#='*30)
papel = jogador == 1 and computador == 0
tesoura = jogador == 2 and computador == 1
pedra = jogador == 0 and computador == 2
a = jogador == 0 and 'Pedra'
b = computador == 0 and 'Pedra'
print('Computador jogou {}'.format(b or computador == 1 and 'Papel' or 2 and 'Tesoura'))
print('Jogador jogou {}'.format(a or jogador == 1 and 'Papel' or 2 and 'Tesoura'))
print('=#=' * 30)
if papel > pedra:
    print('JOGADOR GANHOU')
elif tesoura > papel:
    print('JOGADOR GANHOU')
elif pedra > tesoura:
    print('JOGADOR GANHOU')
elif jogador == computador:
    print('EMPATE')
else:
    print('Computador GANHOU')
