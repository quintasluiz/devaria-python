total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço =float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp =str(input('Quer continuar? [S/N')).strip().upper()[0]
    if resp =='N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA '))
print(f'O total da compra foi R${total}')
print(f'Temos {totmil} produto custando mais de mil reais')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')