#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida





peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O IMC é de {:.1f}'.format(imc))
    print('Voce esta ABAIXO DO PESO!!!')

elif imc <= 25:
    print('O imc é de {:.1f}'.format(imc))
    print('Voce esta com o PESO IDEAL')

elif imc <= 30:
    print('O imc é de {:.1f}'.format(imc))
    print('Voce esta de SOPREPESO')

elif imc <= 40:
    print('O imc é de {:.1f}'.format(imc))
    print('Voce esta com OBESIDADE')

else:
    print('O imc é de {:.1f}'.format(imc))
    print('Voce esta com OBESIDADE MORBIDA')