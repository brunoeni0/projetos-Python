tab = []
num = str(input('Digite uma expressão: '))
for c in range(0, len(num)):
    if num[c] == '(':
        tab.append(num[c])
    elif num[c] == ')':
        tab.append(num[c])
    for k in range(0, len(tab)):
        if tab[0] == '(' and tab[k] == ')':
            tab.remove('(')
            tab.remove(')')
if len(tab) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
