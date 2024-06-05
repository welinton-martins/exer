while (True):
    n1 = int(input('Digite o 1 numero:'))
    n2 = int(input('Digite o 2 numero:'))
    op = input('Digite a operacao:')
    if(op=='+'):
        print(n1+n2)
    elif (op=='-'):
        print(n1-n2)
    elif (op=='*'):
        print(n1*n2)
    elif (op=='/'):
        if (n2 != 0):
            print('Divisao por zero')
        print(n1/n2)
