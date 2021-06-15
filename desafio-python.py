def soma(n1, n2):
    print(f'Somando{n1} + {n2}')
    resultado = n1 + n2

    return resultado

def subtracao(n1, n2):
    print(f'Subtraindo {n1} - {n2}')
    resultado = n1 - n2

    return resultado

def multiplicacao(n1, n2):
    print(f'Multiplicando {n1} * {n2}')
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    print(f'Dividindo {n1} / {n2}')
    resultado = n1 / n2
    return resultado


if __name__ == '__main__':
    n1 = int(input('Digite o primeiro numero:'))
    n2 = int(input('Digite o segundo numero'))

    operador = input('Digite o operador do calculo')

    if operador == '+':
        resultado = soma(n1, n2)
    elif operador == '-':
        resultado = subtracao(n1, n2)
    elif operador == '*':
        resultado = multiplicacao(n1, n2)
    elif operador == '/':
        resultado = divisao(n1,n2)
    else:
        print('Operador incorreto')
    print(f'O resultado da operação é:{resultado}')

