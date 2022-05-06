num = int(input("Digite um número inteiro:"))

import math

if num == 2 or num == 3 or num == 5 or num == 7:
    print("primo")

if (math.sqrt(num))%1 == 0:
    print("não primo")
    
else:
    pasg = 2
    rest = 0
    while pasg != 9:
        rest = num%pasg
        if rest == 0:
            print("não primo")
            pasg = 9
        else:
            pasg += 1
    if rest > 0 and rest <= 9: #Todo número primo tem o resto maior que 0 e menor ou igual a 9
        print("primo")
        


    
    
