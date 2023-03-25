valor = float(input('Quanto você ganha por hora? '))
horas = int(input('número de horas trabalhadas no mês? '))
total = (valor * horas) * 6
print(f'Você ganha R${total:.0f} semanalmente')