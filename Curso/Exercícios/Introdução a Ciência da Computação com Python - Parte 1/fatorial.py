num = int(input("Digite o valor de n:"))

mult = num

if mult == 0:
    print("1")
else:  
    while mult > 1:
        mult += - 1
        num = num * mult
    print(num)
