while (True):
    s = input('Digite uma string:')
    f = ''
    for i in range(len(s)):
        f += s[(len(s)-1)-i]
    print(f)
