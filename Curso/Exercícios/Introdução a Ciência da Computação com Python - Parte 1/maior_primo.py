def maior_primo(x):
    if Primo(x) == 10:
        return x
    else:
        flag = x - 1
        while flag != 1:
            if Primo(flag) == 10:
                return flag
                flag = 1                
            else:
                flag = flag - 1  

def Primo(num):

    import math
    
    if num == 2 or num == 3 or num == 5 or num == 7:
        return 10
    if (math.sqrt(num))%1 == 0:
        return 100
    else:
        pasg = 2
        rest = 0
        while pasg != 9:
            rest = num%pasg
            if rest == 0:
                return 100
                pasg = 9
            else:
                pasg += 1
        if rest > 0 and rest <= 9: #Todo número primo tem o resto maior que 0 e menor ou igual a 9
            return 10
        


    
    
