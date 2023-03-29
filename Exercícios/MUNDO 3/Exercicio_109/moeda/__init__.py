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
