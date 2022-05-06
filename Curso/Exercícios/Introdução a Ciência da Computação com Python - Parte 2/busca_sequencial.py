def busca(lista, elemento):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == elemento:
            pos = i 

    if pos != -1: return pos
    elif pos == -1: return False
