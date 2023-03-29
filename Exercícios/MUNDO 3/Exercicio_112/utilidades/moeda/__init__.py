def dobro(n=1, r=False):
    n *= 2
    if r:
        n = moeda(n)
    return n


def metade(n=1, r=False):
    n /= 2
    if r:
        n = moeda(n)
    return n


def aumentar(n=1, t=1, r=False):
    c = n + (n * t / 100)
    if r:
        c = moeda(c)
    return c


def diminuir(n=1, t=1, r=False):
    c = n - (n * t / 100)
    if r:
        c = moeda(c)
    return c


def moeda(x):
    return f'R${x:.2f}'.replace('.', ',')


def resumo(v, au=0, dim=0):
    print('--' * 15)
    print(f'{"RESUMO DO VALOR":^30}')
    print('--' * 15)
    print(f'Preço analisado:  {moeda(v)}')
    print(f'Dobro do preço:   {dobro(v, True)}')
    print(f'Metade do preço:  {metade(v, True)}')
    print(f'{au}% de Aumento:   {aumentar(v, au, True)}')
    print(f'{dim}% de Redução:   {diminuir(v, dim, True)}')
    print('--' * 15)
