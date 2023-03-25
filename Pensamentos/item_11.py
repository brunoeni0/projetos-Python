from ex107 import moeda
p = float(input('Digite um valor: RS'))
print(f'A metade de {p:.2f} é {moeda.metade(p)}')
print(f'O doblo de {p:.2f} é {moeda.dobro(p)}')
print(f'Aumentado 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

def dobro(n=1):
    n *= 2
    return f'{rs()}{n:.2f}'


def metade(n=1):
    n /= 2
    return f'{rs()}{n:.2f}'


def aumentar(n=1, t=1):
    c = n + (n * t // 100)
    return f'{rs()}{c:.2f}'


def diminuir(n=1, t=1):
    c = n - (n * t // 100)
    return f'{rs()}{c:.2f}'


def rs():
    return 'R$'
