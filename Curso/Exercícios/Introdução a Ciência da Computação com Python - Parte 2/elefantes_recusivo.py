def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n-1)

def elefantes(n, x = 1):
    if x > n:
        return ''
    else:
        if n == 1:
            return 'Um elefante incomoda muita gente\n'
        else:
            if x == 1:
                x += 1
                return 'Um elefante incomoda muita gente\n' + str(x)+' elefantes ' + incomodam(x) + 'muito mais\n' + str(x) + ' elefantes incomodam muita gente\n' +  elefantes(n, x+1)
            elif x == n:
                return str(x)+' elefantes ' + incomodam(x) + 'muito mais'
            else:
                return str(x)+' elefantes ' + incomodam(x) + 'muito mais\n' + str(x) + ' elefantes incomodam muita gente\n' +  elefantes(n, x+1)
        
