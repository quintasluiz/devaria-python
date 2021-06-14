#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
#desconsiderando os espaços


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
print('Voce digitou a frase {}'.format(junto))
inverso =''
for letra in range(len(junto) -1, -1,-1):
    inverso +=junto[letra]
print('Oinverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palidromo')
else:
    print('A frase não é um palindromo')