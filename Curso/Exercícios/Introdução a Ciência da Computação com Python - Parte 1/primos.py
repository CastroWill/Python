n = int(input('Digite um número inteiro positivo > 1: '))
while n > 1:
    fator = 2
    while n%fator != 0:
        fator += 1
    if n%fator == 0 and n == fator:
        print('Primo')
    else:
        print('Não primo!')
    n = int(input('\nDigite um número inteiro positivo > 1: '))
