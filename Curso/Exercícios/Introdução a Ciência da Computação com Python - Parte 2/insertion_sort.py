def insertion_sort(lista):
    '''Cria slices durante a verificação para ir ordenando as listas'''
    for i in range(len(lista)):
        pos = i
        valorAtual = lista[i]
        while pos > 0 and lista[pos-1] > valorAtual:
            lista[pos] = lista[pos-1]
            pos -= 1
        lista[pos] = valorAtual
    return lista
