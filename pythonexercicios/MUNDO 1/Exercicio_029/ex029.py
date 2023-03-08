from cores import vermelho, verde, amarelo, limpa
from time import sleep
print('{}AVISO PROIBIDO VELOCIDADE ACIMA DE 80KM{}'.format('\033[7;30m',limpa))
sleep(5)
velocidade = int(input('{}Qual a velocidade do carro? '.format(amarelo)))
sleep(3)
m = (velocidade - 80)*7
if velocidade > 80:
    print('{}Você foi multado,e vai paga R$ {} de multa '.format(vermelho, m))
else:
    print('{}dirija com segurança'.format(verde))
