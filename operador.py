def SecondOperand():
    print('Avaliando segundo operador')
    return True

if __name__ == '__main__':
    a = False and SecondOperand()
    print(a)
    b =True and SecondOperand()
    print(b)

    a = False or SecondOperand()
    print( a )
    b = True or SecondOperand()
    print( b )



if __name__ == '__main__':
    valido = False

    print(not valido)
    print(not True)