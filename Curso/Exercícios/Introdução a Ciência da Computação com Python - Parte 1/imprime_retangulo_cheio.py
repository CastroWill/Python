l = int(input('\ndigite a largura: '))
a = int(input('digite a altura: '))

x = l
while a > 0:
    while l > 0:
        print('#', end='')
        l -= 1
    a -= 1
    l = x
    print()
