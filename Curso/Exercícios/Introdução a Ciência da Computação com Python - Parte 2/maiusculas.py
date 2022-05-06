def maiusculas(frase):
    fraseM = ''
    for p in range(len(frase)):
        assert frase[p] != 'ç' and frase[p] != 'á'
        assert frase[p] != 'ã' and frase[p] != 'É'
        if ord(frase[p]) >= 65 and ord(frase[p]) <= 90:
            fraseM += frase[p]
    return fraseM
