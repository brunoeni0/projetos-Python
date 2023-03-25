def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de um aluno.
    :param n: recerbe uma ou mais notas do aluno (aceita várias).
    :param sit: opcional, indicando se deve ou não adicionar a situação.
    :return: retorna as informações.
    """
    global resp
    media = 0
    for c in range(0, len(n)):
        media += (n[c] / len(n))
    resp = {"total": len(n), "maior": max(n), "menor": min(n), "media": f'{media:.2f}'}
    if sit:
        if media >= 7:
            resp["situação"] = 'BOA'
        elif 5 <= media < 7:
            resp["situação"] = 'RASOÁVEL'
        else:
            resp["situação"] = 'RUIM'
    print('--' * 40)


#Programa principal
notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
