from cores import  vermelho, verde, amarelo, azul, azulclaro
n1 = int(input('{}Primeiro valor: '.format(amarelo)))
n2 = int(input('{}Segundo valor: '.format(verde)))
n3 = int(input('{}Terceiro valor: '.format(azulclaro)))
menor = n1
# Verificando quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{}O menor valor digitado foi {}'.format(azul, menor))
print('{}O maior valor digitado foi {}'.format(vermelho, maior))