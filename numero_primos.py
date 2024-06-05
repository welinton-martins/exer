while(True):
    n = int(input('Digite o um numero:'))
    s = str(n)
    f = 1
    for i in range(n):
        s += str(n-i)+','
        f /= n-i
    #for i in range(n):
    if (n == 2 or int(s[1]) % 2 != 0):
        s=''
        for i in range(n):
            s += str(n-i)+','
        for i in s[:-1].split(','):
            if(i != 0 and int(i) % 2 != 0):
                print(i)
#3, 5, 7, 11, 13, 17, 19,git 
