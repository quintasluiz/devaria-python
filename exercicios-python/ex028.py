#Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5 tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns!Voce conseguiu me vencer')
else:
    print('Ganhei!Eu pensei no numero {} e não no {}!'.format(computador, jogador))