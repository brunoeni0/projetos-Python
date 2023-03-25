cont = soma = c = 0
while c != 1:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma = soma + num
        cont += 1
    elif num == 999:
        c += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
