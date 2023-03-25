print('Gerador de PA')
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
cont = 0
q = 10
k = 0
while cont <= q:
    print(t, end=' - ')
    k = q
    cont += 1
    t += r
    if cont == q:
        print('PAUSA')
        q += int(input('Quantos termos você quer mostrar a mais? '))
        if k == q:
            q -= 1
print('\nProgressão finalizada com {} termos mostrados.'.format(cont))
