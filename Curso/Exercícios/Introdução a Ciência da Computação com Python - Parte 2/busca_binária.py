
'''
Busca binária só funciona em lista já ordenadas.

'''
def main():
    import time
    
    tempoA= time.time()
    resp = busca_binaria([5, 6, 9, 10, 25, 36 , 55, 500, 600, 800 , 2300], 36)
    print('\n', resp)
    print("Tempo de execução da Busca Binária com recursão: " + str(time.time()-tempoA))

    tempoA= time.time()
    resp1 = busca([5, 6, 9, 10, 25, 36 , 55, 500, 600, 800 , 2300], 36)
    print('\n', resp1)
    print("Tempo de execução da Busca Binária sem recursão: " + str(time.time()-tempoA))

def busca(lista, elemento): 
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False

def busca_binaria(lista, elemento, min = 0, max = None):
    
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max - min) //2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1 , max)
    else:
        return meio



if __name__ == '__main__':

    main()
