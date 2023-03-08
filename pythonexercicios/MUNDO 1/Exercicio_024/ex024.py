from cores import roxo, branco
a = input('{}Em que cidade você naceu? '.format(branco))
a = a.lower()
b = a.split()
c = 'santo' in b[0]
print(roxo, c)