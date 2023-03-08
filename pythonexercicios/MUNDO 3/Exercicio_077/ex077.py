palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'\nNa Palavra {c} temos', end=' ')
    for p in c:
        if p in 'AEIOU':
            print(f'{p.lower()}', end=' ')
