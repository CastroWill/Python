lista = []
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        lista.insert(0, n)
    if n == 0:
        print()
        for i in lista:
            print(i)
        break
