from ulteis import numeros
numero = int(input('Digite um número: '))
fat = numeros.fatorial(numero)
print(f'O fatorial de {numero} é {fat}')
print(f'O doblo de {numero} é {numeros.doblo(numero)}')
print(f'O tiplo de {numero} é {numeros.triplo(numero)}')
