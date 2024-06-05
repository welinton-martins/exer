while (True):
    n = int(input('Digite um numero:'))
    op = input('Digite a operacao:')
    if(op=='+'):
        for i in range(1,10):
            print(n,op,i,'=',n+i)
    elif (op=='-'):
        for i in range(1,10):
            print(n,op,i,'=',n-i)
    elif (op=='*'):
        for i in range(1,10):
            print(n,op,i,'=',n*i)
    elif (op=='/'):
        for i in range(1,10):
            print(n,op,i,'=',n/i)
