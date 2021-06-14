#Escreva um programa em Python que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão'
      [1] Converter para BINARIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''' )
Opção = int(input('Sua opção: '))
if Opção == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif Opção == 2:
    print('{} convertido para octa é igual a {}'.format(num, oct(num)[2:]))
elif Opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Comando Invalido')



