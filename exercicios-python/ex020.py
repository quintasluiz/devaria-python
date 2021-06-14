#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Digite um nome '))
n2 = str(input('Digite outro nome '))
n3 = str(input('Digite mais um nome '))
n4 = str(input('Digite mais um '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)