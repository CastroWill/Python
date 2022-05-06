def remove_repetidos(lista):
    lista1=[]
    for a in range(len(lista)):
        if lista[a] in lista1:
            pass
        else:
            lista1.append(lista[a])
    lista1 = sorted(lista1)
    return lista1

