def dobro(n=1):
    return n * 2


def metade(n=1):
    return  n / 2


def aumentar(n=1, t=1):
    return n + (n * t / 100)


def diminuir(n=1, t=1):
    return n - (n * t / 100)


def moeda(x):
    return f'R${x:.2f}'.replace('.', ',')
