def Validar(valido1, valido2):
    if valido1 and valido2:
        return 'As duas variaveis sao verdadeiras'
    else:
        return 'Nao satisfez a condicao'

if __name__ == '__main__':
    teste1 = True
    teste2 = True

    respostaDaFuncao = Validar(teste1, teste2)

    print(respostaDaFuncao)

