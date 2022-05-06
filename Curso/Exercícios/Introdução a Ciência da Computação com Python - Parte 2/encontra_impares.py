def encontra_impares(lista, impares = None):
    if impares == None:
        impares = []
        
    if len(lista) == 1:
        if lista[0] % 2 != 0:
            impares.extend([lista[0]])
            return impares
        else:
            return impares
    else:
        if lista[0] % 2 != 0:
            impares.extend([lista[0]])
            
        encontra_impares(lista[1:], impares)
        return impares

'''
lista = [13]
len(lista)
print(encontra_impares(lista))
'''
