#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2

if m >= 7.0:
    print('Tirando {} e {} a sua media foi {}'.format(n1, n2, m))
    print('Voce esta APROVADO!!!')

elif m < 5.0:
    print('Tirando {} e {} a sua media foi {}'.format(n1, n2, m))
    print('Voce foi REPROVADO')

else:
    print('Tirando {} e {} a sua media foi {}'.format(n1, n2, m))
    print('Voce ficou de RECUPERAÇÃO')