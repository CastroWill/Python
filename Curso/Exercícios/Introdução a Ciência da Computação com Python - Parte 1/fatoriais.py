a = int(input('\nDigite um número: '))
while a > 0:
    b = a
    while a > 1:
        b = b * (a-1)
        a -= 1
    print(b)
    a = int(input('\nDigite um número: '))
