print('Gerador de PA')
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p + r * 9
while p != r + t:
    print(p, end=' - ')
    p += r
print('FIM')
