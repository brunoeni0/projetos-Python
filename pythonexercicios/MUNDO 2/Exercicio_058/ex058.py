from random import randint
a = 0
tentativas = 0
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
 Será que você consegue adivinhar qual foi?''')
while a != 1:
    jodagor = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jodagor == computador:
        a += 1
        print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
    elif jodagor > computador:
        print('Menos... Tente mais uma vez.')
    elif jodagor < computador:
        print('Mais... Tente mais uma vez.')
