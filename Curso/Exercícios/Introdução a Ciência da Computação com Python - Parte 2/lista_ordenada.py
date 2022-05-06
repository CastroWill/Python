def ordenada(lista):
    lista_cop = lista.copy()
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    if lista_cop == lista:
        return True
    else:
        return False
