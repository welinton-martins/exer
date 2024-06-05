while (True):
    n = int(input('Digite um numero:'))
    s = '!'+str(n)+'='
    f = 1
    for i in range(n):
        s += str(n-i)
        if (i!=n-1):
            s += '*'
        f *= n-i
    print(s,'=',f)
