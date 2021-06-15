if __name__ == '__main__':
    nota = int(input('Digite sua nota: '))

    if nota <= 30:
        print('Voce foi reprovado')
    elif nota <= 60:
        print('Voce ficou de recuperaçao')
    else:
        print('Voce esta aprovado')