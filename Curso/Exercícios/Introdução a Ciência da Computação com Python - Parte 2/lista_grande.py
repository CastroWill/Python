def lista_grande(n):
    import sys, random
    lista = []
    while len(lista) != n:
        lista.append(random.randint(0, sys.maxsize))
    return lista
    
