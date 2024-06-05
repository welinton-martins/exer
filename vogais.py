while (True):
    s = input('Digite uma string:')
    v = ['a','e','i','o','u']
    c = 0
    for i in range(len(s)):
        for j in v:
            if (j==s[i]):
                c+=1
    print('Quantidate de vogais:',c)
