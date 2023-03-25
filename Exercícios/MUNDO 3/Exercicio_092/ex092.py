from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Anos de Nascimento: '))
dados['cateira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['cateira'] != 0:
    dados['tempo'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
print('-=' * 30)
print(f'  - nome tem o valor {dados["nome"]}')
print(f'  - idade tem o valor {(date.today().year) - (dados["ano"])}')
print(f'  - ctps tem o valor {dados["cateira"]}')
if dados['cateira'] != 0:

    print(f'contratação tem o valor {dados["tempo"]}')
    print(f'salário tem o valor {dados["salario"]:.2f}')
    print(f'aposentadoria tem o valor {((date.today().year) - (dados["ano"])) + (35 - ((date.today().year) - (dados["tempo"])))}')
