#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
#mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do seu veiculo?'))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite de veocidade permitido')
    multa = (velocidade - 80) * 7
   print('Voce deve pagar uma multa de {:.2f}!'.format(multa))
    print('Tenha um bom dia dirija com cuidado')



