def leiaDinheiro(algo):
    while True:
        count = 0
        novo = ''
        valor = input(algo).replace(',', '.')
        for v in valor:
            if ' ' not in v:
                novo += v
        for n in novo:
            if n.isnumeric() or '.' in n:
                count += 1
        if len(novo) == 1 and novo[0] == '.':
            count -= 1
        if count == len(novo) and novo.count('.') < 2 and len(novo) != 0:
           break
        print(f'\033[31mERRO: \"{novo}\" é um preço inválido!\033[m')
    return float(novo)
