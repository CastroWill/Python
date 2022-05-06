#n é o número de peças inicial 50
#m é o número máximo de peças que é possível retirar em uma rodada 10


def computador_escolhe_jogada(n, m):
        ret = m
        while 1:
                n1 = n - ret
                if n1%(m+1) == 0:
                        if ret != 1:
                                print('\nO computador tirou', str(ret),'peças.')
                                return ret
                        else:
                                print('\nO computador tirou uma peça.')
                                return ret
                if m == 1:
                        print('\nO computador tirou uma peça.')
                        return m
                else:
                        ret -= 1
                        if ret == 0:
                                print('\nO computador tirou', str(m),'peças.')
                                return m

       
def usuario_escolhe_jogada(n, m):
        ret = int(input('\nQuantas peças você vai tirar? '))
        if ret == 1:
                if ret == 1:
                        print('\nVocê tirou uma peça.')
                        return 1
        if ret != 1 and ret <= m:
                print('Voce tirou ', str(ret),' peças.')
                return ret    
        if ret > m or ret <= 0 or ret > n:
                return ret

        
        
def partida():
        #Começo da partida
        n = int(input('\nQuantas peças? ')) 
        m = int(input('Limite de peças por jogada? '))

        #Usuário começa
        if n%(m+1) == 0 and n != 0: 
                print('\nVoce começa!')
                while n != 0:
                        
                        #Vez do usuário
                        ret = usuario_escolhe_jogada(n, m)
                        while ret > m:
                                print('\nOops! Jogada inválida! Tente de novo.')
                                ret = usuario_escolhe_jogada(n, m)

                        #Peças restantes
                        n = n - ret

                        if n == 1:
                                print('Agora resta apenas uma peça no tabuleiro.')
                        else:
                                print('Agora restam ', str(n),' peças no tabuleiro.')

                        #Vez da máquina
                        ret = computador_escolhe_jogada(n, m)

                        #Peças restantes
                        n = n - ret

                        if n != 0:
                                print('Agora restam ', str(n),' peças no tabuleiro.')
                        if n == 0:
                                print('Fim do jogo! O computador ganhou')
                                break

                  
        if n%(m+1) != 0 and n != 0: #Máquina começa
                print('\nComputador começa!')
                while n != 0:
                        
                        #Vez da Máquina
                        ret = computador_escolhe_jogada(n, m)

                        #Peças restantes
                        n = n - ret
                                
                        if n != 0:
                                print('Agora restam ', str(n),' peças no tabuleiro.')
                        if n == 0:
                                print('Fim do jogo! O computador ganhou')
                                break
                        
                        #Vez do usuário
                        ret = usuario_escolhe_jogada(n, m)
                        while ret > m:
                                #Se o número de peças a serem retiradas for maior que o limite
                                print('\nOops! Jogada inválida! Tente de novo.')
                                ret = usuario_escolhe_jogada(n, m)
                                
                        #Peças restantes
                        n = n - ret

                        if n == 1:
                                print('Agora resta apenas uma peça no tabuleiro.')
                        else:
                                print('Agora restam ', str(n),' peças no tabuleiro.')

def campeonato():
        print('\n**** Rodada 1 ****')
        partida()
        print('\n**** Rodada 2 ****')
        partida()
        print('\n**** Rodada 3 ****')
        partida()
        print('\n**** Final do campeonato! ****')
        print('\nPlacar: Você 0 X 3 Computador')

    
print('\nBem-vindo ao jogo do NIM! Escolha:\n')
esc = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

if esc == 1:
        print('\nVoce escolheu jogar uma partida isolada!')
        partida()
else:
        print('\nVoce escolheu um campeonato!')
        campeonato()



