#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


'''co = float(input('Comprimento do cateto oposto '))
ca = float(input('Comprimento do cateto adjascente '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir{:.2f} '.format(hi))'''

import math
co = float(input('Comprimento do cateto oposto '))
ca = float(input('Comprimento cateto adjascente '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))

from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjascente'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi)



