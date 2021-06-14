#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento


salario = float(input('Qual é o salario do funcionario? '))
aumento = salario + (salario *15 / 100)
print('O funcionario ganhava {:.2f} com o aumento agora ganha {:.2f}'.format(salario, aumento))





