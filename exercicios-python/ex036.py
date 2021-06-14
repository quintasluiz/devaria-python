#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


vc = float(input('Valor da casa: R$ '))
s = float(input('Salario do comprador: R$ '))
f = int(input('Quantos anos de financiamento?'))
minimo = s * 30 / 100
p = vc/(f * 12)
if p <= minimo:
    print('Para pagar uma casa de R${:.3f} em {} anos a prestaçao será de {:.2f} EMPRESTIMO ACEITO!!!'.format(vc, f, p))
else:
 print('Para pagar uma casa de R${:.3f} em {} anos a prestação será de {:.2f} EMPRESTIMO NEGADO!!!'.format(vc, f, p))