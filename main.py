def print_hi(name):
    print(f'Olá mundo, {name}')

if __name__ == '__main__':
    print_hi('Luiz')

    temperatura = 20
    print(type(temperatura))

    temperatura = 'filipe'
    print(type(temperatura))

    listaNomes = ['filipe', 'daniel', 'rafael']
    print(type(listaNomes))

    idade =29
    print(type(idade))

    dicionarioPessoa = {
        'nome': 'Filipe',
        'idade': idade
    }
    print(dicionarioPessoa)

    numeroComplexo = 5 + 5j
    print(type(numeroComplexo))
    # booleano - comentario no python
    verificação = False
    print(type(verificação))

    variavelNula = None
    print(variavelNula)