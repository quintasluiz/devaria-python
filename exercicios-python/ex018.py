#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.



import math
angulo = float(input('Digite um angulo '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo'))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a tangente de {}'.format(angulo, tangente))



