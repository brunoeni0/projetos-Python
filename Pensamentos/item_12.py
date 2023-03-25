def dobro(n=1, r=True):
    n *= 2
    if r:
        return f'R${n:.2f}'
    else:
        return f'{n:.2f}'


def metade(n=1, r=False):
    n /= 2
    if r:
        return f'R${n:.2f}'
    else:
        return f'{n:.2f}'


def aumentar(n=1, t=1, r=False):
    c = n + (n * t // 100)
    if r:
        return f'R${n:.2f}'
    else:
        return f'{c:.2f}'


def diminuir(n=1, t=1, r=False):
    c = n - (n * t // 100)
    if r:
        return f'R${n:.2f}'
    else:
        return f'{c:.2f}'


from ex107 import moeda
p = float(input('Digite um valor: RS'))
print(f'A metade de {p:.2f} é {moeda.metade(p, True)}')
print(f'O doblo de {p:.2f} é {moeda.dobro(p, True)}')
print(f'Aumentado 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
