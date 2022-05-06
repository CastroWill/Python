def éHipotenusa(n):
    import math
    i = 1
    j = 1
    while i <= n:
        while j <= n:
            if (i**2 + j**2) == (n**2):
                return True
            j += 1
        i += 1
        j = 1
    else:
        return False

def soma_hipotenusas(n):
    x = 1
    s_hip = 0
    while x <= n:
        if éHipotenusa(x) == True:
            s_hip += x
        x += 1
    return s_hip
