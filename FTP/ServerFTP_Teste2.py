import os

from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

'''
    Obs1: é necessário criar regra no firewall para que outros dispositivos tenham
    comunicação com o servidor, tanto para o cliente quanto para o servidor.
'''

def main():
    homedir = 'C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Relatórios'
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', homedir, perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())
    '''
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = 30720  # 30 Kb/sec (30 * 1024)
    dtp_handler.write_limit = 30720  # 30 Kb/sec (30 * 1024)
    '''
    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
    # have the ftp handler use the alternative dtp handler class
    #ftp_handler.dtp_handler = dtp_handler

    server = FTPServer(('10.244.40.104', 2121), ftp_handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
