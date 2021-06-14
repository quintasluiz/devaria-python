#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#numero primo dividido por um e por ele mesmo
num = int(input('Digite um numero: '))
contador = 0

for i in range(1,num + 1):  #mais um por que o for conta um a menos
    if num % i == 0:
        contador += 1

print( "O número {} foi divisível {} vezes!".format( num, contador ) )

if contador == 2:
    print( "O número é primo" )
else:
    print( "O número não é primo" )