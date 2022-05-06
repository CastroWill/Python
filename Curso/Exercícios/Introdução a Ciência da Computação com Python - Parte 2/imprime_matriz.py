def imprime_matriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if c == len(matriz[l]) - 1:
                print(matriz[l][c], end = "")
            else:
                print(matriz[l][c], end = " ")
        print()
