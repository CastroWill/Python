import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)



#Essa função devolve em uma lista com todas as frases de um texto.
def frases_texto(sentencas): 
    lista_frases = []
    for i in range(len(sentencas)):
        lista_frases += separa_frases(sentencas[i])
    return lista_frases

#Essa função devolve em uma lista com todas as palavras de um texto.
def palavras_texto(lista_frases):
    lista_palavras = []
    for i in range(len(lista_frases)):
        lista_palavras += separa_palavras(lista_frases[i])
    return lista_palavras

#Essa função devolve a quantidade de letras contidas em um texto.
def conta_letra(lista_palavras):
    quant_letra = 0
    for i in range(len(lista_palavras)):
        quant_letra += len(lista_palavras[i])
    return quant_letra

#Essa função devolve a quantidade de caractéres contidas em um texto.
def conta_caract(texto):
    quant_caract = 0
    for i in texto:
        if i != '.' and i != '?' and i != '!':
            quant_caract += 1
    return quant_caract

#Essa função devolve a quantidade de caractéres contidas em todas as frases do texto.
def conta_caract_frase(lista_frases):
    quant_caract_frase = 0
    for frase in lista_frases:
        for i in frase:
            quant_caract_frase += 1
    return quant_caract_frase

#Essa funcao recebe um texto e deve devolver a assinatura do texto.	
def calcula_assinatura(texto):
    
    ass = []
    sentencas = separa_sentencas(texto)
    lista_frases = frases_texto(sentencas)
    lista_palavras = palavras_texto(lista_frases)
    quant_letra = conta_letra(lista_palavras)

    #Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    wal = quant_letra / len(lista_palavras)
    ass.append(wal)

    #Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    ttr = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    ass.append(ttr)
    
    #Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    hlr = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    ass.append(hlr)
    
    #Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sal = conta_caract(texto) / len(sentencas) 
    ass.append(sal)
    
    #Complexidade de sentença: é o número total de frases divido pelo número de sentenças.
    sac = len(lista_frases) / len(sentencas)
    ass.append(sac)
    
    #Tamanho médio de frase: é a soma do número de caracteres em cada frase dividida pelo número de frases no texto.
    pal = conta_caract_frase(lista_frases) / len(lista_frases)
    ass.append(pal)
    return ass

#Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b):
    as_final = []
    for a in range(len(as_a)):
        for b in range(len(as_b)):
            b = a
            as_final.append(abs(as_a[a] - as_b[b]))
            break
        
    soma = 0
    for s in range(len(as_final)):
        soma += as_final[s]
        
    Sab = soma / 6
    
    return Sab

#Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(Textos, Assinatura):
    assinaturas = []
    for texto in range(len(Textos)):
        assinaturas.append(calcula_assinatura(Textos[texto]))

    ass_comparadas = []

    for ass in range(len(assinaturas)):
        ass_comparadas.append(compara_assinatura(Assinatura, assinaturas[ass]))

    print (ass_comparadas)
    
    menor_Sab = ass_comparadas[0]
    ass = 0
    for Sab in range(len(ass_comparadas)):
        if menor_Sab > ass_comparadas[Sab]:
            ass = Sab     
    return ass 
    
#Função principal    
def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    ass = avalia_textos(textos, ass_cp)
    return print('\nO autor do texto', ass,'está infectado com COH-PIAH')

def teste_main():
    pass
