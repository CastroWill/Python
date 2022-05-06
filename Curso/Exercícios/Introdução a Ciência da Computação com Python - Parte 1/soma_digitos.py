num = int(input("Digite um número inteiro:"))

n = num%10
n1 = 0


while num != 0:
    num //= 10
    n1 = num%10
    n += n1 

print(n)  
