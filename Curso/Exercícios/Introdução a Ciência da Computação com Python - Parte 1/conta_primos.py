def éPrimo(n):
    x = 2
    while x <= n:
        if n%x == 0 and x != n:
            return False
        if x == n:
            return True
        x += 1
    
def n_primos(n):
    x = 2
    c = 0
    while x <= n:
        if éPrimo(x) == True:
            c += 1
        x += 1
    return c
        
        
