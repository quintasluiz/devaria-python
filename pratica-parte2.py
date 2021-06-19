if __name__ == '__main__':
    #Lista de produtos do usuario
    produtos_usuario = []

    #Lista de produtos disponiveis no mercado
    produtos_mercado =["Refrigerante", "cerveja","maça"]

    #Realiza a leitura dos produtos do usuario
    while True:
        produto = input("Digite um produto para adicionar na lista(Digite 'sair'")

        if produto == 'sair':
            break

        produtos_usuario.append(produto)

    #Salvar produtos indisponiveis
        produtos_indisponiveis = []
        #Salvar produtos disponiveis
        produto_disponiveis = []

    #Percorre a listade produtos que o usuario digitou
    for p in produtos_usuario:
        #Valida se o prouto esta disponive ou nao
        if not p in produtos_mercado:
            produtos_indisponiveis.append(p)
        else:
            produto_disponiveis.append(p)

    print(f'Produtos indisponiveis: {produtos_indisponiveis}')

    #Ordenar lista de produtos
    produto_disponiveis.sort()
    print(f'Produtos disponiveis: {produto_disponiveis}')

