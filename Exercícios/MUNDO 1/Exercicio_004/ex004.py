import cores
X = input('{}Digite algo: '.format(cores.branco))
print(cores.vermelho, 'Só tem espaços?', X.isspace())
print(cores.amarelo, 'É um número?', X.isnumeric())
print(cores.verde, 'É alfabético?', X.isalpha())
print(cores.azul, 'É alfanumérico?', X.isalnum())
print(cores.roxo, 'Está em minúsculas?', X.islower())
print(cores.cinza, 'Está em maiúsculas?', X.isupper())
print(cores.branco, 'Está capitalizado?', X.istitle())
print(cores.azul, 'É um decimal?', X.isdecimal())
#print(cores.amarelo, 'É imprimivel?', X.isprintable())
# print('É identificado?',X.isidentifier())
# print('É um digito? ',X.isdigit())1