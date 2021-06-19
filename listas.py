try:
    print( "Iniciando calculo" )
    n = 6 / 2

    print( n )
except Exception as e:
    print( "Desculpe, ocorreu um erro,favor tentar novamente" )


if __name__ == '__main__':
    try:
        pessoas = []
        nome = ''

        while True:
            nome = input("Digite um nome para adicionar na lista(Digite 'sair' para encerrar): ")

            if nome == 'sair':
               break

            pessoas.append(nome)

        print('Pessoas na lista:')
        print(pessoas)

        #ordenar lista forma decrescente
        pessoas.sort(reverse=True)
        print(pessoas)

        #ordenar lista forma crescente
        pessoas.sort()
        print( pessoas )

        #inserir objeto em posicao especifica
        pessoas.insert(2, 'Joao')
        print(pessoas)

        #Limpar lista
        pessoas.clear()
        print(pessoas)

        print(f'quantidade de filipe na lista {pessoas.count("Filipe")}')


        notasDosAlunos = [50, 60, 70, 80]
        mediaDasNotas = lambda notas: sum(notas) / len(notas)

        print(f'A media dos alunos é: {mediaDasNotas(notasDosAlunos)}')



        notasDosAlunos = [50, 60, 70, 80]
        notasFiltradas = list(filter(lambda nota : nota > 80, notasDosAlunos)
        print(notasFiltradas)