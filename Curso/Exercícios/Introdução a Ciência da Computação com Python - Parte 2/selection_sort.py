def ordena(lista):
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
