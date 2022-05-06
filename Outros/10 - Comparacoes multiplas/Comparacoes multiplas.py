
"""n1 = int( input("Digite a primeira nota: "))
n2 = int( input("Digite a segunda nota: "))
n3 = int( input("Digite a terceira nota: "))
n4 = int( input("Digite a quarta nota: "))
print("A sua média é:", ((n1+n2+n3+n4)/4))"""


"""hrd = int( input("Digite quantas hr vc trabalha em dia: "))
shr = int( input("Digite quanto vc ganha por hora: "))
qtd = int( input("Digite quantos dias vc trabalha no mes: "))
print ("O seu salario eh igual a: ", hrd*shr*qtd)"""

"""vlr = int(input("Digite o valor do saque: ")) #Solicita ao usario o vlr de saque

if 10 <= vlr <= 600:        #Verifica se o vlr esta dentro dos limites determinados, usaremos o vlr R$567 de exemplo
    cen = vlr//100          #pega o vlr inteiro da conta, entao 567//100 = 5
    nt50 = vlr%100//10//5   #567%100 = 67 (567/100 = 5,67, nesse caso o resto eh 67), 67//10 = 6, 6//5 = 1
    nt10 = vlr%100//10%5    #567%100 = 67, 67//10 = 6, 6%5 = 1
    nt5 = vlr%100%10//5     #567%100 = 67, 67%10 = 7, 7//5 = 1
    nt1 = vlr%100%10%5      #567%100 = 67, 67%10 = 7, 7%5 = 2
    print ("Voce recebera: ")
    if cen > False:     #Verifica se ha notas de 100 reais a serem entregues
        print ("", cen,"nota(s) de 100 reais")  #Impime a mensagem na tela para alertar o usuario
    if nt50 > False:    #Verifica se ha notas de 50 reais a serem entregues
        print ("", nt50,"nota(s) de 50 reais")
    if nt10 > False:    #Verifica se ha notas de 10 reais a serem entregues
        print ("", nt10,"nota(s) de 10 reais")
    if nt5 > False:     #Verifica se ha notas de 5 reais a serem entregues
        print ("", nt5,"nota(s) de 5 reais")
    if nt1 > False:     #Verifica se ha notas de 1 real a serem entregues
        print ("", nt1,"nota(s) de 1 real")
        
    
else: #O programa entrara nesta condicao quando o usuario exceder os limites impostos
    print(" O valor nao corresponde aos limites diario de saque entre R$10,00 e R$600,00.") #Impime a mensagem na tela para alertar o usuario"""

"""vlr1 = int( input("Digite a base: " ))
vlr2 = int( input("Digite o expoente: "))
count = 0
while count < vlr2-1:
    vlr1 = vlr1*vlr2
    count = count + 1
print (vlr1)"""

"""vlr1 = int (input ("Digite um valor:"))
count = vlr1
while count > 1:
    vlr1 = vlr1*(count-1)
    count = count - 1
print (vlr1)"""

