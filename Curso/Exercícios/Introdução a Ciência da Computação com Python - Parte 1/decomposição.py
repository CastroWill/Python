print('Decomposição em fatores de números primos!\n')
n=1
while n > 0:
    n = int(input('Digite um número inteiro positivo não nulo:'))
    print(n, '=', end=' ')
    a = 2
    if n == 1:
        print(n)
    while n > 1:
        while n%a == 0:
            n = n/a
            if n != 1:
                print(a, 'x', end=' ')
            if n == 1:
                print(a)
                break
        else:
            a += 1
    
