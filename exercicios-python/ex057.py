#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf' and sexo != 'homem' and sexo != 'mulher':
    sexo = str(input('Dados invalidos por favor digite seu sexo: ')).strip().upper()[0]
if sexo == 'masculino ' or 'feminino':
    print(f'Sexo {sexo} reservado com sucesso')