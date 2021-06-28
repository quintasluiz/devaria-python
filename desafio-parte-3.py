from classes.enums.MeioPagamento import MeioPagamento

if __name__ == '__main__':
    produtos_disponiveis = [
        {'nome': 'Chinelo', 'preco_unidade': 20},
        { 'nome': 'Tenis', 'preco_unidade': 250},
        {'nome': 'Sandalia', 'preco_unidade': 180},
        {'nome': 'Calça', 'preco_unitario':120}

    ]
    produtos_selecionados = []

    while True:
        produto_digitado = input("Digite o nome do produto que irá comprar('sair' para sair")

        if(produto_digitado == 'sair'):
            break

        produtos_encontrados = list(filter(lambda p : p['nome'] == produto_digitado, produtos_disponiveis))

        if len(produtos_encontrados) == 0:
            print('Esse produto não foi encontrado, favor digitar outro')
        else:
            while True:
                try:
                    qtd_produto = int(input(f"Digite a quantidade de {produto_digitado} que voce deseja"))
                    break
                except:
                    print("Quantidade digitada incorreta")

            produtos_selecionados.append({
                'nome': produto_digitado,
                'quantidade': qtd_produto,
                'valor': produtos_encontrados[0]['preco_unidade']
            })

        while True:
            try:
                meio_pagamento_digitado = forma_pagamento = input("Digite a forma de pgamento (Pix ou Boleto): ")
                meio_pagamento = MeioPagamento( forma_pagamento )
                break
            except:
              print("Forma de pagamento invalida")

            compra = compra( meio_pagamento, produtos_selecionados )
            compra.RealizarCompra()



