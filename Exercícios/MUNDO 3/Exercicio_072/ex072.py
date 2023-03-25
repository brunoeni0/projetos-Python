numeros = ('zero', 'um', 'dois', 'trêis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while not 0 <= numero or numero > 20:
    numero = int(input('Tente novamente. Digite o número entre 0 e 20: '))
print(f'Você digitou o número {numeros[numero]}')
