#Escreva um programa que converta a temperatura de Cº ara fº

c = float(input('Informe a temperatura em ºc: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c,f))