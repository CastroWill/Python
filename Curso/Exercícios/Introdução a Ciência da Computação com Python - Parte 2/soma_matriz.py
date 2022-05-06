def soma_matrizes(m1, m2):
    a = len(m1)
    b = len(m1[0])
    
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False

    if len(m1) == len(m2):
        s_matriz = []
        for l in range(len(m1)):
            linha = []
            for c in range(len(m1[0])):
                linha.append(m1[l][c]+m2[l][c])
            s_matriz.append(linha)
        return s_matriz
    
    else:
        return False
