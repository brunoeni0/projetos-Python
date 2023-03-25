frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('O inverso de {} é'.format(junto), end=' ')
for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra], end='')
    inverso += junto[letra]
if junto == inverso:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')
