def escreva(p):
    t = len(p) + 4
    print('~' * t)
    print(f'{p:^{t}}')
    print('~' * t)


palavras = ['Gustavo Guanabara', 'Curso de Python no You tube', 'CeV']
for c in palavras:
    escreva(c)
