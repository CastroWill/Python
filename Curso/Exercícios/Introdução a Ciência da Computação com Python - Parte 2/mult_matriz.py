def sao_multiplicaveis(m1, m2):
    for c in range(len(m1)):
        if len(m1[c]) != len(m2):
            return False
        else:
            return True
