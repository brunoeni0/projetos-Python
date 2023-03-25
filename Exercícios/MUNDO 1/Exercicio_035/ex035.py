from cores import amarelo, azul, verde, vermelho, branco, roxo
print('{}-='.format(branco)*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('{}Primeiro segmento: '.format(vermelho)))
r2 = float(input('{}Segundo segmento: '.format(amarelo)))
r3 = float(input('{}Terceiro segmento: '.format(azul)))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('{}Os segmentos acima PODEM FORMA triângulo!'.format(verde))
else:
    print('{}Os segmentos acima NÃO PODEM FORMA triângulo'.format(roxo))
