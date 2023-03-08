def leiaint(x):
    while True:
        num = input(x)
        if num.isnumeric().__int__():
            return num
        else:
            print('\033[31mErro! Digite um valor inteiro válido.\033[m')


#programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
