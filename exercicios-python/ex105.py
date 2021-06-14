def notas(*n, sit=False):
    """
    -> Funçao para analisar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos(aceita varias)
    :param sit: valor opcional,indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informaçoes sobre a situaçãoda turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#programa principal
resp = notas(5.5,2.5,1.5, sit=True)
print(resp)
help(notas)