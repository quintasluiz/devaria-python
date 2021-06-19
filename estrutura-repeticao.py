def lavaCarro(posicao):
    print(f"Lavando carro na posicao {posicao}")

def verificarTemCarroNaFila(posicao):
    if(posicao > 5):
        return False
    else:
        return True


if __name__ == '__main__':


#Estrutura de repetição com intervalo de valores

    #for crescente
    for n in range(0, 5):
        print(n)

    #for decrescente
    for n in range(5, 0, -1):
        print(n)

    #for percorrendo caracteres de uma string
    palavra = 'Devaria'
    for p in palavra:
        print(p)

    #Estrutura de repetiçao while crescente
    n = 0
    while n < 5:
        print(n)
        n = n +1

    temCarroNaFila = True
    posicao = 1
    while temCarroNaFila:
        lavaCarro(posicao)
        posicao += 1
        temCarroNaFila = verificarTemCarroNaFila(posicao)
    else:
        print("Terminou de lavar os carros")