if __name__ == '__main__':
    listaDeConvidados = ['Filipe', 'Douglas', 'Rafael']

    nome = input('Digite o seu nome:')
    idade = int(input('Digite a sua idade:'))

    estaNaLista = nome in listaDeConvidados
    maiorIdade = idade >= 18

    if estaNaLista:
        if maiorIdade:
             print('Pode entrar ')
        else:
            print('Desculpe, voce e menor de idade')
    else:
        print('Voce nao esta na lista')