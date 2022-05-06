def conta_letras(frase, contar = 'vogais'):
    count = 0
    if contar == 'vogais':
        for c in range(len(frase)):
            if ord(frase[c]) == 65 or ord(frase[c]) == 97:
                count += 1
            if ord(frase[c]) == 69 or ord(frase[c]) == 101:
                count += 1
            if ord(frase[c]) == 73 or ord(frase[c]) == 105:
                count += 1
            if ord(frase[c]) == 79 or ord(frase[c]) == 111:
                count += 1
            if ord(frase[c]) == 85 or ord(frase[c]) == 117:
                count += 1
            
    
    if contar == 'consoantes':
        for c in range(len(frase)):
            if ord(frase[c]) >= 66 and ord(frase[c]) <= 90 or ord(frase[c]) >= 98 and ord(frase[c]) <= 122:
                if ord(frase[c]) != 65 and ord(frase[c]) != 97:
                    if ord(frase[c]) != 69 and ord(frase[c]) != 101:
                        if ord(frase[c]) != 73 and ord(frase[c]) != 105:
                            if ord(frase[c]) != 79 and ord(frase[c]) != 111:
                                if ord(frase[c]) != 85 and ord(frase[c]) != 117:
                                   count += 1
    
    return count
