#Faça um programa que leia o peso de cinco pessoas.No final mostre qual o maior eo menor pesolidos

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))


lista = []

for p in range(1,6):
    lista.append(float(input(f'Qual é o peso da {p} pessoa')))
print(f'O maior peso é {max(lista)}')
print(f'O menor peso é {min(lista)}')