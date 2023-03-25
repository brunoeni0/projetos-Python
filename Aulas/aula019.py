#def soma(a, b):
#    s = a + b
#    print(s)


# Programa Principal
#soma(4, 5)
#soma(8, 9)
#soma(2, 1)


#def soma(a, b):
#    print(f'A = {a} B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')

# Programa Principal
#soma(b=4, a=5)
#soma(7, 2)


#def contador(* a):
#    print(a)


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

#def contador(* a):
#    for valor in a:
#        print(valor, end=' ')
#    print()


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

#def contador(* a):
#    print(f'Recebi os valores {a} e são ao todo {len(a)} números')


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)


#def dobla(lista):
#    for c in range(0, len(valores)):
#        lista[c] *= 2


#valores = [6, 3, 9, 1, 0, 2]
#dobla(valores)
#print(valores)


def num(* valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valores {valores} temos {s}')


num(5, 2)
num(2, 9, 4)
