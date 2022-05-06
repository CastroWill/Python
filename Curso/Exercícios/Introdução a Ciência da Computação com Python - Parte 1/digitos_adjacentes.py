num = int(input("Digite um número inteiro:"))
n1 = num

flag = False

if num > -10 and num < 10:
    flag = True
    num = 0

n = num%10
num //= 10
    
while flag == False and num != 0:
    if n == num%10:
        flag = True
        print("sim")
    else:
        n = num%10
        num //= 10
        if num == 0:
            flag = True
if flag == True and num == 0:
    print("não")
