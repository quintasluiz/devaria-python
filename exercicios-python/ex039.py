#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
atual = date.today().year

nascimento = int(input('Digite a data de seu nascimento: '))
idade = atual - nascimento
alistamento = 18
falta = alistamento - idade
f = idade - alistamento
d = atual - f
data = atual + falta
if idade == alistamento:
    print('Quem nasceu em {} tem {} anos em 2021.Voce tem que se alistar IMEDIATAMENTE'.format(nascimento, idade))
elif idade < alistamento:
    print('Quem nasceu em {} tem {} anos em 2021.Ainda faltam {} anos para o alistamento.Seu alistamento será em {}'.format(nascimento, idade, falta, data))
else:
    print('Quem nasceu em {} tem {} anos em 2021.Voce ja deveria ter se alistado a {} anos.Seu alistamento foi em {}'.format(nascimento, idade,  f, d))