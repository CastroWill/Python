def menor_nome(nomes):
    nomesR = []
    menor = 0
    
    for n in range(len(nomes)):
        nomesR.append(nomes[n].strip().capitalize())

    for m in range(1, len(nomesR)):
        if len(nomesR[menor]) > len(nomesR[m]):
            menor = m
            
    return  nomesR[menor]
