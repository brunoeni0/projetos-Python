from cores import amarelo, azul, vermelho
n = int(input('{}digite um numero:'.format(amarelo)))
s =n%2
if s == 0:
    print('{}PAR'.format(azul))
else:
    print('{}ÍMPAR'.format(vermelho))
