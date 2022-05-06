num = int(input("Digite um número inteiro:"))

num1 = num % 3
num2 = num % 5

if num1 == 0 and num2 == 0:
    print("FizzBuzz")
else:
    print(num)
