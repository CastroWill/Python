import math

def delta(a, b, c):
    return b**2 - 4*a*c

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d))/(2 * a)
        print("A raiz desta equação é", raiz1)
    else:
        if d < 0:
            print("Esta equação não possui raízes reais.")
        else:
            raiz1 = (-b + math.sqrt(d))/(2 * a)
            raiz2 = (-b - math.sqrt(d))/(2 * a)
            if raiz1 <= raiz2:
                print("as raízes da equação são", raiz1,"e", raiz2)
            if raiz1 >= raiz2:    
                print("as raízes da equação são", raiz2,"e", raiz1)
def main():
    a_dig = float(input("Digite o valor de A :"))
    b_dig = float(input("Digite o valor de B :"))
    c_dig = float(input("Digite o valor de C :"))
    imprime_raizes(a_dig, b_dig, c_dig)
