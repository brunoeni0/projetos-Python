frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print('Oi')

print('''''')

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))

#print(len(frase))
# print(len(frase.strip()))
# print(frase.replace('Python','Android'))
# frase = frase.replace('Python','Android')
# print(frase)

print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))

# print(frase.split())

dividido = (frase.split())
# print(dividido[0])
print(dividido[2][3])