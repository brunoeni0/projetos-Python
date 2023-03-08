r1 = float(input('Primeiro número: '))
r2 = float(input('Segundo número: '))
r3 = float(input('Terceiro número: '))
regra = r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2
i = r1 == r2 != r3 and r2 == r3 != r1 and r1 == r3 != r2
d = r1 != r2 != r3
if regra and i:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
elif r1 == r2 == r3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif regra and d:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
