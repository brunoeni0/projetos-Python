print('=X=' * 30)
print('{}10 TERMOS DE UMA PA'.format(' ' * 30))
print('=x=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c, end=' ')
print('ACABOU')