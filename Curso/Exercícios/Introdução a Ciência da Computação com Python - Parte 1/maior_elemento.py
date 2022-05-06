def maior_elemento(lista):
    x = lista[0]
    for a in range(len(lista)):
        if x < lista[a]:
            x = lista[a]
    return x
        
