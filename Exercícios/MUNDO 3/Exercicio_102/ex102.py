def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    c = 1
    num = n
    print()
    print('--' * 15)
    while c != num:
        if show:
            print(c, end=' x ')
        n *= c
        c += 1
    if show:
        print(c, end=' = ')
    return n


#progrma principal
print(fatorial(5, True))
help(fatorial)
