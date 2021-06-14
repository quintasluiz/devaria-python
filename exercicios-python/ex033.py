#Faça um programa que leia tres numeros emostrre o maior e o menor valor


v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
valores = [v1, v2, v3]
print('O menor valor digitado foi {}'.format(min(valores)))
print('O maior valor digitado foi {}'.format(max(valores)))


a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

    maior = a
if b > a ad b > c:
    maior = b
if c > a and c > b:
    maior = c

    print('O menor valor digitado foi {}'.format(menor))
    print('O maior valor digitado foi {}'.format(maior))