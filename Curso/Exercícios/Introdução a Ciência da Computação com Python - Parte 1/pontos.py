import math

num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))
num3 = int(input("Digite o terceiro número inteiro:"))
num4 = int(input("Digite o quarto número inteiro:"))

d = math.sqrt(((num1-num2)**2)+((num3-num4)**2))

if d < 10:
    print("perto")
else:
    print("longe")
