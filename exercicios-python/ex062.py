#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos

print('Gerador de PA')
print('-=' * 10)
primeiro= int(input('Primeiro termo: '))
razão = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados '.format(total))