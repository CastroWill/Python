import os

from pyftpdlib.handlers import FTPHandler #Control Connection
from pyftpdlib.servers import FTPServer #Server Configuration
from pyftpdlib.authorizers import DummyAuthorizer #Users

'''
    Obs1: é necessário criar regra no firewall para que outros dispositivos tenham
    comunicação com o servidor, tanto para o cliente quanto para o servidor.
    Obs2: 'elradfmwMT' da permissão total ao usuário.
'''

def main():
    #Definindo configurações de usuários que poderão acessar o servidor
    homedir = 'C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Files_Received'
    authorizer = DummyAuthorizer()
    authorizer.add_user('Rasp1', '12345', homedir, perm='elradfmwMT')
    authorizer.add_anonymous(homedir)
    
    #Configuração e controle do servidor 
    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
    server = FTPServer(('192.168.50.60', 2121), ftp_handler)
    server.serve_forever()


if __name__ == '__main__':
    #try:
    main()
    '''
    except Exception:
        print("Verificar conexão com a rede.")
    '''
