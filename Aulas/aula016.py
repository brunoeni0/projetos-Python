# lanche = (trupla)[listar]{dicionario}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
for c in lanche:
    print(f'Eu vou comer {c}')

for comida in range(0, len(lanche)):
    print(lanche[comida])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche))

print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))
print(c.count(5))
print(c.index(5, 1))

pessoa = ('Gustavo', 39, 'M', 99.88)
del (pessoa)
print(pessoa)
