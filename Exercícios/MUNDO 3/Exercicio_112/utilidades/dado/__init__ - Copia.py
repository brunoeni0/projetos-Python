def verificar(valor):
    try:
        novo = ""
        for v in valor:
            if ' ' not in v:
                novo += v
        valor = float(novo.replace(',', '.'))
    except ValueError:
        while True:
            print(f'\033[31mErro: \"{novo}\" é um preço inválido!\033[m')
            novo = ''
            count = 0
            valor = input('Digite o preço: R$').replace(',', '.')
            for v in valor:
                if ' ' not in v:
                    novo += v
            for n in novo:
                if n.isnumeric() or '.' in n:
                    count += 1
            if count == len(novo) and count != 0 and not (novo[0] in '.' and len(novo) == 1 or novo.count('.') > 1):
                break
    finally:
        return float(valor)
