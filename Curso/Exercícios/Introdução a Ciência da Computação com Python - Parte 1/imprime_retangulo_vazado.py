l = int(input('\ndigite a largura: '))
a = int(input('digite a altura: '))

x = l
y = a
while a > 0:
    
    if l == 0:
        a -= 1
        l = x
        print()

    while l > 0 and a == y or l > 0 and a == 1:
        if l != 0:
            print('#', end='')
            l -= 1
    
    while l > 0 and a < y and a != 0 or l > 0 and a <= 2 and a != 0:
        if l == x or l == 1:
            print('#', end='')
            l -= 1
        else:
            print(' ', end = '')
            l -= 1

    
