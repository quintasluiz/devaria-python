# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros



print('{:=^40}'.format(' LOJAS GUANABARA '))
compras = float(input('Preço das Compras:R$ '))
print('''FORMAS DE PAGAMENTO
        [1] a vista dinheiro/cheque
        [2] a vista cartao
        [3] 2x no cartao
        [4] 3x ou mais no cartao  ''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = compras - (compras * 10) / 100
    print('Sua compra de {:.2f}, vai custar {:.2f} no final '.format(compras, desconto))
elif opção == 2:
    cartao = compras - (compras * 5) / 100
    print('Sua compra de {:.2f}, vai custar {:.2f} no final '.format(compras, cartao))
elif opção == 3:
    parcelas = int( input( 'Quantas parcelas?' ) )
    mensal = compras / parcelas
    print('Sua compra de {:.2f}, vai custar {:.2F} no final em {} parcelas de {:.2f}'.format(compras, compras, parcelas, mensal ))
elif opção == 4:
    parcelas = int( input( 'Quantas parcelas?' ) )
    juros = compras + (compras * 20) / 100
    jurosmensal = juros / parcelas
    print('Sua compra será parcelada em {} vezes de {:.2f} COM JUROS'.format(parcelas, jurosmensal))
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(compras, juros))
else:
    print('OPÇÃO INVALIDA!!!POR FAVOR VOLTE PARA O MENU INICIAL')












