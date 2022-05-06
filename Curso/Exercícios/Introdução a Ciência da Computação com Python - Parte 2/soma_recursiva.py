def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])
    


    
    
lista = [10,10,10,10,10,10,10,10,10,10]
print(soma_lista(lista))
