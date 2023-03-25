from random import randint
sorti = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
listar = sorted(sorti)
print(f'''Os valores sorteados foram: {sorti}
O maior valor sorteado foi {listar[-1]}
O menor valor sorteado foi {listar[0]}''')