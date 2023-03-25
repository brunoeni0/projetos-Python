#print(input.__doc__)
#help(input)


#def contador(i, f, p):
#    """
#  -> Faz uma contagem e mostra na tela.
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    for c in range(i, f+1, p):
#        print(c, end=' ')
#    print('FIM!')


#contador(2, 10, 2)
#help(contador)
#print(contador.__doc__)


#def soma(a=0, b=0, c=0):
#    s = a + b + c
#    print('A soma vale: ', s)


#soma(3, 2, 5)
#soma(8, 5)

#def teste():
#    x = 8
#    print(f'Na função teste, n vale {n}')
#    print(f'Na função teste, x vale {x}')


# Programa Principal
#n = 2
#print(f'No programa principal, n vale {n}')
#teste()


#def funcao():
#    n1 = 4
#    print(f'N1 dentro vale {n1}')


#n1 = 2
#funcao()
#print(f'N1 fora vale {n1}')
#def teste (b):
#    b += 4
#    a = 8
#    c = 2
#    print(f'A dentro vale {a}')
#    print(f'B dentro vale {b}')
#    print(f'C dentro vale {c}')


#a = 5
#teste(a)
#print(f'A fora vale {a}\n')


#def teste (b):
#    global a
#    b += 4
#    a = 8
#    c = 2
#    print(f'A dentro vale {a}')
#    print(f'B dentro vale {b}')
#    print(f'C dentro vale {c}')


#a = 5
#teste(a)
#print(f'A fora vale {a}')
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(2, 2)
soma(6)


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
