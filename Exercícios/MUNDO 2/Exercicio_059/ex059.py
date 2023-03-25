from time import sleep
a = 5
c = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo  valor: '))
while a != c:
    print('''Escolhar a opção:
[ 1 ] para somar
[ 2 ] para multiplicar
[ 3 ] para ver o maior número
[ 4 ] para novos números
[ 5 ] para sair do programa''')
    c = int(input('Qual é a sua opção? '))
    if c == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif c == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    if c == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        elif n1 == n2:
            print('Os números são iguais')
    if c == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    if c == 5:
        print('Finalizando...')
    elif c > 5:
        print('Opção inválida. Tente novamente')
    print('===' * 15)
    sleep(2)
print('Fim do programa! Volte sempre!')
