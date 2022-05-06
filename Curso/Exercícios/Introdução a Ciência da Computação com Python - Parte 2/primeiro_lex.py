def primeiro_lex(lista):
    word = lista[0]
    for p in range(1, len(lista)):
        if word > lista[p]:
            word = lista[p]
    return word
